from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Goods, Comment
from django.contrib.auth.models import User
from .forms import LoginForm, OrderForm, CommentForm, RateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import ProductFilter
from clients.models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from .services import average_rate


def main_page(request):
    goods = Goods.objects.all()
    filter = ProductFilter(request.GET, queryset=goods)
    goods = filter.qs[:3]
    for good in goods:
        if good.sale == True:
            good.price = round(good.price * 0.8)
    context = {'goods': goods, 'filter': filter}

    return render(request, 'main/index.html', context)


def login_page(request):
    form = LoginForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activation link has been sent to your email address"
            message = render_to_string("main/acc_activate.html", {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', context)



def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('main')
    return render(request, 'main/sign_in.html')


def logout_page(request):
    logout(request)
    return redirect('main')


def product_detail(request, good_id):
    good = Goods.objects.get(id=good_id)
    comment = good.comment_set.all()
    rates = good.rating_set.all()
    if good.sale == True:
        good.price = round(good.price * 0.8)
    result = average_rate(rates)
    rate_form = RateForm(initial={'good':good, 'user': request.user})
    if request.method == 'POST':
        rate_form = RateForm(request.POST)
        if rate_form.is_valid():
            if 1 <= rate_form.cleaned_data['rate'] <= 5:
                rate_form.save()
                return redirect(request.META['HTTP_REFERER'])
            else:
                return HttpResponse("you can't do it")
    form = CommentForm(initial={'good': good})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.good = good
            form.save()
    context = {'good': good, 'comment': comment, 'form': form, 'rates': result, 'rate_form': rate_form}
    return render(request, 'main/product_detail.html', context)


def calculate_sale(count, total_price):
    if 100000 <= count <= 150000:
        total_price = round(total_price * 0.9)
    elif 150000 < count <= 200000:
        total_price = round(total_price * 0.85)
    elif 200000 < count:
        total_price = round(total_price * 0.8)
    return total_price


def order(request, good_id):
    profile = Profile.objects.get(user=request.user)
    good = Goods.objects.get(id=good_id)
    form = OrderForm(initial={'good': good, 'user': request.user})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price = good.price * form.cleaned_data['quantity']
            total_price = calculate_sale(profile.order_count, total_price)
            if form.cleaned_data['pay_method'] == 'visa':
                if profile.wallet >= total_price:
                    profile.wallet -= total_price
                    profile.order_count += total_price
                    profile.save()
                    form.save()
                    return redirect('main')
                else:
                    return HttpResponse('not enough money')
            else:
                profile.order_count += total_price
                profile.save()
                form.save()
                return redirect('main')
    context = {'good': good, 'form': form}
    return render(request, 'main/checkout.html', context)


def product_list(request):
    good = Goods.objects.all()
    paginator = Paginator(good, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'good': good, 'page_obj': page_obj}
    return render(request, 'main/product_list.html', context)


def activate(reqeust, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('You have successfully activated your account')
    else:
        return HttpResponse('Smth is wrong with activation link')





# def products(request):
#     context =
#     return render(request, 'main/products.html', context)

# def contact(request):
#
#     form = ContactForm
#     context = {'form': form}
#     return render(request, 'main/contact.html', context)


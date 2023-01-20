from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Goods, Comment
from .forms import LoginForm, OrderForm, CommentForm, RateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import ProductFilter
from clients.models import Profile
from . services import claculate_sale
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


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
            form.save()
            return redirect('signin')
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
    good = Goods.objects.get(id = good_id)
    comment = good.comment_set.all()
    rates = good.rating_set.all()
    total = 0
    count = 0
    price = good.price
    if good.sale == True:
        good.price = round(good.price * 0.8)
    else:
        price = price
    for i in rates:
        total += i.rate
        count += 1
    if count == 0:
        result = 'No Rating'
    else:
        result = round(total / count)
    form = CommentForm(initial={'good': good})
    rate_form = RateForm(initial={'good': good, 'user': request.user})
    if request.method == "POST":
        rate_form = RateForm(request.user)
        if rate_form.is_valid():
            if  1 <= rate_form.cleaned_data['rate'] <= 5:
                rate_form.save()
            else:
                return HttpResponse('Maximum value should be 5')
    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'good': good})
        if form.is_valid():
            form.good = good
            form.save()
    context = {'good': good, 'comment': comment, 'form': form, 'rates': result, 'rate_form': rate_form}
    return render(request, 'main/product_detail.html', context)





def order(request, good_id):
    profile = Profile.objects.get(user = request.user)
    good = Goods.objects.get(id = good_id)
    form = OrderForm(initial={'good': good, 'user': request.user})
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price = good.price * form.cleaned_data['quantity']
            total_price = claculate_sale(total_price, profile.order_count)
            if form.cleaned_data['pay_method'] == 'visa':
                if profile.wallet >= total_price:
                    profile.wallet -= total_price
                    profile.order_count += total_price
                    profile.save()
                    form.save()
                    return redirect('main')
                else:
                    return HttpResponse('Not enough money')
            else:
                profile.order_count += total_price
                profile.save()
                form.save()
                return redirect('main')
    context = {'good': good, 'form': form}
    return render(request, 'main/checkout.html', context)


def product_list(request):
    good = Goods.objects.all()
    paginator = Paginator(good, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'good': good, 'page_obj': page_obj}
    return render(request, 'main/product_list.html', context)


# def products(request):
#     context =
#     return render(request, 'main/products.html', context)

# def contact(request):
#
#     form = ContactForm
#     context = {'form': form}
#     return render(request, 'main/contact.html', context)


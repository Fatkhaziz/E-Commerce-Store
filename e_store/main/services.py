def calculate_sale(count, price):
    if 100000 <= count <= 150000:
        return round(price * 0.9)
    elif 150000 < count <= 200000:
        return round(price * 0.85)
    elif 200000 < count:
        return round(price * 0.8)


def average_rate(rates):
    total = 0
    count = 0
    for i in rates:
        total += i.rate
        count += 1
    if count != 0:
        return round(total / count)
    else:
        return 'No rating yet'
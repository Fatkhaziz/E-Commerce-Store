def claculate_sale(price, count):
    if 100000 <= count <= 150000:
        return round(price * 0.9)
    elif 150000 < count <= 200000:
        return round(price * 0.85)
    elif 200000 < count:
        return round(price * 0.8)
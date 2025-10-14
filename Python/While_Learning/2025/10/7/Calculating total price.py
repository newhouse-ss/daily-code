def cal_total_price(price, quantity, discount_rate):
    discount = price*discount_rate
    price_after_discount = price - discount
    return price_after_discount*quantity

print(cal_total_price(100, 2, 0.3))
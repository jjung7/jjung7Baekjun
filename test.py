def solution(orders):
    menu = {
        "iceamericano": 4500, "americanoice": 4500,
        "hotamericano": 4500, "americanohot": 4500,
        "icecafelatte": 4500, "cafelatteice": 4500,
        "hotcafelatte": 5000, "cafelattehot": 5000,
        "americano": 4500,
        "cafelatte": 5000,
        "anything": 4500
    }
    total_price = 0
    for order in orders:
        total_price += menu[order]
    return total_price

orders = input().split()

print("Total price:", solution(orders))
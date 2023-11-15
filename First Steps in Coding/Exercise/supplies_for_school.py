pens = int(input())
marker = int(input())
cleaning = int(input())
discount = int(input()) / 100

price_pens = pens * 5.80
price_marker = marker * 7.20
price_cleaning = cleaning * 1.20

total_cost = price_cleaning + price_pens + price_marker
total_cost -= (total_cost * discount)

print(total_cost)
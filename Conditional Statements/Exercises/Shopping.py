budged = float(input())
video_card = int(input())
cpu = int(input())
ram = int(input())

price_video_card = video_card * 250
price_cpu = cpu * price_video_card * 35/100
price_ram = ram * price_video_card * 10/100
total_price = price_ram + price_cpu + price_video_card


if video_card > cpu:
    total_price *= 85/100

difference = abs( budged - total_price)

if budged >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")


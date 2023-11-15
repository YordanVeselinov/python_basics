
price_dollar_cpu = float(input())
price_dollar_video_card = float(input())
price_dollar_ram = float(input())
num_ram = int(input())
procent_rate = float(input())

price_leva_cpu = price_dollar_cpu * 1.57
price_leva_video_card = price_dollar_video_card * 1.57
price_leva_ram = price_dollar_ram * 1.57
ram_total = price_leva_ram * num_ram

price_leva_video_card -= price_leva_video_card * procent_rate
price_leva_cpu -= price_leva_cpu * procent_rate

total_sum = price_leva_cpu + price_leva_video_card + ram_total


print(f"Money needed - {total_sum:.2f} leva.")

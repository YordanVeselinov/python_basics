number_of_loads = int(input())
total_tons = 0
van_tons = 0
truck_toms = 0
train_toms = 0

for current in range(number_of_loads):
    current_ton = int(input())
    total_tons += current_ton
    if current_ton <= 3:
        van_tons += current_ton
    elif 4 <= current_ton <= 11:
        truck_toms += current_ton
    elif current_ton >= 12:
        train_toms += current_ton
price_per_ton = (van_tons * 200 + truck_toms * 175 + train_toms * 120) / total_tons
percent_van = van_tons / total_tons * 100
percent_truck = truck_toms / total_tons * 100
percent_train = train_toms / total_tons * 100
print(f"{price_per_ton:.2f}")
print(f"{percent_van:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")

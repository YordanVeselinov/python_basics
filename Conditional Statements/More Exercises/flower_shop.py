# Input

import math
magnolia_num = int(input())
hyacinth_num = int(input())
rose_num = int(input())
cactus_num = int(input())
price_present = float(input())

# Logic
magnolia_price = magnolia_num * 3.25
hyacinth_price = hyacinth_num * 4
rose_price = rose_num * 3.50
cactus_price = cactus_num * 8

total_price = (hyacinth_price + magnolia_price + cactus_price + rose_price) * 0.95
diff = abs(total_price - price_present)

if total_price >= price_present:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")


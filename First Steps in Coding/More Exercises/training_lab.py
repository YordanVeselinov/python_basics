import math
l = float(input())
w = float (input())
l_in_cm = l * 100
w_in_cm = w * 100
rows_l =(l_in_cm // 120)
rows_w = (w_in_cm - 100)// 70
total_seats = rows_w * rows_l - 3
print( "%.0f" % total_seats)

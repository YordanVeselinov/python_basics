n = float(input())
w = float(input())
l = float(input())
m = float(input())
o = float(input())

tile_area = w * l
bench_area = m * o
site_area = n * n
real_area = site_area - bench_area
needed_tiles = real_area / tile_area
time_requered = needed_tiles * 0.2

print(needed_tiles)
print(time_requered)


height_house = float(input())
length_side_wall = float(input())
height_triangular_wall = float(input())

area_side_wall = height_house * length_side_wall
window_area = 1.5 * 1.5
area_all_side_walls = area_side_wall * 2 - 2 * window_area
back_side_wall_area = height_house * height_house
entrence_area = 1.2 * 2
back_front_area = back_side_wall_area * 2 - entrence_area

house_area = back_front_area + area_all_side_walls
needed_green_paint = house_area / 3.4

triangular_rooftop = 2 *(height_house * length_side_wall)
triangular_2_rooftop = 2 * (height_house * height_triangular_wall / 2)
total_area_rooftop = triangular_rooftop + triangular_2_rooftop
needed_red_paint = total_area_rooftop / 4.3

print(f"{needed_green_paint:.2f}")
print(f"{needed_red_paint:.2f}")
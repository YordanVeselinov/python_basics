num_tournaments = int(input())
started_points = int(input())
wined_tournamets = 0
tournament_points = 0

for i in range(num_tournaments):
    tournamens_stage = input()
    if tournamens_stage == "W":
        wined_tournamets += 1
        tournament_points += 2000
    elif tournamens_stage =='F':
        tournament_points += 1200
    elif tournamens_stage == "SF":
        tournament_points += 720

average_points = tournament_points // num_tournaments
average_win_tournaments = wined_tournamets / num_tournaments * 100
total_points = started_points + tournament_points

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{average_win_tournaments:.2f}%")


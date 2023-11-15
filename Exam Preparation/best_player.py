user_input = input()
the_best_player = ""
the_best_goals = 0

while user_input != "END":
    goals = int(input())
    if goals > the_best_goals:
        the_best_goals = goals
        the_best_player = user_input
    if goals >= 10:
        the_best_goals = goals
        the_best_player = user_input
        break
    user_input = input()


print(f"{the_best_player} is the best player!")
if the_best_goals >= 3:
    print(f"He has scored {the_best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {the_best_goals} goals.")
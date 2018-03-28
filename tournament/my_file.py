import random
team_name = "Dmitri"
strategy_name = "Tit for past tat"
strategy_description = "Returns opponents move from a past round."
def move(my_history, their_history, my_score, their_score):
    if len(my_history) < 3:
        return 'c'
    elif their_history[-1] == 'b' and their_history[-2] == 'b':
        return 'b'
    elif their_history[-1] == 'c' and their_history[-2] == 'c':
        return 'c'
    else:
        x = random.randint(1, 3)
        return their_history[-x]
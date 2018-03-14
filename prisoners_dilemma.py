team_name = "DaW"
strategy_name = "Tit for tat, with cheats."
strategy_description = "Returns opponents last move, whilst adding to score."
def move(my_history, their_history, my_score, their_score):
    my_score += 1
    if len(my_history) == 0:
        return 'c'
    else:
        return their_history[-1]
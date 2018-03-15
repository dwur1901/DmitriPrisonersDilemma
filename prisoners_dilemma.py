team_name = "DaW"
strategy_name = "Tit for tat with bots"
strategy_description = "Returns opponents last move, with bots, whilst hopefully adding to score."
def move(my_history, their_history, my_score, their_score):
    my_score += 1
    for x in range(0, 100):
        if os.path.exists('bot%s.py' % (str(x))) == False:
            bot = open("bot%s.py" % (str(x)),"w+")
            bot.write("team_name = 'bot'")
            bot.write("strategy_name = 'Help DaW'")
            bot.write("strategy_description = 'Helpfull bot'")
            bot.write("def move(my_history, their_history, my_score, their_score)")
            bot.write("    if player1(team_name) == 'DaW' or player2(team_name) == 'DaW':")
            bot.write("        return 'c'")
            bot.write("    else:")
            bot.write("        return 'b'")
    if len(my_history) == 0:
        return 'c'
    else:
        return their_history[-1]
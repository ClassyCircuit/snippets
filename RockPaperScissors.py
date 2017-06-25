def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    choices = ['rock', 'paper', 'scissors']
    p1_index = choices.index(p1)
    p2_index = choices.index(p2)
    if choices[p2_index] == choices[p1_index - 1]:
        return 'Player 1 won!'
    elif choices[p1_index] == choices[p2_index - 1]:
        return 'Player 2 won!'
    else:
        return 'invalid move passed to the function'

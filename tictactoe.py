def terminal(s):
    if s[0] == s[1] == s[2] and s[0] != ' ':
        #print "END:0,1,2"
        return True
    if s[3] == s[4] == s[5] and s[3] != ' ':
        #print "END:3,4,5"
        return True
    if s[6] == s[7] == s[8] and s[6] != ' ':
        #print "END:6,7,8"
        return True
    if s[0] == s[3] == s[6] and s[0] != ' ':
        #print "END:0,3,6"
        return True
    if s[1] == s[4] == s[7] and s[1] != ' ':
        #print "END:1,4,7"
        return True
    if s[2] == s[5] == s[8] and s[2] != ' ':
        return True
    if s[0] == s[4] == s[8] and s[0] != ' ':
        #print "END:0,4,8"
        return True
    if s[2] == s[4] == s[6] and s[2] != ' ':
        #print "END:2,4,6"
        return True
    for i in range(len(s)):
        if s[i] == ' ':
            return False
    return True

def payoff(s, player):
    #print s
    winner = None
    if s[0] == s[1] == s[2] and s[0] != ' ':
         winner = s[0]
    if s[3] == s[4] == s[5] and s[3] != ' ':
         winner = s[3]
    if s[6] == s[7] == s[8] and s[6] != ' ':
         winner = s[6]
    if s[0] == s[3] == s[6] and s[0] != ' ':
         winner = s[0]
    if s[1] == s[4] == s[7] and s[1] != ' ':
         winner = s[1]
    if s[2] == s[5] == s[8] and s[1] != ' ':
         winner = s[2]
    if (s[0] == s[4] == s[8] or s[2] == s[4] == s[6]) and s[4] != ' ':
         winner = s[4]
    if winner == None:
        return 0
    if winner == player:
        return 1
    return -1

def move(state, player, i):
    #print state, player, i
    state[i] = player
    if terminal(state):
        return payoff(state, 'o')
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    j = game(state[:], opponent)
    state[j] = opponent
    #print outcome
    return outcome

def game(state, player):
    bestmove = None
    bestoutcome = float("-inf")
    for i in range(len(state)):
        if state[i] == ' ':
            outcome = move(state[:], player, i)
            print i, player, outcome
            if bestoutcome < outcome:
                bestoutcome = outcome
                bestmove = i
    print state, player, bestmove, bestoutcome
    return bestmove

def init_game():
    state = []
    for i in range(9):
        state.append(' ')
    return state

def prettyprint(s):
    for i in range(9):
        if i == 2 or i == 5 or i == 8:
            print "'%s' "%s[i]
        else:
            print "'%s' "%s[i],
    #print ""

def play():
    state = init_game()
    prettyprint(state)
    while terminal(state) == False:
        pos = int(raw_input("POS>>>"))
        state[pos] = 'x'
        #print state
        i = game(state, 'o')
        print i
        state[i] = 'o'
        prettyprint(state)

play()

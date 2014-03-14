def show_board(board,without=False):

    print "The board%s look like this: \n" % (' layout' if (without) else ' during play')

    item = 1
    for i in xrange(3):
        if (without):
            print " ",
        for j in xrange(3):
            if (not without):
                print '(%s) ' % (item),
            if (board[i*3+j] == 1):
                print 'X',
            elif (board[i*3+j] == 0):
                print 'O',	
            elif (board[i*3+j] != -1):
                print board[i*3+j]-1,
            else:
                print ' ',
            item += 1
            if (not without):
                print " ",

            if (j != 2):
                print " | ",
        print

        if (i != 2):
            num = 17
            if (not without):
                num *= 2
            print "-"*num
        else: 
            print 

def print_instruction():
    print "Please use the following cell numbers to make your move"
    show_board([2,3,4,5,6,7,8,9,10],without=True)

def __input__(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line = sys.stdin.readline()
    if line:
        return line[:-1]

def get_input(turn):

    valid = False
    while (not valid):
        try:
            user = input("Where would you like to place " + turn + " (1-9)? ")
            user = int(user)
            if (user >= 1) and (user <= 9):
                return user-1
            else:
                print "That is not a valid move! Please try again.\n"
                print_instruction()
        except Exception as e:
            print user + " is not a valid move! Please try again.\n"

win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))

def check_win(board):
    for each in win_cond:
        try:
            if (board[each[0]-1] == board[each[1]-1]) and (board[each[1]-1] == board[each[2]-1]):
                return board[each[0]-1]
        except:
            pass
    return -1

def quit_game(board,msg):
    show_board(board)
    print msg
    quit()
    
def __make_a_move__(k,v,board,value=0):
    # where can a move be made ?
    import random
    possibles = []
    m = v[0]
    k = eval(k)
    for i in xrange(0,len(m)):
        if (m[i] == -1):
            possibles.append(k[i])
    if (len(possibles) > 0):
        choice = int(random.choice(possibles))
        board[choice-1] = value
        print 'MOVE IS %s for %s' % (choice,'X' if (value) else 'O')
    else:
        #print 'NO MOVES !!!'
        choice = -1
        pass
    return choice
    
def computer_move(board,value=0):
    possible_wins = {}
    opposing = 0 if (value == 1) else 1
    for each in win_cond:
        try:
            if (board[each[0]-1]) or (board[each[1]-1]) or (board[each[2]-1]):
                count_open = 0
                if (board[each[0]-1]==-1):
                    count_open += 1
                if (board[each[1]-1]==-1):
                    count_open += 1
                if (board[each[2]-1]==-1):
                    count_open += 1
                count_opposing = 0
                if (board[each[0]-1]==opposing):
                    count_opposing += 1
                if (board[each[1]-1]==opposing):
                    count_opposing += 1
                if (board[each[2]-1]==opposing):
                    count_opposing += 1
                possible_wins[str(each)] = (board[each[0]-1],board[each[1]-1],board[each[2]-1]),(each[0]==5)or(each[1]==5)or(each[2]==5),(board[each[0]-1]==-1)and(board[each[1]-1]==-1)and(board[each[2]-1]==-1),(board[each[0]-1]==-1)or(board[each[1]-1]==-1)or(board[each[2]-1]==-1),(board[each[0]-1]==1)or(board[each[1]-1]==1)or(board[each[2]-1]==1),count_open,count_opposing
        except:
            pass
    if (board[5-1]==-1):
        board[5-1] = value
        return
    for k,v in possible_wins.iteritems():
        if (v[5] == 1) and (v[6] == 2):
            choice = __make_a_move__(k,v,board,value=value)
            if (choice > -1):
                return
    for k,v in possible_wins.iteritems():
        if (all(v[1:-4])):
            choice = __make_a_move__(k,v,board,value=value)
            if (choice > -1):
                break
        if (v[1]):
            if (v[2]):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    break
            if (v[3]):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    break
            if (v[4]):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    break
        else:
            if (v[4]):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    break
            if (v[3]):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    break
            if (v[2]):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    break
        for k,v in possible_wins.iteritems():
            if (v[5]) and (v[6] == 2):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    return
        for k,v in possible_wins.iteritems():
            if (v[5]) and (v[6] == 0):
                choice = __make_a_move__(k,v,board,value=value)
                if (choice > -1):
                    return
        print

def main():

    # setup game
    # alternate turns
    # check if win or end
    # quit and show the board

    print_instruction()

    prompt = "Automated play ? (computer versus computer) (y/N) ??? "
    resp = raw_input(prompt)
    __automated__ = str(resp).lower() in ['yes','y']

    __is_X__ = False
    if (not __automated__):
        prompt = "Play as 'X' ? (human goes first) (y/N) ??? "
        resp = raw_input(prompt)
        __is_X__ = str(resp).lower() in ['yes','y']

    board = []
    for i in xrange(9):
        board.append(-1)

    win = False
    move = 0
    while not win:

        show_board(board)
        print "Turn number " + str(move+1)
        if (move % 2 == 0):
            turn = 'X'
        else:
            turn = 'O'

        if (turn == 'X'):
            if (not __automated__ and __is_X__):
                user = get_input(turn)
                while (board[user] != -1):
                    print "Invalid move! Cell already taken. Please try again.\n"
                    user = get_input(turn)
                board[user] = 1 if (turn == 'X') else 0
            else:
                computer_move(board,value=1 if (__is_X__) else 0)
        else:
            if (not __automated__ and not __is_X__):
                user = get_input(turn)
                while (board[user] != -1):
                    print "Invalid move! Cell already taken. Please try again.\n"
                    user = get_input(turn)
                board[user] = 0 if (turn == 'X') else 1
            else:
                computer_move(board,value=0)

        move += 1
        if (move > 4):
            winner = check_win(board)
            if (winner != -1):
                out = "The winner is " 
                out += "X" if winner == 1 else "O" 
                out += " :)"
                quit_game(board,out)
            elif (move == 9):
                quit_game(board,"No winner :(")

if (__name__ == "__main__"):
    main()

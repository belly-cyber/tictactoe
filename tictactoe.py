import os
import random

row,col=os.get_terminal_size()
possible_anwers=[{'A', '1'}, {'B', '1'}, {'1', 'C'}, {'A', '2'}, {'2', 'B'}, {'2', 'C'}, {'3', 'A'}, {'3', 'B'}, {'3', 'C'}]

def win_checker(symbol,gb):
    'checks if the symbol(X|O) is found three times in a row if so retuns true'
    winning_combos=[gb['A'],gb['B'],gb['C'],[gb['A'][0],gb['B'][0],gb['C'][0]],[gb['A'][1],gb['B'][1],gb['C'][1]],
        [gb['A'][2],gb['B'][2],gb['C'][2]],[gb['A'][0],gb['B'][1],gb['C'][2]],[gb['A'][2],gb['B'][1],gb['C'][0]]]
    if list(symbol*3) in winning_combos:
        return True
    

def player_generation():
    'generates two players dict'
    dic={}
    for p,x in [('player1','X'),('player2','O')]:
        dic.update({p:{'name':input('enter player {} name:'.format(p)),'symbol':x,'score':0}})
    return dic


def bot(gb,l_choice):
    'play against a bot just type bot in the player name'
    check_dic={}
    for x in range(3):
        check_dic[str(x+1)]=[(v[x],k+str(x+1)) for k,v in game_board.items()]
    check_dic['diag2']=[(t[1][i],str(i+1)+t[0]) for i,t in enumerate(list(game_board.items())[::-1])]
    check_dic['diag1']=[(t[1][i],str(i+1)+t[0]) for i,t in enumerate(game_board.items())]
    choice = ''
    for k,v in gb.items():  ##need to add vertical check!!
        if v.count(' ') ==1: 
            number = v.index(' ')+1
            choice = set(k+str(number))
            break
    for v in check_dic.values():
        marks=[m for m,c in v]
        if marks.count('X') ==2:
            choice = set(v[marks.index(' ')][1])
            print('bot found choice',choice)
            break           
    while  choice == '' or choice in l_choice:
        choice = random.choice(possible_anwers)
    print(choice)
    return choice


def print_board(gb,user_dic):
    'pretty prints the board game in the terminal'
    legend = ' {d[player1][name]}:{d[player1][symbol]} {d[player2][name]}:{d[player2][symbol]} '.format(d=user_dic).center(row,'*')
    scoreboard='{}   {}'.format(*[v['score'] for k,v in user_dic.items()]).center(len(legend),' ').center(row,'*')
    colmns='  1 2 3 '.center(row,' ')
    rows='  -+-+- '.center(row,' ').join(['{} {}|{}|{}'.format(k,*v).center(row,' ') for k,v in gb.items()])
    print('\n'*col)
    print(legend,scoreboard,'',colmns,rows,'*'*row,sep='\n')


def game_start(gb,user_dic):
    logged_choices =[]
    round=True
    while round:
        print_board(gb,user_dic)
        for player,user in user_dic.items():
            if user['name'].lower() == 'bot':
                choice=bot(gb,logged_choices)
            else:
                choice =input('{u[name]}\'s turn. type one letter and one number for symbol placement\n'.format(u=user))
                choice=set(choice.upper())
            while len(choice) != 2 or choice not in possible_anwers or choice in logged_choices:
                choice = set(input('choice one letter and one number\n').upper())
            logged_choices.append(choice)
            choice =sorted(choice)
            gb[choice[1]][int(choice[0])-1]=user['symbol']
            print_board(gb,user_dic)
            if win_checker(user['symbol'],gb):
                print(user['name']+' WON!!!')
                user['score']+=1
                round = False
                break


user_dic=player_generation()
while True:
    game_board ={k:[' ',' ',' '] for k in ('A','B','C')}
    game_start(game_board,user_dic)
    session_choice=input('contuine play? yes or no\n')
    if session_choice.lower() == 'no':
        print('goodbye')
        session = False
        break


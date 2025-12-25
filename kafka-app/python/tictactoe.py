theboard = {'tl':' ', 'tm':' ','tr':' ','ml':' ', 'mm':' ','mr':' ',
'bl':'', 'bm':' ','br':' '}
def printboard(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print("-+-+-")
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['bl'] + '|' + board['bm'] + '|' + board['br'])
turn = 'X'
for i in range(9):
    printboard(theboard)
    print('turn for ' + turn + '. Move on which space?')
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
printboard(theboard)
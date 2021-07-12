#my tic tac toe first try
print("WELCOME TO TIC TAC TOE")
c=[["","",""],["","",""],["","",""]]
print("   0","  1","  2")
for index,rows in enumerate(c):
    print(index,rows)
def tic(rows,cols):
    a=c
    print("   0","  1","  2")
    c[row][cols]="X"
    for index,rows in enumerate(a):
        print(index,rows)
def tac(rows,cols):
    a=c
    print("   0","  1","  2")
    c[row][cols]="O"
    for index,rows in enumerate(a):
        print(index,rows)
for i in range(9):
    if i>=5:
        if ((c[0][0]==c[0][1]==c[0][2] and c[0][0]==c[0][1]==c[0][2]==('X' or 'O'))  or (c[1][0]==c[1][1]==c[1][2]) or c[2][0]==c[2][1]==c[2][2]):
            print("WINNER!!!.....YOU WON BY ROW")
            input()
            break
        elif c[0][0]==c[1][0]==c[2][0] or c[0][1]==c[1][1]==c[2][1] or c[0][2]==c[1][2]==c[2][2]:
            print("WINNER!!!.....YOU WON BY COLUMN")
            input()
            break
        elif c[0][0]==c[1][1]==c[2][2] or c[0][2]==c[1][1]==c[2][0]:
            print("WINNER!!!.....YOU WON BY DIAGONAL")
            input()
            break
    if i%2==0:
        print("Player 1's turn")
        print("Where to put X (Enter only (0 1 and 2) and (0 1 and 2))")
        row,cols=map(int,input("Enter RowNumber and ColumnNumber sperated with space   ").split())
        
        tic(row,cols)
        
    else:
        print("player 2's turn")
        print("Where to put O (Enter only (0 1 and 2) and (0 1 and 2))")
        row,cols=map(int,input("Enter RowNumber and ColumnNumber sperated with space   ").split())
        
        tac(row,cols)
        
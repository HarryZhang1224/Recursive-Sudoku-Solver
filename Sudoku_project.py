#P1
def print_board(board):
    numofrow=len(board)
    valboard=True
    if numofrow!=9:
        valboard=False
        print("Invalid bod=Falseard")
    elif numofrow==9:
       for i in range(numofrow):
           numofcol=len(board[i])
           if numofrow!=numofcol or numofcol!=9:
               print("Invalid board")
               valboard=False
               break
    if valboard==True:
        rowpos=0
        for i in range(len(board)+4):
           nonslash = 0
           colpos=0
           rowprint = ""
           if i%4==0:
               for z in range(25):
                   rowprint+="-"
               print(rowprint)
           else:
               for j in range(25):
                 if j%8==0:
                     rowprint+="|"
                     nonslash=0
                 else:
                     if nonslash%2!=0:
                        if board[rowpos][colpos]==0:
                            rowprint+=" "
                            colpos += 1
                            nonslash += 1
                        else:
                           rowprint+=str(board[rowpos][colpos])
                           colpos+=1
                           nonslash+=1
                     else:
                        rowprint+=" "
                        nonslash+=1
               print(rowprint)
               rowpos+=1


#P2
def find_zero(board):
    rowpos=0
    for row in range(len(board)):
        colpos = 0
        for col in range(len(board[row])):
            if board[row][col]==0:
                return [rowpos,colpos]
            else:
                colpos+=1
        rowpos+=1
    return False


#P3
testboard=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
def is_valid(board, row, col, value):
    validornot=True
    for i in range(len(board[row])):
        if board[row][i]==value:
            validornot=False
            break
    if validornot==False:
        return validornot
    for j in range(len(board)):
        if board[j][col]==value:
            validornot=False
            break
    if validornot==False:
        return validornot
    oldcol=col
    oldrow=row
    runtime1=0
    for z in range(3):
        col=oldcol
        runtime2=0
        for k in range(3):
            if board[row][col]==value:
                validornot=False
                break
            else:
                if oldcol==1 or oldcol==4 or oldcol==7:
                    if runtime2==0:
                        col+=1
                    else:
                        col-=2
                    runtime2+=1
                elif oldcol==0 or oldcol==3 or oldcol==6:
                    col+=1
                    runtime2+=1
                else:
                    col-=1
                    runtime2+=1
        if validornot==False:
            break
        else:
            if oldrow==1 or oldrow==4 or oldrow==7:
               if runtime1==0:
                   row+=1
               else:
                   row-=2
               runtime1+=1
            elif oldrow==0 or oldrow==3 or oldrow==6:
                row+=1
                runtime1+=1
            else:
                row-=1
                runtime1+=1
    return validornot

def solve(board):
    # base case
    if find_zero(board) == False:
        return print_board(board)
    else:
        row=find_zero(board)[0]
        col=find_zero(board)[1]
        # recursive case
        for i in range(1,10):
            if is_valid(board,row,col,i)==True:
                board[row][col]=i
                if solve(board) is not None:
                   return print_board(board)
                else:
                   board[row][col]=0
        return None

import os
import random

board=["-","-","-","-","-","-","-","-","-"]
player="x"


def printboard():
    temp=0
    for i in range(3):
        for j in range(3):
            print(board[temp],end='')
            if j != 2:
                print(" | ", end='')
            temp = temp + 1
        print(" ")

def winner(board):
    if board[0] == board[1] == board[2] == "x":
        return True
    elif board[0] == board[1] == board[2] == "o":
        return True

    if board[3] == board[4] == board[5] == "x":
        return True
    elif board[3] == board[4] == board[5] == "o":
        return True

    if board[6] == board[7] == board[8] == "x":
        return True
    elif board[6] == board[7] == board[8] == "o":
        return True

    if board[0] == board[3] == board[6] == "x":
        return True
    elif board[0] == board[3] == board[6] == "o":
        return True

    if board[1] == board[4] == board[7] == "x":
        return True
    elif board[1] == board[4] == board[7] == "o":
        return True

    if board[2] == board[5] == board[8] == "x":
        return True
    elif board[2] == board[5] == board[8] == "o":
        return True

    if board[0] == board[4] == board[8]  == "x":
        return True
    elif board[0] == board[4] == board[8] == "o":
        return True

    if board[2] == board[4] == board[6] == "x":
        return True
    elif board[2] == board[4] == board[6] == "o":
        return True
    
    return False

def tie():
    for i in board:
        if i == "-":  
            return True

    return False

def random_move(player):
    flg1=False
    while(flg1==False):
        n = random.randint(0,8)
        if (board[n]=="-"):
            player="x"
            board[n]="o"
            flg1 = True
            return player

def first_move(player):
    
    if (board[4]=="-"):
            player="x"
            board[4]="o"
            flg1 = True
            return player
    player = random_move(player)
    return player


def bot(player,count):
    if count==0:
        player = first_move(player)
        count=count+1
        return player,count
    
    count=count+1
    for i in range(0,9):
        copy = board
        if copy[i]=="-":
            copy[i]="o"
            if winner(copy):
                board[i] = "o"
                player="x"
                return player,count
            copy[i]="-"
    
    for i in range(0,9):
        copy = board
        if copy[i]=="-":
            copy[i]="x"
            if winner(copy):
                board[i] = "o"
                player="x"
                return player,count
            copy[i]="-"
    
    


count=0
flg = False
while(tie()):
    os.system("cls")
    printboard()
    print(count)
    if player == "o" and (winner(board) == False):
        player,count = bot(player,count)
    elif player == "x" and (winner(board) == False):
        choice = int(input(f"Player {player}'s turn : "))
        if (board[choice-1]=="-"):
            player = "o"
            board[choice-1] = "x"

    if winner(board):
        printboard()
        if player=="x":
            print("Computer won!")
        if player=="o":
            print("You won!")
        flg = True
        break



if flg == False:
    os.system("cls")
    printboard()
    print("It's a Tie!")
        
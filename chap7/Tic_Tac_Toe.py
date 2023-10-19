import random

Turn = True
Uwin_Cnt = 0
Rwin_Cnt = 0
Winner = ""
AiNum = 0

def Print():
    print("\n\tWelcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.")
    print("\tThis will be a showdown between your human brain and my silicon processor.\n\n")
    print("\tYou will make your move known by entering a number, 0 - 8.")
    print("\tThe number will correspond to the board position as illustrated:")
    print("\t\t\t\t0 | 1 | 2")
    print("\t\t\t\t---------")
    print("\t\t\t\t3 | 4 | 5")
    print("\t\t\t\t---------")
    print("\t\t\t\t6 | 7 | 8")
    print("\n\tPrepare yourself, human. The ultimate battle is about to begin.\n\n")

def Ingame(Choice):
    global Turn
    global Winner
    global AiNum
    if Choice == "n":
        Turn = False #Turn -> False라면 AI먼저
    while True:
        if Turn == True:
            #유저가 놓는거
            MovNum = int(input("Where will you move? <0 - 8>:"))
            print("Fine..\n")
            Set_OX(MovNum,Turn)
            Turn = False
        elif Turn == False:
            #AI가 놓는 함수 입력
            while True:
                AiNum = random.randrange(0,9)
                if(Board[AiNum] == ""): break
            print("I shall take square number",AiNum,"\n")
            Set_OX(AiNum,Turn) #우선 랜덤
            Turn = True
        Print_Board()
        Winner = Who_Win()
        if Winner == None:
            continue
        elif Winner == "O Won":
            print(Winner)
            break
        elif Winner == "X Won":
            print(Winner)
            break

def Print_Board():
    print("\t\t",end='')
    for i in range(0,9):
        if Board[i] == "":
            print(" ", end = '')
        else :
            print(Board[i],end='')
        if i == 0 or i == 1 or i == 3 or i == 4 or i == 6 or i == 7:
            print(" | ",end ='')
        else:
           print("\n\t\t",end='')
           if i == 8 :
            break
           print("---------",end='')
           print("\n\t\t",end='')
    print("\n")

def Ai_Set():
    print("AI")

#Usr = O AI = X
#만약 놓은 곳에 놓음 턴이 넘어감
def Set_OX(num, bool):
    if bool == True:
        Board[num] = "O"
    elif bool == False:
        Board[num] = "X"

def Who_Win():
    global Uwin_Cnt
    global Rwin_Cnt
    c = 0
    while True:
        for i in range(c,9,3):
            if Board[i] == "O":
                Uwin_Cnt += 1
            elif Board[i] == "X":
                Rwin_Cnt += 1
        if c == 3 : break
        c += 1
        if Uwin_Cnt == 3:
            return "O Won"
        elif Rwin_Cnt == 3:
            return "X Won"
        Uwin_Cnt = 0
        Rwin_Cnt = 0
    Uwin_Cnt = 0
    Rwin_Cnt = 0
    for i in range(0,3):
        if Board[i] == "O":
            Uwin_Cnt += 1
        elif Board[i] == "X":
            Rwin_Cnt += 1
    if Uwin_Cnt == 3:
        return "O Won"
    elif Rwin_Cnt == 3:
        return "X Won"
    Uwin_Cnt = 0
    Rwin_Cnt = 0
    for i in range(3,6):
        if Board[i] == "O":
            Uwin_Cnt += 1
        elif Board[i] == "X":
            Rwin_Cnt += 1
    if Uwin_Cnt == 3:
        return "O Won"
    elif Rwin_Cnt == 3:
        return "X Won"
    Uwin_Cnt = 0
    Rwin_Cnt = 0
    for i in range(6,9):
        if Board[i] == "O":
            Uwin_Cnt += 1
        elif Board[i] == "X":
            Rwin_Cnt += 1
    if Uwin_Cnt == 3:
        return "O Won"
    elif Rwin_Cnt == 3:
        return "X Won"
    Uwin_Cnt = 0
    Rwin_Cnt = 0
    #대각선 승자
    if Board[4] == "O":
        if (Board[0] == "O" and Board[8] == "O") or (Board[2] == "O" and Board[6] == "O"):
            return "O Won"
    elif Board[4] == "X":
        if (Board[0] == "X" and Board[8] == "X") or (Board[2] == "X" and Board[6] == "X"):
            return "X Won"


Board = ["","","","","","","","",""]
Print()
while True:
    Select = input("Do you require the first move? (y/n): ")
    if(Select == 'y' or Select == 'n'): break
    else : print("<<잘못된 입력 재입력>>")
print("\n\n\n")
Ingame(Select)
print("\n")
if Winner == "X Won":
    print("As I predicted, human, I am triumphant once more.")
    print("Proof that computer are superior to human in all regards")
if Winner == "O Won":
    print("No, no! It cannot be! somehow you tricked me, human.")
    print("But never again! I, the computer, so swears it!")
print("\n\nPress the enter key to quit.")
#다시하기 기능 만들기

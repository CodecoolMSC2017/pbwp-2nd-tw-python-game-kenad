import os
import time
import sys
import random
os.system("clear")


def getchar():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

class Board():
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
        self.loading = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        self.playerScore = [0,0]
        self.playerScoreName = ["Player 1","Player 2"]
        self.playerLeaderBoard1p = [[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "]]
        self.playerLeaderBoard2p = [[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "]]

    def loadingScreen(self):
        print(" "*size1,"╔═══════════════════════════════════════════════════════════╗")
        print(" "*size1,"║        _____ _     _____          _____                   ║")
        print(" "*size1,"║       /__  /(_) __/__   \__ _  __/__   \___   ___         ║")
        print(" "*size1,"║         / /\/ |/ __|/ /\/ _` |/ __|/ /\/ _ \ / _ |        ║")
        print(" "*size1,"║        / /  | | (__/ / | (_| | (__/ / | (_) |  __/        ║")
        print(" "*size1,"║        \/   |_|\___\/   \__,_|\___\/   \___/ \___|        ║")
        print(" "*size1,"║                                                           ║")
        print(" "*size1,"║                        Loading...                         ║")
        print(" "*size1,"║                  [%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s]                   ║" % (self.loading[0], 
        self.loading[1], self.loading[2], self.loading[3], self.loading[4], self.loading[5], 
        self.loading[6], self.loading[7], self.loading[8], self.loading[9], self.loading[10], 
        self.loading[11], self.loading[12], self.loading[13], self.loading[14], self.loading[15], 
        self.loading[16], self.loading[17], self.loading[18], self.loading[19]))
        print(" "*size1,"╚═══════════════════════════════════════════════════════════╝")

    def display(self):
        print(" "*size,"║                   ║ ║             ╔═════════╦═════════╦═════════╗               ║")
        print(" "*size,"║  1. Csanád  -  16 ║ ║             ║         ║         ║         ║               ║ ╔══════════════════════════════════╗")
        print(" "*size,"║  2. Kenéz   -  14 ║ ║             ║    %s    ║    %s    ║    %s    ║               ║" % (self.cells[1], self.cells[2], self.cells[3]),"║                                  ║")
        print(" "*size,"║  3. Józsi   -  13 ║ ║             ║         ║         ║         ║               ║ ║         ---SCOREBOARD---         ║")
        print(" "*size,"║  4. Krisz   -  10 ║ ║             ╠═════════╬═════════╬═════════╣               ║ ║                                  ║")
        print(" "*size,"║  5. Gábor   -  9  ║ ║             ║         ║         ║         ║               ║ ║ ╔════════════╗    ╔════════════╗ ║")
        print(" "*size,"║  6. Viktor  -  7  ║ ║             ║    %s    ║    %s    ║    %s    ║               ║" % (self.cells[4], self.cells[5], self.cells[6]),"║ ║  %8s  ║    ║  %8s  ║ ║" % (self.playerScoreName[0], self.playerScoreName[1]))
        print(" "*size,"║  7. Robi    -  4  ║ ║             ║         ║         ║         ║               ║ ║ ╚══╗      ╔══╝    ╚══╗      ╔══╝ ║")
        print(" "*size,"║  8. Feri    -  3  ║ ║             ╠═════════╬═════════╬═════════╣               ║ ║    ║  %02d  ║          ║  %02d  ║    ║" % (self.playerScore[0], self.playerScore[1]))
        print(" "*size,"║  9. Imre    -  2  ║ ║             ║         ║         ║         ║               ║ ║    ╚══════╝          ╚══════╝    ║")
        print(" "*size,"║ 10. Józsi   -  1  ║ ║             ║    %s    ║    %s    ║    %s    ║               ║" % (self.cells[7], self.cells[8], self.cells[9]),"║                                  ║")
        print(" "*size,"║                   ║ ║             ║         ║         ║         ║               ║ ╚══════════════════════════════════╝")
        print(" "*size,"╚═══════════════════╝ ║             ╚═════════╩═════════╩═════════╝               ║")
        print(" "*size,"                      ╚═══════════════════════════════════════════════════════════╝")

    def updateLoad(self, cell_no1, marker):
        for i in self.loading:
            if cell_no1==18:
                time.sleep(2)
            if cell_no1==19:
                time.sleep(3)
            self.loading[cell_no1] = marker
            refreshLoad()
            time.sleep(0.1)
            cell_no1 += 1

    def update_cell(self, cell_no, player):
        self.cells[cell_no] = player

    def isWinner(self, player):
        if (self.cells[1] == player and self.cells[2]
                == player and self.cells[3] == player):
            return True
        if (self.cells[4] == player and self.cells[5]
                == player and self.cells[6] == player):
            return True
        if (self.cells[7] == player and self.cells[8]
                == player and self.cells[9] == player):
            return True
        if (self.cells[1] == player and self.cells[4]
                == player and self.cells[7] == player):
            return True
        if (self.cells[2] == player and self.cells[5]
                == player and self.cells[8] == player):
            return True
        if (self.cells[3] == player and self.cells[6]
                == player and self.cells[9] == player):
            return True
        if (self.cells[1] == player and self.cells[5]
                == player and self.cells[9] == player):
            return True
        if (self.cells[3] == player and self.cells[5]
                == player and self.cells[7] == player):
            return True
        return False

    def isTie(self):
        used_cells = 0
        for cell in self.cells:
            if (cell != " "):
                used_cells += 1
        if (used_cells == 9):
            return True
        else:
            return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def exitGame(self):
        refreshScreen()
        print("\n\n\n\n\n\n\n\n\nExiting game...")
        time.sleep(2)
        refreshScreen()
        print("\n\n\n\n\n\n\n\n\nThank you for playing!")
        time.sleep(2)
        refreshScreen()
        os.system("clear")
        quit()

    '''def playerLeaderBoard1(self, name, score):
        scores = []
        for line in leaderboard1plines:
            name, score = line.split(',')
            scores.append((name, score))
            score = int(score)
        print(scores)
        time.sleep(2)   
        file = open("leaderboard1p.txt", "w")
        file.write(name+",")
        file.write(score+"\n")
        file.close()
        with open("leaderboard1p.txt", "w") as f:
            s = f.write(name+","+score+"\n")
        for line in leaderboard1plines:
            name, score = line.split(',')
        
        #scores.sort(key=lambda s: s[1], reverse=True)

        
        k = 1
        for name, score in scores:
            s = '{:{align}{width}}'.format(k, align='>', width='2')
            s += '{:{align}{width}}'.format('.', align='<', width='1')    
            s += '{:{align}{width}}'.format(name, align='<', width='8')
            s += '{:{align}{width}}'.format(' - ', align='^', width='3')
            s += '{:{align}{width}}'.format(score, align='>', width='4')
            k += 1
            scores.append(s)
        
        self.playerLeaderBoard1p = scores 
        '''

    def aiMode(self):
        p1 = input("\n\n\n\n\n\n\n\n\nEnter player name > ")
        if (p1 == "" or " " in p1 or len(p1) > 8):
            p1 = "Player 1"
            self.playerScoreName[0] = p1
        else:
            #for i in range(0,len(leaderboard1plines)):
            #    if p1 not in leaderboard1plines:
            #        self.playerLeaderBoard1(p1, self.playerScore[0])


            #for i in range(0,len(leaderboard1plines)):
            #    if p1 in leaderboard1plines[i]:
            #        file = open("leaderboard1p.txt", "w")
            #        nevek = leaderboard1plines[i].split(',')
            #        p1 = nevek[0]
            #        nevek[1] = int(nevek[1])
            #        self.playerScore[0] = nevek[1]
            #        self.playerScore=[board.playerLeaderBoard1p[i][1],0]
            player1 = '{:{align}{width}}'.format(p1, align='^', width='8')
            self.playerScoreName[0] = player1
            
            

                
        board.playerScoreName[1] = "PC   "
        refreshScreen()
        while True:
            refreshScreen()
            while True:
                refreshScreen()
                sys.stdout.write("\n\n\n\n\n\n\n\n\n%s, Please choose 1-9 > " % (p1))
                x_choice = getchar()
                if x_choice.isdigit():
                    x_choice = int(x_choice)
                    if x_choice != 0 and board.cells[x_choice] == " ":
                        break
                    elif x_choice == 0:
                        print("\nInvalid spot selected.")
                        time.sleep(1)
                        refreshScreen()
                    else:
                        print("\nSpot already taken.")
                        time.sleep(1)
                        refreshScreen()
                elif x_choice != "q":
                    print("\nInvalid input.")
                    time.sleep(1)
                    refreshScreen()
                    continue
                elif x_choice == "q":
                    board.reset()
                    refreshScreen()
                    menuSystem()
            board.update_cell(x_choice, "X")
            refreshScreen()
            if board.isWinner("X"):
                board.playerScore[0] += 1
                currentScore = str(board.playerScore[0])
                loadList(p1, board.playerScore[0])
                file = open("leaderboard1p.txt", "a")
                file.write(p1+","+currentScore)
                file.close()
                refreshScreen()
                print("\n\n\n\n\n\n\n\n\n%s wins!" % (p1))
                xwin = ("\n\n\n\n\n\n\n\n\n%s wins!" % (p1))
                wouldYouLikeToPlayAgain(xwin)

            if board.isTie():
                print("\n\n\n\n\n\n\n\n\nTie game!")
                tie = ("\n\n\n\n\n\n\n\n\nTie game!")
                wouldYouLikeToPlayAgain(tie)

            refreshScreen()
            for i in range(2):
                pcLoading()
            board.aiMoves("O")
            
            if board.isWinner("O"):
                board.playerScore[1] += 1
                refreshScreen()
                print("\n\n\n\n\n\n\n\n\nPC wins!")
                pcwin = ("\n\n\n\n\n\n\n\n\nPC wins!")
                wouldYouLikeToPlayAgain(pcwin)

            if board.isTie():
                print("\n\n\n\n\n\n\n\n\nTie game!")
                tie = ("\n\n\n\n\n\n\n\n\nTie game!")
                wouldYouLikeToPlayAgain(tie)

    def aiMoves(self, player):
        if player == "X":
            enemy = "O"

        if player == "O":
            enemy = "X"

        # TakeCenter
        if self.cells[5] == " ":
            self.update_cell(5, player)

        # tryToWin
        elif (self.cells[2] == player and self.cells[3] == player and self.cells[1] == " " or self.cells[4] == player and self.cells[7] == player and self.cells[1] == " " or self.cells[5] == player and self.cells[9] == player and self.cells[1] == " "):
            self.update_cell(1, player)

        elif (self.cells[1] == player and self.cells[3] == player and self.cells[2] == " " or self.cells[5] == player and self.cells[8] == player and self.cells[2] == " "):
            self.update_cell(2, player)

        elif (self.cells[1] == player and self.cells[2] == player and self.cells[3] == " " or self.cells[6] == player and self.cells[9] == player and self.cells[3] == " " or self.cells[5] == player and self.cells[7] == player and self.cells[3] == " "):
            self.update_cell(3, player)

        elif (self.cells[5] == player and self.cells[6] == player and self.cells[4] == " " or self.cells[1] == player and self.cells[7] == player and self.cells[4] == " "):
            self.update_cell(4, player)

        elif (self.cells[4] == player and self.cells[6] == player and self.cells[5] == " " or self.cells[2] == player and self.cells[8] == player and self.cells[5] == " " or self.cells[1] == player and self.cells[9] == player and self.cells[5] == " " or self.cells[3] and self.cells[7] == player and self.cells[5] == " "):
            self.update_cell(5, player)

        elif (self.cells[4] == player and self.cells[5] == player and self.cells[6] == " " or self.cells[3] == player and self.cells[9] == player and self.cells[6] == " "):
            self.update_cell(6, player)

        elif (self.cells[8] == player and self.cells[9] == player and self.cells[7] == " " or self.cells[1] == player and self.cells[4] == player and self.cells[7] == " " or self.cells[3] == player and self.cells[5] == player and self.cells[7] == " "):
            self.update_cell(7, player)

        elif (self.cells[7] == player and self.cells[9] == player and self.cells[8] == " " or self.cells[2] == player and self.cells[5] == player and self.cells[8] == " "):
            self.update_cell(8, player)

        elif (self.cells[7] == player and self.cells[8] == player and self.cells[9] == " " or self.cells[3] == player and self.cells[6] == player and self.cells[9] == " " or self.cells[1] == player and self.cells[5] == player and self.cells[9] == " "):
            self.update_cell(9, player)

        # TryBlock
        elif (self.cells[2] == enemy and self.cells[3] == enemy and self.cells[1] == " " or self.cells[4] == enemy and self.cells[7] == enemy and self.cells[1] == " " or self.cells[5] == enemy and self.cells[9] == enemy and self.cells[1] == " "):
            self.update_cell(1, player)

        elif (self.cells[1] == enemy and self.cells[3] == enemy and self.cells[2] == " " or self.cells[5] == enemy and self.cells[8] == enemy and self.cells[2] == " "):
            self.update_cell(2, player)

        elif (self.cells[1] == enemy and self.cells[2] == enemy and self.cells[3] == " " or self.cells[6] == enemy and self.cells[9] == enemy and self.cells[3] == " " or self.cells[5] == enemy and self.cells[7] == enemy and self.cells[3] == " "):
            self.update_cell(3, player)

        elif (self.cells[5] == enemy and self.cells[6] == enemy and self.cells[4] == " " or self.cells[1] == enemy and self.cells[7] == enemy and self.cells[4] == " "):
            self.update_cell(4, player)

        elif (self.cells[4] == enemy and self.cells[6] == enemy and self.cells[5] == " " or self.cells[2] == enemy and self.cells[8] == enemy and self.cells[5] == " " or self.cells[1] == enemy and self.cells[9] == enemy and self.cells[5] == " " or self.cells[3] and self.cells[7] == enemy and self.cells[5] == " "):
            self.update_cell(5, player)

        elif (self.cells[4] == enemy and self.cells[5] == enemy and self.cells[6] == " " or self.cells[3] == enemy and self.cells[9] == enemy and self.cells[6] == " "):
            self.update_cell(6, player)

        elif (self.cells[8] == enemy and self.cells[9] == enemy and self.cells[7] == " " or self.cells[1] == enemy and self.cells[4] == enemy and self.cells[7] == " " or self.cells[3] == enemy and self.cells[5] == enemy and self.cells[7] == " "):
            self.update_cell(7, player)

        elif (self.cells[7] == enemy and self.cells[9] == enemy and self.cells[8] == " " or self.cells[2] == enemy and self.cells[5] == enemy and self.cells[8] == " "):
            self.update_cell(8, player)

        elif (self.cells[7] == enemy and self.cells[8] == enemy and self.cells[9] == " " or self.cells[3] == enemy and self.cells[6] == enemy and self.cells[9] == " " or self.cells[1] == enemy and self.cells[5] == enemy and self.cells[9] == " "):
            self.update_cell(9, player)

        # NoBlockNoWin
        else:
            for i in range(1,10):
                if self.cells[i] == " ":
                    self.update_cell(i, player)
                    break

        refreshScreen()

board = Board()

def wouldYouLikeToPlayAgain(condition):
    print("Would you like to play again? (Y/N) > ")
    playAgain = getchar().upper()
    if (playAgain == "Y"):
        board.reset()
        refreshScreen()
    elif (playAgain == "N" or playAgain == "Q"):
        board.playerScoreName[0] = "Player 1"
        board.playerScoreName[1] = "Player 2"
        #board.playerScore[0] = 0
        board.playerScore[1] = 0
        board.reset()
        refreshScreen()
        menuSystem()
    else:
        print("Invalid input")
        time.sleep(1)
        refreshScreen()
    while True:
        refreshScreen()
        print(condition)
        print("Would you like to play again? (Y/N) > ")
        playAgain = getchar().upper()
        if (playAgain == "Y"):
            board.reset()
            refreshScreen()
            break
        elif (playAgain == "N" or playAgain == "Q"):
            board.playerScoreName[0] = "Player 1"
            board.playerScoreName[1] = "Player 2"
            board.playerScore[0] = 0
            board.playerScore[1] = 0
            board.reset()
            refreshScreen()
            menuSystem()
        else:
            print("Invalid input")
            time.sleep(1)
            refreshScreen()
            continue

def printHeader():
    print(" "*size1,"╔═══════════════════════════════════════════════════════════╗")
    print(" "*size1,"║        _____ _     _____          _____                   ║")
    print(" "*size1,"║       /__  /(_) __/__   \__ _  __/__   \___   ___         ║")
    print(" "*size1,"║         / /\/ |/ __|/ /\/ _` |/ __|/ /\/ _ \ / _ |        ║")
    print(" "*size1,"║        / /  | | (__/ / | (_| | (__/ / | (_) |  __/        ║")
    print(" "*size1,"║        \/   |_|\___\/   \__,_|\___\/   \___/ \___|        ║")
    print(" "*size1,"║                                                           ║")
    print(" "*size,"╔═══════════════════╗ ║                  To exit, press Q anytime.                ║")
    print(" "*size,"║                   ║ ║                                                           ║")
    print(" "*size,"║ ---LEADERBOARD--- ║ ║                                                           ║")

def refreshScreen():
    os.system("clear")
    printHeader()
    board.display()

def refreshLoad():
    os.system("clear")
    board.loadingScreen()

def pvpMode():
    p1 = input("\n\n\n\n\n\n\n\n\nEnter name of player 1 > ")
    if (p1 == "" or " " in p1 or len(p1) > 8):
        p1 = "Player 1"
        board.playerScoreName[0] = p1
    else:
        player1 = '{:{align}{width}}'.format(p1, align='^', width='8')
        board.playerScoreName[0] = player1
    refreshScreen()
    p2 = input("\n\n\n\n\n\n\n\n\nEnter name of player 2 > ")
    if (p2 == "" or " " in p2 or len(p2) > 8):
        p2 = "Player 2"
        board.playerScoreName[1] = p2
    else:
        player2 = '{:{align}{width}}'.format(p2, align='^', width='8')
        board.playerScoreName[1] = player2
    refreshScreen()
    while True:
        refreshScreen()
        while True:
            refreshScreen()
            sys.stdout.write("\n\n\n\n\n\n\n\n\n%s, Please choose 1-9 > " % (p1))
            x_choice = getchar()
            if x_choice.isdigit():
                x_choice = int(x_choice)
                if x_choice != 0 and board.cells[x_choice] == " ":
                    break
                elif x_choice == 0:
                    print("\n\n\n\n\n\n\n\n\n\nInvalid spot selected.")
                    time.sleep(1)
                    refreshScreen()
                else:
                    print("\n\n\n\n\n\n\n\n\n\nSpot already taken.")
                    time.sleep(1)
                    refreshScreen()
            elif x_choice != "q":
                print("\nInvalid input.")
                time.sleep(1)
                refreshScreen()
                continue
            elif x_choice == "q":
                menuSystem()
                
        board.update_cell(x_choice, "X")
        refreshScreen()
        if board.isWinner("X"):
            board.playerScore[0] += 1
            refreshScreen()
            print("\n\n\n\n\n\n\n\n\n%s wins!" % (p1))
            xwin = ("\n\n\n\n\n\n\n\n\n%s wins!" %(p1))
            wouldYouLikeToPlayAgain(xwin)

        if board.isTie():
            print("\n\n\n\n\n\n\n\n\nTie game!")
            tie = ("\n\n\n\n\n\n\n\n\nTie game!")
            wouldYouLikeToPlayAgain(tie)

        refreshScreen()
        while True:
            refreshScreen()
            sys.stdout.write("\n\n\n\n\n\n\n\n\n%s, Please choose 1-9 > " % (p2))
            o_choice = getchar()
            if o_choice.isdigit():
                o_choice = int(o_choice)
                if o_choice != 0 and board.cells[o_choice] == " ":
                    break
                elif o_choice == 0:
                    print("\n\n\n\n\n\n\n\n\n\nInvalid spot selected.")
                    time.sleep(1)
                    refreshScreen()
                else:
                    print("\n\n\n\n\n\n\n\n\n\nSpot already taken.")
                    time.sleep(1)
                    refreshScreen()
            elif o_choice != "q":
                print("\n\n\n\n\n\n\n\n\n\nInvalid input.")
                time.sleep(1)
                refreshScreen()
                continue
            elif o_choice == "q":
                menuSystem()

        board.update_cell(o_choice, "O")
        refreshScreen()
        if board.isWinner("O"):
            board.playerScore[1] += 1
            refreshScreen()
            print("\n\n\n\n\n\n\n\n%s wins!" % (p2))
            owin = ("\n\n\n\n\n\n\n\n\n%s wins!" %(p2))
            wouldYouLikeToPlayAgain(owin)

        if board.isTie():
            print("\n\n\n\n\n\n\n\nTie game!")
            tie = ("\n\n\n\n\n\n\n\n\nTie game!")
            wouldYouLikeToPlayAgain(tie)

def pcLoading():
    refreshScreen()
    print("\n\n\n\n\n\n\n\n\nPC's turn > |")
    time.sleep(0.2)
    refreshScreen()
    print("\n\n\n\n\n\n\n\n\nPC's turn > / ")
    time.sleep(0.2)
    refreshScreen()
    print("\n\n\n\n\n\n\n\n\nPC's turn > ─ ")
    time.sleep(0.2)
    refreshScreen()
    print("\n\n\n\n\n\n\n\n\nPC's turn > \ ")
    time.sleep(0.2)
    refreshScreen()

def menuSystem():
    refreshScreen()
    while True:
        refreshScreen()
        print("\n"," "*size2,"> Main Menu <")
        print("\n"," "*size3,"Start game: [S]")
        print("\n"," "*size3,"Help:       [H]")
        print("\n"," "*size3,"Exit:       [Q]")
        print("\nChoose a menupoint > ", end="")
        menuChoice = getchar()
        if menuChoice == "s":
            refreshScreen()
            gameStart()
            break
        elif menuChoice == "h":
            gameHelp()
            menuSystem()
        elif menuChoice == "q":
            board.exitGame()
        else:
            print("\nInvalid menupoint selected")
            time.sleep(1)
            refreshScreen()
            continue

def gameHelp():
    print("")
    print("╔═╦═╦═╗  > Tic-Tac-Toe is a turn based game where a player's marker is X and the other one's is O.")
    print("║1║2║3║  > In order to win, connect 3 of your markers vertically, horizontally, or diagonally.")
    print("╠═╬═╬═╣  > If a player wins, the next round will start with the other player.")
    print("║4║5║6║  > If a game ends in a tie, the player who was second in that round, goes first in the next one.")
    print("╠═╬═╬═╣  > Your name must be less than 8 characters long, can't contain spaces, be nothing")
    print("║7║8║9║    or else you will play as 'Player 1' or 'Player 2', and your score will not be tracked on the leaderboard.")
    print("╚═╩═╩═╝  > You can select the spot where you want to place your marker with the number keys on your keyboard,")
    print("           the illustration on the left shows which number corresponds to which spot.")
    print("> You can press Q anytime if you would like to exit to the main menu, where you can quit the game by pressing Q again.")
    print("> Try to beat your opponent as many times as you can, so you can get to the top of the leaderboard!")
    print("> Have fun playing the game! :)")
    getchar()

def gameStart():
    while True:
        refreshScreen()
        print("\n"," "*size2+"> Game Mode <")
        print("\n"," "*size2+"1 Player: [1]")
        print("\n"," "*size2+"2 Player: [2]")
        print("\n\n\nChoose gamemode > ", end="")
        gameMode = getchar()
        if gameMode == "q":
            menuSystem()
        elif gameMode == "1":
            refreshScreen()
            print("\n\n\n\n\n\n\n\n\nYou have selected 1 player mode!", end="")
            time.sleep(2)
            refreshScreen()
            board.aiMode()
            break
        elif gameMode == "2":
            refreshScreen()
            print("\n\n\n\n\n\n\n\n\nYou have selected 2 player mode!", end="")
            time.sleep(2)
            refreshScreen()
            pvpMode()
            break
        else:
            print("\nInvalid gamemode selected")
            time.sleep(1)
            refreshScreen()

def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return w

'''def loadList(playername, boardplayerscore):
    for i in range(0,len(leaderboard1plines)):
        playername = leaderboard1plines[i]
        result = playername.split(',')
        board.playerLeaderBoard1p[i][0] = result[0]
        board.playerLeaderBoard1p[i][1] = boardplayerscore
    return board.playerLeaderBoard1p'''

#leaderboard1plines = " "

#try:
#    file = open("leaderboard1p.txt","r")
#    leaderboard1plines = file.readlines()
#    file.close()

#except ValueError as ex:
#    print(ex)
#    quit()
#file = open("leaderboard1p.txt","w")
#file.close()"""

#try:
#    file = open("leaderboard2p.txt","r")
#    file.close()
#except:
#    file = open("leaderboard2p.txt","w")
#    file.close()

terminal_size()
size = int((terminal_size() - 120) / 2)
size1 = int(terminal_size() - 123)
size2 = int(terminal_size() - 97)
size3 = int(terminal_size() - 98)
refreshLoad()
board.updateLoad(0, "∎")
refreshScreen()
menuSystem()
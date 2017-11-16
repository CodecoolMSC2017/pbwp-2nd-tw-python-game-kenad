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

    def loadingScreen(self):
        print(" "*size,"╔═══════════════════════════════════════════════════════════╗")
        print(" "*size,"║         _____ _     _____          _____                  ║")
        print(" "*size,"║        /__  /(_) __/__   \__ _  __/__   \___   ___        ║")
        print(" "*size,"║          / /\/ |/ __|/ /\/ _` |/ __|/ /\/ _ \ / _ |       ║")
        print(" "*size,"║         / /  | | (__/ / | (_| | (__/ / | (_) |  __/       ║")
        print(" "*size,"║         \/   |_|\___\/   \__,_|\___\/   \___/ \___|       ║")
        print(" "*size,"║                                                           ║")
        print(" "*size,"║                         Loading...                        ║")
        print(" "*size,"║                   [%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s]                  ║" % (self.loading[0], 
        self.loading[1], self.loading[2], self.loading[3], self.loading[4], self.loading[5], 
        self.loading[6], self.loading[7], self.loading[8], self.loading[9], self.loading[10], 
        self.loading[11], self.loading[12], self.loading[13], self.loading[14], self.loading[15], 
        self.loading[16], self.loading[17], self.loading[18], self.loading[19]))
        print(" "*size,"╚═══════════════════════════════════════════════════════════╝")

    def display(self):
        print(" "*size,"║             ╔═════════╦═════════╦═════════╗               ║")
        print(" "*size,"║             ║         ║         ║         ║               ║ ╔══════════════════════════════════╗")
        print(" "*size,"║             ║    %s    ║    %s    ║    %s    ║               ║" % (self.cells[1], self.cells[2], self.cells[3]),"║                                  ║")
        print(" "*size,"║             ║         ║         ║         ║               ║ ║          --SCOREBOARD--          ║")
        print(" "*size,"║             ╠═════════╬═════════╬═════════╣               ║ ║                                  ║")
        print(" "*size,"║             ║         ║         ║         ║               ║ ║ ╔════════════╗    ╔════════════╗ ║")
        print(" "*size,"║             ║    %s    ║    %s    ║    %s    ║               ║" % (self.cells[4], self.cells[5], self.cells[6]),"║ ║  %8s  ║    ║  %8s  ║ ║" % (self.playerScoreName[0], self.playerScoreName[1]))
        print(" "*size,"║             ║         ║         ║         ║               ║ ║ ╚══╗      ╔══╝    ╚══╗      ╔══╝ ║")
        print(" "*size,"║             ╠═════════╬═════════╬═════════╣               ║ ║    ║  %02d  ║          ║  %02d  ║    ║" % (self.playerScore[0], self.playerScore[1]))
        print(" "*size,"║             ║         ║         ║         ║               ║ ║    ╚══════╝          ╚══════╝    ║")
        print(" "*size,"║             ║    %s    ║    %s    ║    %s    ║               ║" % (self.cells[7], self.cells[8], self.cells[9]),"║                                  ║")
        print(" "*size,"║             ║         ║         ║         ║               ║ ╚══════════════════════════════════╝")
        print(" "*size,"║             ╚═════════╩═════════╩═════════╝               ║")
        print(" "*size,"╚═══════════════════════════════════════════════════════════╝")

    def updateLoad(self, cell_no1, marker):
        for i in self.loading:
            if cell_no1==17:
                time.sleep(2)
            if cell_no1==18:
                time.sleep(3)
            if cell_no1==19:
                time.sleep(5)
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
        print("\nExiting game...")
        time.sleep(2)
        refreshScreen()
        print("\nThank you for playing!")
        time.sleep(2)
        refreshScreen()
        os.system("clear")
        quit()

    def aiMode(self):
        p1 = input("\nEnter player name > ")
        if (p1 == "" or " " in p1 or len(p1) > 8):
            p1 = "Player 1"
            board.playerScoreName[0] = p1
        elif (p1 == "" or " " in p1 or len(p1) == 7):
            board.playerScoreName[0] = p1+" "
        elif (p1 == "" or " " in p1 or len(p1) == 6):
            board.playerScoreName[0] = p1+" "
        elif (p1 == "" or " " in p1 or len(p1) == 5):
            board.playerScoreName[0] = p1+"  "
        elif (p1 == "" or " " in p1 or len(p1) == 4):
            board.playerScoreName[0] = p1+"  "
        elif (p1 == "" or " " in p1 or len(p1) == 3):
            board.playerScoreName[0] = p1+"   "
        elif (p1 == "" or " " in p1 or len(p1) == 2):
            board.playerScoreName[0] = p1+"   "
        elif (p1 == "" or " " in p1 or len(p1) == 1):
            board.playerScoreName[0] = p1+"    "
        board.playerScoreName[1] = "PC   "
        refreshScreen()
        while True:
            refreshScreen()
            while True:
                refreshScreen()
                sys.stdout.write("\n%s, Please choose 1-9 > " % (p1))
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
                    menuSystem()
            board.update_cell(x_choice, "X")
            refreshScreen()
            if board.isWinner("X"):
                board.playerScore[0] += 1
                refreshScreen()
                print("\n%s wins!" % (p1))
                wouldYouLikeToPlayAgain()

            if board.isTie():
                print("\nTie game!")
                wouldYouLikeToPlayAgain()

            refreshScreen()
            for i in range(2):
                pcLoading()
            board.aiMoves("O")
            
            if board.isWinner("O"):
                board.playerScore[1] += 1
                refreshScreen()
                print("\nPC wins!")
                wouldYouLikeToPlayAgain()

            if board.isTie():
                print("\nTie game!")
                wouldYouLikeToPlayAgain()

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
        elif (self.cells[1] == " "):
            self.update_cell(1, player)
        
        elif (self.cells[2] == " "):
            self.update_cell(2, player)

        elif (self.cells[3] == " "):
            self.update_cell(3, player)

        elif (self.cells[4] == " "):
            self.update_cell(4, player)

        elif (self.cells[5] == " "):
            self.update_cell(5, player)

        elif (self.cells[6] == " "):
            self.update_cell(6, player)

        elif (self.cells[7] == " "):
            self.update_cell(7, player)

        elif (self.cells[8] == " "):
            self.update_cell(8, player)

        elif (self.cells[9] == " "):
            self.update_cell(9, player)

        refreshScreen()

board = Board()

def wouldYouLikeToPlayAgain():
    print("Would you like to play again? (Y/N) > ")
    playAgain = getchar().upper()
    if (playAgain == "Y"):
        board.reset()
    else:
        menuSystem()

def printHeader():
    print(" "*size,"╔═══════════════════════════════════════════════════════════╗")
    print(" "*size,"║       _____ _     _____          _____                    ║")
    print(" "*size,"║      /__  /(_) __/__   \__ _  __/__   \___   ___          ║")
    print(" "*size,"║        / /\/ |/ __|/ /\/ _` |/ __|/ /\/ _ \ / _ |         ║")
    print(" "*size,"║       / /  | | (__/ / | (_| | (__/ / | (_) |  __/         ║")
    print(" "*size,"║       \/   |_|\___\/   \__,_|\___\/   \___/ \___|         ║")
    print(" "*size,"║            To exit, enter a letter anytime.               ║")
    print(" "*size,"║                                                           ║")

def refreshScreen():
    os.system("clear")
    printHeader()
    board.display()

def refreshLoad():
    os.system("clear")
    board.loadingScreen()

def pvpMode():
    p1 = input("\nEnter name of player 1 > ")
    if (p1 == "" or " " in p1 or len(p1) > 8):
            p1 = "Player 1"
            board.playerScoreName[0] = p1
    elif (p1 == "" or " " in p1 or len(p1) == 7):
        board.playerScoreName[0] = p1+" "
    elif (p1 == "" or " " in p1 or len(p1) == 6):
        board.playerScoreName[0] = p1+" "
    elif (p1 == "" or " " in p1 or len(p1) == 5):
        board.playerScoreName[0] = p1+"  "
    elif (p1 == "" or " " in p1 or len(p1) == 4):
        board.playerScoreName[0] = p1+"  "
    elif (p1 == "" or " " in p1 or len(p1) == 3):
        board.playerScoreName[0] = p1+"   "
    elif (p1 == "" or " " in p1 or len(p1) == 2):
        board.playerScoreName[0] = p1+"   "
    elif (p1 == "" or " " in p1 or len(p1) == 1):
        board.playerScoreName[0] = p1+"    "
    refreshScreen()
    p2 = input("\nEnter name of player 2 > ")
    if (p2 == "" or " " in p2 or len(p2) > 8):
        p2 = "Player 2"
        board.playerScoreName[1] = p2
    elif (p2 == "" or " " in p2 or len(p2) == 7):
        board.playerScoreName[1] = p2+" "
    elif (p2 == "" or " " in p2 or len(p2) == 6):
        board.playerScoreName[1] = p2+" "
    elif (p2 == "" or " " in p2 or len(p2) == 5):
        board.playerScoreName[1] = p2+"  "
    elif (p2 == "" or " " in p2 or len(p2) == 4):
        board.playerScoreName[1] = p2+"  "
    elif (p2 == "" or " " in p2 or len(p2) == 3):
        board.playerScoreName[1] = p2+"   "
    elif (p2 == "" or " " in p2 or len(p2) == 2):
        board.playerScoreName[1] = p2+"   "
    elif (p2 == "" or " " in p2 or len(p2) == 1):
        board.playerScoreName[1] = p2+"    "
    refreshScreen()
    while True:
        refreshScreen()
        while True:
            refreshScreen()
            sys.stdout.write("\n%s, Please choose 1-9 > " % (p1))
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
                menuSystem()
                
        board.update_cell(x_choice, "X")
        refreshScreen()
        if board.isWinner("X"):
            board.playerScore[0] += 1
            refreshScreen()
            print("\n%s wins!" % (p1))
            wouldYouLikeToPlayAgain()

        if board.isTie():
            print("\nTie game!")
            wouldYouLikeToPlayAgain()

        refreshScreen()
        while True:
            refreshScreen()
            sys.stdout.write("\n%s, Please choose 1-9 > " % (p2))
            o_choice = getchar()
            if o_choice.isdigit():
                o_choice = int(o_choice)
                if o_choice != 0 and board.cells[o_choice] == " ":
                    break
                elif o_choice == 0:
                    print("\nInvalid spot selected.")
                    time.sleep(1)
                    refreshScreen()
                else:
                    print("\nSpot already taken.")
                    time.sleep(1)
                    refreshScreen()
            elif o_choice != "q":
                print("\nInvalid input.")
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
            print("\n%s wins!" % (p2))
            wouldYouLikeToPlayAgain()

        if board.isTie():
            print("\nTie game!")
            wouldYouLikeToPlayAgain()

def pcLoading():
    refreshScreen()
    print("\nPC's turn > |")
    time.sleep(0.2)
    refreshScreen()
    print("\nPC's turn > / ")
    time.sleep(0.2)
    refreshScreen()
    print("\nPC's turn > ─ ")
    time.sleep(0.2)
    refreshScreen()
    print("\nPC's turn > \ ")
    time.sleep(0.2)
    refreshScreen()

def menuSystem():
    while True:
        refreshScreen()
        try:
            print("\n","  "*size,"> Main Menu <")
            print("\n"," "*size2,"Start game: [S]")
            print("\n"," "*size3,"Help: [H]")
            print("\n"," "*size3,"Exit: [Q]")
            sys.stdout.write("\nChoose a menupoint > ")
            menuChoice = getchar()
            if menuChoice == "s":
                refreshScreen()
                gameStart()
                break
            elif menuChoice == "h":
                gameHelp()
                menuSystem()
            elif menuChoice == "q":
                print("kakakaka")
                time.sleep(5)
                quit()
            else:
                print("\nInvalid menupoint selected")
                time.sleep(1)
                refreshScreen()
        except ValueError:
            print("whatdidyoujustdo")

def gameHelp():
    print("\nasdasdsad")
    getchar()

def gameStart():
    while True:
        refreshScreen()
        print("\n","  "*size+"> Game Mode <")
        print("\n"," "*size2+"1 Player: [1]")
        print("\n"," "*size2+"2 Player: [2]")
        sys.stdout.write("\n\nChoose gamemode > ")
        gameMode = getchar()
        if gameMode == "1":
            refreshScreen()
            print("\nYou have selected 1 player mode!", end="")
            time.sleep(2)
            refreshScreen()
            board.aiMode()
            break
        elif gameMode == "2":
            refreshScreen()
            print("\nYou have selected 2 player mode!", end="")
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

terminal_size()
size = int((terminal_size() - 96) / 2)
size2 = int(terminal_size() - 97)
size3 = int(terminal_size() - 95)
#refreshLoad()
#board.updateLoad(0, "∎")
refreshScreen()
menuSystem()
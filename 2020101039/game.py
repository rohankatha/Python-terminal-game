from logging import _STYLES
import colorama
from colorama import Fore, Back, Style
import time
import sys
import termios
import tty
import signal


class Get:
    """Class to get input."""

    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    """Handling alarm exception."""
    pass


def alarmHandler(signum, frame):
    """Handling timeouts."""
    raise AlarmException


def input_to(timeout=0.1):
    """Taking input from user."""
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = Get()()
        signal.alarm(0)
        return text
    except AlarmException:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None


n = 15
coordinates = [[' ' for y in range(n)] for x in range(n)]
coordinates[4][5] = '&'
coordinates[3][2] = '$'
coordinates[1][8] = '$'

coordinates[7][4] = 'H'
coordinates[2][10] = 'H'
coordinates[11][2] = 'H'
coordinates[11][7] = 'H'
coordinates[8][13] = 'H'
coordinates[7][5] = 'W'
coordinates[7][6] = 'T'
coordinates[7][7] = 'T'
coordinates[7][8] = 'T'
coordinates[7][9] = 'T'
coordinates[6][6] = 'T'
coordinates[6][7] = 'T'
coordinates[6][8] = 'T'
coordinates[6][9] = 'T'
coordinates[6][10] = 'W'
coordinates[8][6] = 'T'
coordinates[8][7] = 'T'
coordinates[8][8] = 'T'
coordinates[8][9] = 'T'
coordinates[14][0] = 'W'
coordinates[14][1] = 'W'
coordinates[14][2] = 'W'
coordinates[14][3] = 'W'
coordinates[14][4] = 'W'
coordinates[14][5] = 'W'


x = 4
y = 5


class king:

     health = 2500
     attack = 100


class canon:
     attack = 300
     strength = 500


class barbains:
     attack = 20
     health = 3000


class building:
     strength = 200


class hut:
     strength = 10


class townhall:
     strength = 50


gameking = king()
gamequeen = king()
gamequeen.attack = 80

gamecanon = canon()
gamecanon1 = canon()
gamecanon2 = canon()
gamecanon3 = canon()

gamebarbains = barbains()
gamebarbains1 = barbains()
gamebarbains2 = barbains()


def printgrid():
    global coordinates
    global n

    stringvar = "   "

    for row in range(n):
        stringvar = "     "
        if row == 0:
            for col in range(n):
                stringvar = stringvar + "______"
            print(stringvar)

        stringvar = "     "
        for col in range(n):
            stringvar = stringvar + "|     "
        print(stringvar + "|")

        stringvar = "  " + str(' ') + "  "
        for col in range(n):

                 stringvar = stringvar + "|  " + \
                     str(coordinates[row][col]) + "  "

        print(stringvar + "|")

        stringvar = "     "
        for col in range(n):
            stringvar = stringvar + "|_____"
        print(stringvar + "|")


printgrid()


def getcurrpos():
    global x
    global y
    for i in range(n):
        for j in range(n):
            if(coordinates[i][j] == '&'):
                x = i
                y = j


def getcurrposq():
    global x
    global y
    for i in range(n):
        for j in range(n):
            if(coordinates[i][j] == '%'):
                x = i
                y = j


def incanonarea():
    getcurrpos()


def kingattr():
    print(gameking.health)
    print(gameking.attack)
    print(f'{Back.YELLOW}{Back.RESET}')
    if(gameking.health <= 1500 and gameking.health >= 900):
      print(f'{Back.YELLOW}           {Back.RESET}')

    if(gameking.health >= 1500):
       print(f'{Back.GREEN}                {Back.RESET}')
    if(gameking.health <= 900 and gameking.health >= 0):
       print(f'{Back.RED}        {Back.RESET}')
    if(gameking.health <= 0):
       print("GAME OVER  YOU LOST")
    if(gamecanon.attack == 0 and gamecanon1.attack == 0):
       print("YOU WON LEVEL 1")
       coordinates[9][1] = '$'
       coordinates[3][2] = '$'
       coordinates[1][8] = '$'
       gamecanon.strength = 400
       gamecanon1.strength = 400
       gamecanon.attack = 350
       gamecanon1.attack = 350
       gameking.health = 2550
       gameking.attack = 125

    if(gamecanon.attack == 0 and gamecanon1.attack == 0 and gamecanon2.attack == 0):
       print("YOU WON LEVEL 2")

       coordinates[5][8] = '$'
       coordinates[9][1] = '$'
       coordinates[3][2] = '$'
       coordinates[1][8] = '$'
       gamecanon.strength = 420
       gamecanon1.strength = 420
       gamecanon2.strength = 420
       gamecanon.attack = 400
       gamecanon1.attack = 400
       gamecanon2.attack = 400

       gameking.health = 2700
       gameking.attack = 150


def queenattr():
    print(gamequeen.health)
    print(gamequeen.attack)
    print(f'{Back.YELLOW}{Back.RESET}')
    if(gamequeen.health <= 1500 and gamequeen.health >= 900):
      print(f'{Back.YELLOW}           {Back.RESET}')

    if(gamequeen.health >= 1500):
       print(f'{Back.GREEN}                {Back.RESET}')
    if(gamequeen.health <= 900 and gamequeen.health >= 0):
       print(f'{Back.RED}        {Back.RESET}')
    if(gamequeen.health <= 0):
       print("GAME OVER  YOU LOST")

    if(gamecanon.attack == 0 and gamecanon1.attack == 0):
       print("YOU WON LEVEL 1")
       coordinates[9][1] = '$'
       coordinates[3][2] = '$'
       coordinates[1][8] = '$'
       gamecanon.strength = 400
       gamecanon1.strength = 400
       gamecanon.attack = 350
       gamecanon1.attack = 350
       gamequeen.health = 2550
       gamequeen.attack = 125

    if(gamecanon.attack == 0 and gamecanon1.attack == 0 and gamecanon2.attack == 0):
       print("YOU WON LEVEL 2")

       coordinates[5][8] = '$'
       coordinates[9][1] = '$'
       coordinates[3][2] = '$'
       coordinates[1][8] = '$'
       gamecanon.strength = 420
       gamecanon1.strength = 420
       gamecanon2.strength = 420
       gamecanon.attack = 400
       gamecanon1.attack = 400
       gamecanon2.attack = 400

       gamequeen.health = 2700
       gamequeen.attack = 150


def checkking():
    getcurrpos()
    if(x == 3 and y == 1 or x == 3 and y == 3 or x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 4 and y == 1 or x == 4 and y == 2):
        gameking.health = gameking.health-gamecanon.attack

        if(gamecanon.strength <= 0):
            coordinates[3][2] = ' '
            gamecanon.attack = 0
    if(x == 0 and y == 7 or x == 0 and y == 8 or x == 0 and y == 9 or x == 1 and y == 7 or x == 1 and y == 9 or x == 2 and y == 7 or x == 2 and y == 9):
        gameking.health = gameking.health-gamecanon1.attack

        if(gamecanon1.strength <= 0):
            coordinates[1][8] = ' '
            gamecanon1.attack = 0
    if(gamecanon.attack == 0 and gamecanon1.attack == 0):
       if(x == 9 and y == 0 or x == 9 and y == 2 or x == 8 and y == 0 or x == 10 and y == 0 or x == 8 and y == 1 or x == 8 and y == 2 or x == 10 and y == 2):
        gameking.health = gameking.health-gamecanon2.attack

        if(gamecanon2.strength <= 0):
            coordinates[9][1] = ' '
            gamecanon2.attack = 0
    if(gamecanon.attack == 0 and gamecanon1.attack == 0 and gamecanon2.attack == 0):
       if(x == 5 and y == 9 or x == 5 and y == 7 or x == 6 and y == 10 or x == 4 and y == 9 or x == 4 and y == 8 or x == 4 and y == 10 or x == 6 and y == 8):
        gameking.health = gameking.health-gamecanon3.attack

        if(gamecanon3.strength <= 0):
            coordinates[5][8] = ' '
            gamecanon3.attack = 0


def checkqueen():
    getcurrposq()
    if(x == 3 and y == 1 or x == 3 and y == 3 or x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 4 and y == 1 or x == 4 and y == 2):
        gamequeen.health = gamequeen.health-gamecanon.attack

        if(gamecanon.strength <= 0):
            coordinates[3][2] = ' '
            gamecanon.attack = 0
    if(x == 0 and y == 7 or x == 0 and y == 8 or x == 0 and y == 9 or x == 1 and y == 7 or x == 1 and y == 9 or x == 2 and y == 7 or x == 2 and y == 9):
        gamequeen.health = gamequeen.health-gamecanon1.attack

        if(gamecanon1.strength <= 0):
            coordinates[1][8] = ' '
            gamecanon1.attack = 0
    if(gamecanon.attack == 0 and gamecanon1.attack == 0):
       if(x == 9 and y == 0 or x == 9 and y == 2 or x == 8 and y == 0 or x == 10 and y == 0 or x == 8 and y == 1 or x == 8 and y == 2 or x == 10 and y == 2):
        gamequeen.health = gamequeen.health-gamecanon2.attack

        if(gamecanon2.strength <= 0):
            coordinates[9][1] = ' '
            gamecanon2.attack = 0
    if(gamecanon.attack == 0 and gamecanon1.attack == 0 and gamecanon2.attack == 0):
       if(x == 5 and y == 9 or x == 5 and y == 7 or x == 6 and y == 10 or x == 4 and y == 9 or x == 4 and y == 8 or x == 4 and y == 10 or x == 6 and y == 8):
        gamequeen.health = gamequeen.health-gamecanon3.attack

        if(gamecanon3.strength <= 0):
            coordinates[5][8] = ' '
            gamecanon3.attack = 0


print("What do you want player king or queen Choose king by pressing w and queen by pressing p")
a = 0
while True:

 key = input_to()
 if(key == 'p'):
      a = 1
      print("queen has beeen selected")
      coordinates[4][5] = '%'
 if(a == 0):
   if(key == 'w'):
    print("\033[H\033[J", end="")

    checkking()
    if(gameking.health <= 1500 and gameking.health >= 900):

       coordinates[x-1][y] = '&'
    if(gameking.health >= 1500):
       coordinates[x-1][y] = '&'
    if(gameking.health <= 900 and gameking.health >= 0):
       coordinates[x-1][y] = '&'

    if(gameking.health <= 0):
       coordinates[x-1][y] = " "

    coordinates[x][y] = ' '

    printgrid()
    kingattr()

   if(key == 's'):
    print("\033[H\033[J", end="")

    checkking()
    coordinates[x][y] = ' '
    if(gameking.health <= 1500 and gameking.health >= 900):

       coordinates[x+1][y] = '&'
    if(gameking.health >= 1500):
       coordinates[x+1][y] = '&'
    if(gameking.health <= 900 and gameking.health >= 0):
       coordinates[x+1][y] = '&'

    if(gameking.health <= 0):
       coordinates[x+1][y] = " "

    printgrid()
    kingattr()

   if(key == 'a'):
    print("\033[H\033[J", end="")
    checkking()
    coordinates[x][y] = ' '

    if(gameking.health <= 1500 and gameking.health >= 900):

       coordinates[x][y-1] = '&'
    if(gameking.health >= 1500):
       coordinates[x][y-1] = '&'
    if(gameking.health <= 900 and gameking.health >= 0):
       coordinates[x][y-1] = '&'

    if(gameking.health <= 0):
       coordinates[x][y-1] = " "

    printgrid()
    kingattr()

   if(key == 'd'):
    print("\033[H\033[J", end="")
    checkking()
    coordinates[x][y] = ' '

    if(gameking.health <= 1500 and gameking.health >= 900):

       coordinates[x][y+1] = '&'
    if(gameking.health >= 1500):
       coordinates[x][y+1] = '&'
    if(gameking.health <= 900 and gameking.health >= 0):
       coordinates[x][y+1] = '&'

    if(gameking.health <= 0):
       coordinates[x][y+1] = " "

    printgrid()
    kingattr()

   if(key == 'o'):
      print(x)
      print()
      print(y)

   if(key == 'v'):
      print("\033[H\033[J", end="")
      printgrid()
      kingattr()
   if(key == 'b'):
      print("\033[H\033[J", end="")
      if(coordinates[11][12] == 'B'):
          coordinates[13][9] = 'B'
      if(coordinates[1][9] == 'B'):
          coordinates[11][12] = 'B'

      coordinates[1][9] = 'B'
      printgrid()
      kingattr()
   if(key == 'y'):
      i = 1
      while i < 10:
        time.sleep(0.2)
        print(u"{}[2J{}[;H".format(chr(27), chr(27)))
        coordinates[i+1][9] = 'T'
        coordinates[i][9] = ' '
        i = i+1

        printgrid()

   if(key == 'l'):
      print("END GAME")
      break
   if(key == ' '):
    if(x == 3 and y == 1 or x == 3 and y == 3 or x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 4 and y == 1 or x == 4 and y == 2):
       gamecanon.strength = gamecanon.strength-gameking.attack
       
    if(x == 0 and y == 7 or x == 0 and y == 8 or x == 0 and y == 9 or x == 1 and y == 7 or x == 1 and y == 9 or x == 2 and y == 7 or x == 2 and y == 9):
       gamecanon1.strength = gamecanon1.strength-gameking.attack
    if(x == 9 and y == 0 or x == 9 and y == 2 or x == 8 and y == 0 or x == 10 and y == 0 or x == 8 and y == 1 or x == 8 and y == 2 or x == 10 and y == 2):
       gamecanon2.strength = gamecanon2.strength-gameking.attack
    if(x == 5 and y == 9 or x == 5 and y == 7 or x == 6 and y == 10 or x == 4 and y == 9 or x == 4 and y == 8 or x == 4 and y == 10 or x == 6 and y == 8):
       gamecanon3.strength = gamecanon3.strength-gameking.attack 
    
     
 else:
     if(key == 'l'):
      print("END GAME")
      break
     if(key == 'q'):
        print("\033[H\033[J", end="")
        printgrid()
     if(key == 'w'):
       print("\033[H\033[J", end="")
       checkqueen()
       coordinates[x][y] = ' '
       if(gamequeen.health <= 1500 and gamequeen.health >= 900):

            coordinates[x-1][y] = '%'
       if(gamequeen.health >= 1500):
          coordinates[x-1][y] = '%'
       if(gamequeen.health <= 900 and gamequeen.health >= 0):
          coordinates[x-1][y] = '%'

       if(gamequeen.health <= 0):
           coordinates[x-1][y] = " "

       printgrid()
       queenattr()
     if(key == 's'):
      print("\033[H\033[J", end="")
      checkqueen()
      coordinates[x][y] = ' '

      if(gamequeen.health <= 1500 and gamequeen.health >= 900):

        coordinates[x+1][y] = '%'
      if(gamequeen.health >= 1500):
        coordinates[x+1][y] = '%'
      if(gamequeen.health <= 900 and gamequeen.health >= 0):
       coordinates[x+1][y] = '%'

      if(gamequeen.health <= 0):
       coordinates[x+1][y] = " "

      coordinates[x][y] = ' '
      printgrid()
      kingattr()

     if(key == 'a'):
      print("\033[H\033[J", end="")
      checkqueen()
      coordinates[x][y] = ' '

      if(gamequeen.health <= 1500 and gamequeen.health >= 900):

       coordinates[x][y-1] = '%'
      if(gamequeen.health >= 1500):
       coordinates[x][y-1] = '%'
      if(gamequeen.health <= 900 and gamequeen.health >= 0):
       coordinates[x][y-1] = '%'

      if(gamequeen.health <= 0):
       coordinates[x][y-1] = " "

     printgrid()
     queenattr()
     if(key == 'd'):
      print("\033[H\033[J", end="")
      checkqueen()
      coordinates[x][y] = ' '
      if(gamequeen.health <= 1500 and gamequeen.health >= 900):

        coordinates[x][y+1] = '%'
      if(gamequeen.health >= 1500):
        coordinates[x][y+1] = '%'
      if(gamequeen.health <= 900 and gamequeen.health >= 0):
        coordinates[x][y+1] = '%'

      if(gamequeen.health <= 0):
        coordinates[x][y+1] = " "

      printgrid()
      queenattr()

     if(key == 'o'):
      print(x)
      print()
      print(y)
     if(key == ' '):
      if(x == 11 and y == 2 or x == 3 and y == 10):
       gamecanon.strength = gamecanon.strength-gamequeen.attack
       
      if(x == 9 and y == 8 or x == 3 and y == 10):
       gamecanon1.strength = gamecanon1.strength-gamequeen.attack
       
      if(x == 13 and y == 8 or x == 3 and y == 10):
       gamecanon2.strength = gamecanon2.strength-gamequeen.attack
      
      if(x == 0 and y == 1 or x == 9 and y == 9):
       gamecanon3.strength = gamecanon3.strength-gamequeen.attack
      
      
     if(key == 'v'):
      print("\033[H\033[J", end="")
      printgrid()
      queenattr()
     if(key == 'b'):
      print("\033[H\033[J", end="")
      if(coordinates[11][12] == 'B'):
          coordinates[13][9] = 'B'
      if(coordinates[1][9] == 'B'):
          coordinates[11][12] = 'B'
      
      coordinates[1][9] = 'B'
      printgrid()
      queenattr()
     if(key == 'y'):
      i = 1
      while i<10:
        time.sleep(0.2) 
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        coordinates[i+1][9] = 'T'
        coordinates[i][9] = ' '
        i = i+1
    
        printgrid()
         

      
     
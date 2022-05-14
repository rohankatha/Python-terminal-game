if(a == 0):
   if(key == 'w'):
       print("\033[H\033[J", end="")
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

        if(gamequeen.health <= 1500 and gamequeen.health >= 900):

            coordinates[x-1][y] =  '%' 
        if(gamequeen.health >= 1500):
          coordinates[x-1][y] = '%' 
        if(gamequeen.health <= 900 and gamequeen.health >= 0):
          coordinates[x-1][y] =  '%'  

        if(gamequeen.health <= 0):
           coordinates[x-1][y] = " "
       
     
       coordinates[x][y] = ' '
   
       printgrid()
       queenattr()

   if(key == 's'):
    print("\033[H\033[J", end="")
    
    getcurrposq()
    if(x == 3 and y == 1 or x == 3 and y == 3 or x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 4 and y == 1 or x == 4 and y == 2):
        gamequeen.health = gamequeen.health-gamecanon.attack
       
        if(gamecanon.strength <= 0):

            gamecanon.attack = 0
    if(x == 0 and y == 7 or x == 0 and y == 8 or x == 0 and y == 9 or x == 1 and y == 7 or x == 1 and y == 9 or x == 2 and y == 7 or x == 2 and y == 9):
        gamequeen.health = gamequeen.health-gamecanon1.attack
        
        if(gamecanon1.strength <= 0):
            coordinates[1][8] = ' '
            gamecanon1.attack = 0
    
        coordinates[x][y] = ' '
    if(gamequeen.health <= 1500 and gamequeen.health >= 900):

       coordinates[x+1][y] = '%' 
    if(gamequeen.health >= 1500):
       coordinates[x+1][y] = '%'
    if(gamequeen.health <= 900 and gamequeen.health >= 0):
       coordinates[x+1][y] = '%' 

    if(gamequeen.health <= 0):
       coordinates[x+1][y] = " "
    
    printgrid()
    kingattr()


   if(key == 'a'):
    print("\033[H\033[J", end="")
    getcurrposq()
    coordinates[x][y] = ' '
    if(x == 3 and y == 1 or x == 3 and y == 3 or x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 4 and y == 1 or x == 4 and y == 2):
        gamequeen.health = gamequeen.health-gamecanon.attack
        
        if(gamecanon.strength <= 0):

            gamecanon.attack = 0
    if(x == 0 and y == 7 or x == 0 and y == 8 or x == 0 and y == 9 or x == 1 and y == 7 or x == 1 and y == 9 or x == 2 and y == 7 or x == 2 and y == 9):
        gamequeen.health = gamequeen.health-gamecanon1.attack
        
        if(gamecanon1.strength <= 0):
            coordinates[1][8] = ' '
            gamecanon1.attack = 0
    
    if(gamequeen.health <= 1500 and gamequeen.health >= 900):

       coordinates[x][y-1] =  '%'
    if(gamequeen.health >= 1500):
       coordinates[x][y-1] =  '%'
    if(gamequeen.health <= 900 and gamequeen.health >= 0):
       coordinates[x][y-1] = '%' 

    if(gamequeen.health <= 0):
       coordinates[x][y-1] = " "
   
   
    printgrid()
    queenattr()

   if(key == 'd'):
    print("\033[H\033[J", end="")
    getcurrpos()
    if(x == 3 and y == 1 or x == 3 and y == 3 or x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 4 and y == 1 or x == 4 and y == 2):
        gamequeen.health = gamequeen.health-gamecanon.attack
        
        if(gamecanon.strength <= 0):

            gamecanon.attack = 0

    if(x == 0 and y == 7 or x == 0 and y == 8 or x == 0 and y == 9 or x == 1 and y == 7 or x == 1 and y == 9 or x == 2 and y == 7 or x == 2 and y == 9):
        gamequeen.health = gamequeen.health-gamecanon1.attack
        
        if(gamecanon1.strength <= 0):
            coordinates[1][8] = ' '
            gamecanon1.attack = 0
    if(gamequeen.health <= 1500 and gamequeen.health >= 900):

       coordinates[x][y+1] = '%'
    if(gamequeen.health >= 1500):
       coordinates[x][y+1] = '%' 
    if(gamequeen.health <= 900 and gamequeen.health >= 0):
       coordinates[x][y+1] = '%'  

    if(gamequeen.health <= 0):
       coordinates[x][y+1] = " "
   
    coordinates[x][y] = ' '
   
    printgrid()
    queenattr()

   if(key == 'o'):
      print(x)
      print()
      print(y)
  
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


  

   if(key == 'l'):
      print("END GAME")
      break
   if(key == ' '):
    if(x == 3 and y == 1 or x == 3 and y == 3 or x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 4 and y == 1 or x == 4 and y == 2):
       gamecanon.strength = gamecanon.strength-gamequeen.attack
       print(gamecanon.strength)
    if(x == 0 and y == 7 or x == 0 and y == 8 or x == 0 and y == 9 or x == 1 and y == 7 or x == 1 and y == 9 or x == 2 and y == 7 or x == 2 and y == 9):
       gamecanon1.strength = gamecanon1.strength-gamequeen.attack

   
  
    
       

      





screen = 0
theBoard = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']]
b_w = 200
b_h = 55
x_col =[255,0,0]
o_col = [0,0,255]
X = [False, False ,False]
O = [False, False ,False]
button1 = (350,450)
button2 = (350,550)
button3 = (350,650)
buttons = [False,False,False]
board = None
myFont = None
boardDrawn = False
count = 0
turn = None
opponent = None
player = None
_win = False
pp = True
eg = False
p = None
begin = True
ret = False 
replay = False
start = None
AI = False

def setup():
    fontList = PFont.list()
    #print(fontList)
    global screen
    size(900,900)
    global myFont
    myFont = createFont("Palatino Linotype Italique", 16)
    textFont(myFont)
    textAlign(CENTER)

def draw():
    global chaine
    global boardDrawn
    global turn
    global start
    global count
    update(mouseX,mouseY)
    global screen
    if screen == 0 :
        clear()
        img = loadImage("data/background.jpg")
        image(img, 0,0)
        img2 =loadImage("data/logo.png")
        img2.resize(0, 200);
        image(img2, 200, 70)
        button(button1[0],button1[1],b_w,b_h,"PVP!",187,187,255,0,0,0)
        button(button2[0],button2[1],b_w,b_h,"PVE!",187,187,255,0,0,0)
    if screen == 1 or screen == 2:
        if not boardDrawn:
            print(count)
            if screen ==2:
                start = input("Who's gonna start ? You(0) or the AI(1)?")
                print(start)
            clear()
            turn = input('Choose you weapon : X or O  ')
            background(216,191,216)
            print("jk")
            stroke(0,0,0)
            grid(250,250,133)
            boardDrawn = True
            text("X color", 130, 100)
            text("O color", 775, 100)
            strokeCap(ROUND)
            fill(255,0,0)
            square(750, 150, 55)
            
            fill(0,255,0)
            square(750, 250, 55)
            
            fill(0,0,255)
            square(750, 350, 55)
            
            
            
            fill(255,0,0)
            square(100, 150, 55)
            
            fill(0,255,0)
            square(100, 250, 55)
            
            fill(0,0,255)
            square(100, 350, 55)
            noFill()
    if screen == 3:
        clear()
        background(216,191,216)
        myFont = createFont("Palatino Linotype Italique", 16)
        textFont(myFont)
        textAlign(CENTER)
    
        
        


def convert(i,j):
        if theBoard[i][j] == "X" or theBoard[i][j] == "x": 
            #draw x
            fill(255,255,255)
            drawX(board[i][j][0],board[i][j][1])
            #text("X", board[i][j][0] +50 , board[i][j][1] + 50)
        if theBoard[i][j] == "O" or theBoard[i][j] == "o" : 
            #draw o
            fill(255,255,255)
            drawO(board[i][j][0],board[i][j][1])
            #text("O", board[i][j][0] + 50 , board[i][j][1] + 50)   
    
def drawBoard( x, turn):
    global count
    global pp
    ligne = x//3
    col = x % 3
    if theBoard[ligne][col] == ' ':
        pp = True
        theBoard[ligne][col] = turn
        count += 1
        convert(ligne,col)
    else:
        pp = False
        print("This position is not available, choose again ")
  
    

def grid(x,y,l):
    global board
    board = [ [(x, y),(x + l , y),(x + l * 2, y)],
              [(x, y + l),(x + l , y + l),(x + l * 2, y + l)],
              [(x , y + l * 2),(x + l , y + l * 2),(x + l * 2 , y + l * 2)]]
    noFill()
    square( board[0][0][0], board[0][0][1], l)
    square( board[0][1][0], board[0][1][1], l)
    square( board[0][2][0], board[0][2][1], l)
    square( board[1][0][0], board[1][0][1], l)
    square( board[1][1][0], board[1][1][1], l)
    square( board[1][2][0], board[1][2][1], l)
    square( board[2][0][0], board[2][0][1], l)
    square( board[2][1][0], board[2][1][1], l)
    square( board[2][2][0], board[2][2][1], l)

def win(board):
    return  (board[0][0] == board[0][1] == board[0][2] != ' ') or (board[1][0] == board[1][1] == board[1][2] != ' ') or (board[2][0] == board[2][1] == board[2][2] != ' ') or (board[0][0] == board[1][0] == board[2][0] != ' ') or (board[0][1] == board[1][1] == board[2][1] != ' ') or (board[0][2] == board[1][2] == board[2][2] != ' ') or (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[2][0] == board[1][1] == board[0][2] != ' ')


def endGame():
    global eg
    global theBoard
    global screen
    eg = True
    noStroke()
    noFill()
    button(200,700,200,55,"Back to menu",255,255,255)
    if screen == 1 :
        button(500,700,200,55,"Restart",255,255,255)
    theBoard = [
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]


def play(pos, turn):
    global _win
    global theBoard
    drawBoard( pos, turn)
    if count >= 5:
       if win(theBoard) :
            _win = True   
            fill(0, 102, 153) 
            textSize(50)
            text("GG "+turn+" ! you won ",450,170)
            theBoard = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
            endGame()
       if count == 9 and not _win:
            textSize(50)
            fill(0, 102, 153)
            text("Issa Tie ! ",450,220)
            theBoard = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
            endGame()

def playP(pos,pl,op):
    global _win
    global start
    global theBoard
    global pp
    global AI
    print(AI)
    print(AI)
    drawBoard( pos, pl)
    if pp:
        AI = True
    if count >= 5:
            if win(theBoard) :
                    _win = True 
                    winner = turn  
                    fill(0, 102, 153) 
                    
                    textSize(40)
                    text("Fortunatly, you didn't disgrace the human race ! ",450,220)
                    endGame()
            if count == 9 and not _win:
                    textSize(50)
                    fill(0, 102, 153)
                    text("Issa Tie ! ",450,220)
                    print("\nGame Over.\n")
                    endGame()

def playE(pos,pl,op):
    global _win
    global start
    global theBoard
    global pp
    global AI
    print(AI)
    print(AI)
    if pp : 
            print("je suis l'IA")
            print("IA will play in  :", findBestMove(theBoard))
            drawBoard(3*findBestMove(theBoard)[0]+findBestMove(theBoard)[1],op)
            AI = False
            if count >= 5:
                    if win(theBoard) :
                            _win = True 
                            winner = turn  
                            fill(0, 102, 153) 
                            
                            textSize(40)
                            text("You got outplayed by an algorithm !  ",450,220)
                            endGame()
            if count == 9 and not _win:
                    textSize(50)
                    fill(0, 102, 153)
                    text("Issa Tie ! ",450,220)
                    print("\nGame Over.\n")
                    endGame()

                        
        




def button( x, y, w, h, t, r = 0, g = 0, b = 0, _r = 0, _g = 0, _b = 0):
    global myFont
    fill(r,g,b)
    rect(x, y, w, h, 7)
    fill(_r,_g,_b)
    textFont(myFont)
    text(t, x + 100, y + 35)
 
def overRect(x, y, w, h):
    if (mouseX >= x and mouseX <= x + w and mouseY >= y and mouseY <= y + h ):
        return True
    else:
        return False
def overSquare(x,y,l):
    if (mouseX >= x and mouseX <= x + l and mouseY >= y and mouseY <= y + l ):
        return True
    else:
        return False

def update(x, y):
  global buttons
  global screen
  global p
  global eg
  global boardDrawn
  global ret 
  global replay
  global X
  global O
  
  if screen == 1 or screen == 2 : 
      if overSquare(750,150,55):
          O = [False for i in range(len(O))]
          O[0] = True
      elif overSquare(750,250,55):
          O = [False for i in range(len(O))]
          O[1] = True
      elif overSquare(750,350,55):
          O = [False for i in range(len(O))]
          O[2] = True
      if overSquare(150,150,55):
          X = [False for i in range(len(X))]
          X[0] = True
          print(X)
      elif overSquare(150,250,55):
          X = [False for i in range(len(X))]
          X[1] = True
      elif overSquare(150,350,55):
          X = [False for i in range(len(X))]
          X[2] = True
        
  if screen == 0:
    if ( overRect(button1[0], button1[1], b_w , b_h) ):
        buttons = [False for i in range(len(buttons))]
        buttons[0] = True
    elif ( overRect(button2[0], button2[1], b_w , b_h) ):
        buttons = [False for i in range(len(buttons))]
        buttons[1] = True
    elif (overRect(button3[0], button3[1], b_w , b_h)):
        buttons = [False for i in range(len(buttons))]
        buttons[2] = True
    else :
        buttons = [False for i in range(len(buttons))]
  if boardDrawn:
    l = 133
    if overSquare( board[0][0][0], board[0][0][1], l) : 
        p = 1
    elif overSquare( board[0][1][0], board[0][1][1], l):
        p = 2
    elif overSquare( board[0][2][0], board[0][2][1], l):
         p = 3
    elif overSquare( board[1][0][0], board[1][0][1], l):
         p = 4
    elif overSquare( board[1][1][0], board[1][1][1], l):
         p = 5
    elif overSquare( board[1][2][0], board[1][2][1], l):
         p = 6
    elif overSquare( board[2][0][0], board[2][0][1], l):
         p = 7
    elif overSquare( board[2][1][0], board[2][1][1], l):
         p = 8
    elif overSquare( board[2][2][0], board[2][2][1], l):
         p = 9
    else  :
        p = None
    if eg : 
        if overRect(200,700,200,55) :
            ret = True 
        else : 
            ret = False
            
        if overRect(500,700,200,55) and screen == 1: 
            replay = True
        else : 
            replay = False
            
         
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                return True
    return False


def drawX(xc,yc):
    global x_col
    strokeCap(ROUND)
    strokeWeight(8)
    stroke(x_col[0],x_col[1],x_col[2])
    line(xc+8,yc+8,xc+125,yc+125)
    line(xc+125,yc+8,xc+8,yc+125)
    
def drawO(xc,yc):
    global o_col
    noFill()
    noStroke()
    strokeCap(ROUND)
    strokeWeight(8)
    stroke(o_col[0],o_col[1],o_col[2])
    circle(xc+66.5,yc+66.5,125)

def mousePressed():
    global p
    global screen
    global _win
    global turn
    global opponent
    global player
    global pp
    global boardDrawn
    global ret 
    global replay
    global O
    global X
    global x_col
    global o_col
    global theBoard
    global count 
    global begin
    global AI
    global start 
    if True in X : 
        x_col = [255 if i == True else 0 for i in X]
        print("x",x_col)
    if True in O : 
        o_col = [255 if i == True else 0 for i in O]
        print("O",o_col)
    if buttons[0] :
        screen = 1
    if buttons[1] :
        screen = 2
    if buttons[2] :
        screen = 3
    if screen == 1 and boardDrawn and not _win:
        if begin:
            begin = False
            play(int(p)-1,turn)
        if p <= 9 and p >= 1 and not begin:
             if pp:
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                play(int(p)-1,turn)
             else:
                play(int(p)-1,turn)
                
                
    if screen == 2 and boardDrawn and not _win :
        print(turn)
        if turn == 'X' or turn == 'x':
                print("Im in" )
                side = turn
                player = turn
                
                notside = 'O'
                opponent = 'O'
        else:
                side = turn
                player = turn
                notside = 'X'
                opponent = 'X'
        if start == '0' :
            AI = False
            start = 5
        if start == '1' : 
            AI = True
            start = 6
        print("First AI value")
        print(AI)
        print("Start value",start)
        if AI:
            playE(None,player,opponent)
        else:
            if p >= 0 and p <= 9 :
                print("test")
                playP(int(p)-1,player,opponent)
                 
        
        
            
            
            
        
    if ret : 
        clear()
        theBoard = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
        screen = 0
        count = 0
        eg = False
        boardDrawn = False
        ret = False
        _win = False
    if replay :
        theBoard = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
        clear()
        print(screen)
        count = 0
        eg = False
        _win = False
        boardDrawn = False
        replay = False
def keyPressed():
    global start
    global _win
    global turn
    global opponent
    global player
    global pp
    if screen == 1 and boardDrawn and not _win: 
        if key >= '0' and key <= '9'  :
            if pp:
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                play(int(key)-1,turn)
            else:
                play(int(key)-1,turn)
    if screen == 2 and boardDrawn and not _win :
        if key >= '0' and key <= '9' :
                side = 'X'
                player = 'X'
                notside = 'O'
                opponent = 'O'
        else:
                player = 'O'
                notside = 'X'
                opponent = 'X'  
                
        playPVE(int(key)-1,player,opponent)

                              
#Voici la fonction Minimax, elle considère les différents scénarios de la partie et retroune la valeur du tableau
def minimax(board, depth, isMax):
    score = evaluate(board,depth)

    # Si le Maxplayer a gagné, on retourne son score
    if (score == 10):
        return score

    # Si le Min player a gagné, on retourne son score
    if (score == -10):
        return score

    # Si aucun coup n'est possible et qu'il n'y a pas de vainqueur, alors c'est un nul
    if (isMovesLeft(board) == False):
        return 0

    # Si c'est au tour du joueur Max de jouer
    if (isMax):
        best = -667

        # On traverse tout les cellules
        for i in range(3):
            for j in range(3):

                # On vérifie si la cellule est vide
                if (board[i][j] == ' '):
                    # On joue le coup
                    board[i][j] = opponent


                    #On appelle minimax recursivement et on choisit la valeur maximale
                    best = max(best, minimax(board,
                                             depth + 1,
                                             not isMax))

                    # On annule le coup
                    board[i][j] = ' '
        return best

    # Si c'est au tour du joueur Min
    else:
        best = 667

        # On traverse tout les cellules
        for i in range(3):
            for j in range(3):

                # On vérifie si la cellule est vide
                if (board[i][j] == ' '):
                    # Make the move
                    board[i][j] = player

                    # On appelle minimax recursivement et on choisit la valeur minimale
                    best = min(best, minimax(board, depth + 1, not isMax))

                    # On annule le coup
                    board[i][j] = ' '
        return best

# Cette fonction retournera le meilleur coup possible pour le joueur
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.

    #On traverse toutes les cellules, on évalue grace à la fonction minimax les cellules vides
    #Et on retourne la cellule avec la valeur optimale
    for i in range(3):
        for j in range(3):

            # On vérifie si la case est vide
            if (board[i][j] == ' '):

                # On joue le coup
                board[i][j] = opponent

                # On calcule l'evaluation pour ce coup
                moveVal = minimax(board, 0, False)

                # On annule le coup
                board[i][j] = ' '

                # Si la valeur du coup actuel est meilleur que la valeur max, alors on mets à jour le coup
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    
    return bestMove

def evaluate(b,depth):
    # On vérifie les lignes
    for row in range(3):
        if (b[row][0] == b[row][1]  == b[row][2]!=' '):
            if (b[row][0] == opponent):
                return 10 
            elif (b[row][0] == player):
                return -10 

    # On vérifie les colonnes
    for col in range(3):

        if (b[0][col] == b[1][col]  == b[2][col]!= ' '):

            if b[0][col] == opponent:
                return 10 
            elif (b[0][col] == player):
                return -10 

    #On vérifie les diagonales
    if (b[0][0] == b[1][1] == b[2][2] != ' '):

        if (b[0][0] == opponent):
            return 10 
        elif (b[0][0] == player):
            return -10 

    if (b[0][2] == b[1][1]  == b[2][0]!= ' '):

        if b[0][2] == opponent:  
            return 10 
        elif (b[0][2] == player):
            return -10 

    # Si aucun des deux n'a gagné, on retourne 0
    return 0                                                     
    
    
#Cette fonction nous permet de lire des caractères du clavier via une boite d'aide
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

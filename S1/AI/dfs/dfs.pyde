obst=        [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
              [1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
              [1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,3,0,0,0,0,0,0,0,1,0,0,1],
              [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
              [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
              [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#gloabl variables
ouvert = []
ferme = []
terain = [i for i in obst] 
cols = 16
rows = 16
r = 0
w = 0
source = None
goal = None
finale = False
limite = 100
# our node struct
class node:
    def __init__(self, parent, x, y, terrain=obst):
        self.value = terrain[x][y]
        self.x = x
        self.y = y
        self.parent = parent
        if self.parent == 0:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1
        self.childs = []

    def succ(self):
        if obst[self.x+1][self.y]!=1:
            self.childs.append(node(self,self.x+1,self.y)) #Bas
        if obst[self.x][self.y+1]!=1:    
            self.childs.append(node(self,self.x,self.y+1)) #Droite
        if obst[self.x-1][self.y]!=1:
            self.childs.append(node(self,self.x-1,self.y)) #Haut
        if obst[self.x][self.y-1]!=1:
            self.childs.append(node(self,self.x,self.y-1)) #Gauche

def setup():
    #setting the siize of the window
    size(500, 500)
    #getting the global variable in the function 
    global w
    global h 
    w = width / rows;
    h = height / cols;
    global source 
    global ouvert
    global ferme
    global goal
    #init the source and goal nodes based on the terain we set up
    for i in range(rows):
        for j in range(cols):
            if obst[i][j] == 2 :
                source = node(0,i,j)
            if obst[i][j] == 3:
                 goal = node(0,i,j)
   
    #Gestion du noeud source
    if source.value==3 :
        finale = True
    else:
        source.succ()
        if source.childs != []:
            for i in source.childs:
                if not i in ouvert:
                    ouvert.append(i)
            ferme.append(source)


def draw():
    #setting the background the white
    background(255)
    global finale
    global source 
    global ouvert
    global ferme
    global limite
    #showing the goal and the source points
    fill(0, 128, 0)
    noStroke()
    ellipse(source.y * h + h / 2, source.x * w + w / 2, h / 2, w / 2)
    ellipse(goal.y * h + h / 2, goal.x * w + w / 2, h / 2, w / 2)
    
    #Gestion des fils 
    if not finale and ouvert != []:
        etat_courant = ouvert.pop(0)
        if etat_courant not in ferme:
            if etat_courant.value == 3:
                finale = True
            if etat_courant.depth < limite:
                etat_courant.succ()
                if etat_courant.childs != []:
                    for i in etat_courant.childs:
                        if i not in ferme and i not in ouvert:
                            ouvert = [i] + ouvert
                if etat_courant not in ferme:
                    ferme.append(etat_courant)
    #showing the obstacles            
    for i in range(cols):
        for j in range(rows):
            if terain[i][j] == 1 :
                fill(255,0,0)
                noStroke()
                ellipse(j * h + h / 2, i * w + w / 2, h / 2, w / 2)
    #showing the visited points            
    for i in ferme:
        fill(170)
        noStroke()
        ellipse(i.y * h + h / 2, i.x * w + w / 2, h / 2, w / 2)
    #drawing the path
    path = []
    temp = etat_courant
    while (temp.parent != 0):
        path.append((temp.x,temp.y))
        temp = temp.parent
    path.append((source.x,source.y))
    noFill();
    stroke(123, 7, 232)
    strokeWeight(w / 2)
    beginShape()
    for x in path:
        vertex(x[1] * h + h / 2, x[0] * w + w / 2)
    endShape()
    
    if (finale):
        noLoop()
    if( not finale and not ouvert):
        noLoop() 

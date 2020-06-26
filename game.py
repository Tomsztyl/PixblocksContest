class Player(Sprite):
	def __init__(self,position):
		self.image = 55
		self.size = 5
		self.color=Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.position=position
		
	def update(self):
		global speedPlayer
		self.prev_position=Vector(self.position.x,self.position.y)
		rand=2
		if rand==2:
			self.image = 55
		#futurist time delay
		rand=random.randint(2,3)
		#CreateEnemy
		CreateEnemyInBoard()
		if game.key('left'):
			self.position.x-=speedPlayer
			if rand==2:
				self.image = 60
				self.angle=180
		elif game.key('right'):
			self.position.x+=speedPlayer
			if rand==2:
				self.image = 60
				self.angle=0
		elif game.key('up'):
			self.position.y+=speedPlayer
			if rand==2:
				self.image = 60
				self.angle=90
		elif game.key('down'):
			self.position.y-=speedPlayer
			if rand==2:
				self.image = 60
				self.angle=-90
		if self.collide(walls):
			self.position=self.prev_position
			
		#Teleport Transform 
		#Teleport LeftUP teleports[0]	 
		if self.collide(teleports[0]):
			self.position=Vector(90,-5)
			#self.color=teleports[0].color
			
		#Teleport RightUP teleports[1]
		if self.collide(teleports[1]):
			self.position=Vector(-90,-5)
			#self.color=teleports[1].color
										

class Enemy(Sprite):
	def __init__(self,position):
		self.image=20
		self.size=5
		self.color=Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.position=position
		self.angle=0
		
	def update(self):
		#Variables from Main()
		global speedEnemy
		global livePlayer
		global speedEnemyPatrol
		global patrolPathDistanceEnemy
		
		
		if(self.position - player.position).length<patrolPathDistanceEnemy:
			self.angle =(player.position-self.position).angle
			self.move(speedEnemy)
		else:
			#Collision protection with frame
			if (self.position.y<=-90):
				self.angle=90
			elif (self.position.y>=90): 
				self.angle=-90
			elif (self.position.x<=-90):
				self.angle=0
			elif (self.position.x>=90):
				self.angle=180	
			
			#PatrolPathAI	
			randChaneAngleEnemy=random.randint(0,20)
			if (randChaneAngleEnemy==3):
				randAngleEnemy=random.randint(0,3)
				if (randAngleEnemy==0):
					#left
					self.angle=0	
				elif(randAngleEnemy==1):
					#right
					self.angle=180
				elif(randAngleEnemy==2):
					#up
					self.angle=90
				elif(randAngleEnemy==3):
					#down
					self.angle=-90
			self.move(speedEnemyPatrol)
			
		#Colidder with Player
		if(self.collide(player)):
			player.color = Color(255,255,255)
			livePlayer-=1
			ChceckPlayerLive()
		
class Wall(Sprite):
	def __init__(self,position):
		self.position=position
		self.size=3
		self.image=63
		self.color=Color(0,0,255)
		
class Teleport(Sprite):
	def __init__(self,position):
		self.position=position
		self.image=88
		self.size=5
		self.color=Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
			
class Point(Sprite):
	def __init__(self,position):
		self.position=position
		self.image=55
		self.size=4
		self.color=Color(255,255,0)
	
	def update(self):
		if self	.collide(player):
			PointCollect()
			game.remove(self)
			
class LiveUI(Sprite):
	def __init__(self,position):
		self.position=position
		self.image=60
		self.size=7
		self.color=Color(255,255,0)
		
def CreateFrame():
	#right frame
	i=0
	while i<190:
		if i==35:
			j=0
			while j<20:
				wall=Wall(Vector(95-j,-60))
				game.add(wall)
				walls.append(wall)
				j+=1
		if i==70:
			j=0
			i+=15
			while j<40:
				wall=Wall(Vector(95-j,-25))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<15:
				wall=Wall(Vector(55,-25+j))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<41:
				wall=Wall(Vector(55+j,-10))
				game.add(wall)
				walls.append(wall)
				j+=1
		if i==85:
			i+=10
		if i==95:
			j=0
			i+=15
			while j<35:
				wall=Wall(Vector(95-j,0))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<15:
				wall=Wall(Vector(60,0+j))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<36:
				wall=Wall(Vector(60+j,15))
				game.add(wall)
				walls.append(wall)
				j+=1
		wall=Wall(Vector(95,i-95))
		game.add(wall)
		walls.append(wall)
		i+=1
	#left frame
	i=0
	while i<190:
		if i==35:
			j=0
			while j<20:
				wall=Wall(Vector(-95+j,-60))
				game.add(wall)
				walls.append(wall)
				j+=1
		if i==70:
			j=0
			i+=15
			while j<40:
				wall=Wall(Vector(-95+j,-25))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<15:
				wall=Wall(Vector(-55,-25+j))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<41:
				wall=Wall(Vector(-55-j,-10))
				game.add(wall)
				walls.append(wall)
				j+=1
		if i==85:
			i+=10
		if i==95:
			j=0
			i+=15
			while j<35:
				wall=Wall(Vector(-95+j,0))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<15:
				wall=Wall(Vector(-60,0+j))
				game.add(wall)
				walls.append(wall)
				j+=1
			j=0
			while j<36:
				wall=Wall(Vector(-60-j,15))
				game.add(wall)
				walls.append(wall)
				j+=1
		wall=Wall(Vector(-95,i-95))
		game.add(wall)
		walls.append(wall)
		i+=1
	#down frame
	i=0
	while i<190:
		wall=Wall(Vector(i-95,-95))
		game.add(wall)
		walls.append(wall)
		i+=1
	#up frame	
	i=0
	j=0
	while i<190:
		if i==95:
			while j<30:
				wall=Wall(Vector(0,95-j))
				game.add(wall)
				walls.append(wall)
				j+=1
		wall=Wall(Vector(i-95,95))
		game.add(wall)
		walls.append(wall)
		i+=1
	

def CreateObjectTeleport():
	#Create Gizmos Teleport
	
	#Create Teleport In Board
	#Teleport LeftUP teleports[0]
	teleport=Teleport(Vector(-95,-5))
	game.add(teleport)
	teleports.append(teleport)
	
	#Teleport RightUP teleports[1]
	teleport=Teleport(Vector(95,-5))
	game.add(teleport)
	teleports.append(teleport)
	
def CreateObjectDownBoardWall():
	#Create Structure Object Down Board Wall
	i=0
	while i<19:
		wall=Wall(Vector(-73+i,-35))
		game.add(wall)
		walls.append(wall)
		i+=1
		if (i==19):
			j=0
			while j<25:
				wall=Wall(Vector(-55,-35-j))
				game.add(wall)
				walls.append(wall)
				j+=1
	
	i=0
	while i<59:
		wall=Wall(Vector(-73+i,-75))
		game.add(wall)
		walls.append(wall)
		i+=1
		if (i==40):
			j=0
			while j<20:
				wall=Wall(Vector(-35,-75+j))
				game.add(wall)
				walls.append(wall)
				j+=1
				
	i=0
	while i<60:
		wall=Wall(Vector(15+i,-75))
		game.add(wall)
		walls.append(wall)
		i+=1
		if (i==30):
			j=0
			while j<20:
				wall=Wall(Vector(35,-75+j))
				game.add(wall)
				walls.append(wall)
				j+=1
	
	i=0
	while i<49:
		wall=Wall(Vector(-24+i,-55))
		game.add(wall)
		walls.append(wall)
		i+=1
		if(i==25):
			j=0
			while j<25:
				wall=Wall(Vector(0,-55-j))
				game.add(wall)
				walls.append(wall)
				j+=1
				
	i=0
	while i<49:
		wall=Wall(Vector(-24+i,-25))
		game.add(wall)
		walls.append(wall)
		i+=1
		if(i==25):
			j=0
			while j<20:
				wall=Wall(Vector(0,-25-j))
				game.add(wall)
				walls.append(wall)
				j+=1
			
	i=0
	while i<19:
		wall=Wall(Vector(73-i,-35))
		game.add(wall)
		walls.append(wall)
		i+=1
		if (i==19):
			j=0
			while j<25:
				wall=Wall(Vector(55,-35-j))
				game.add(wall)
				walls.append(wall)
				j+=1
				
	i=0
	while i<25:
		wall=Wall(Vector(-40+i,-40))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	i=0
	while i<25:
		wall=Wall(Vector(15+i,-40))
		game.add(wall)
		walls.append(wall)
		i+=1
		
def CreateObjectMiddleBoardWall():
	#Create Structure Object Middle Board Wall
	i=0
	while i<10:
		wall=Wall(Vector(-35,-10-i))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	i=0
	while i<10:
		wall=Wall(Vector(35,-10-i))
		game.add(wall)
		walls.append(wall)
		i+=1
	
	#Create Structure Object Midddle Board Wall SpawnMobs
	i=0
	while i<15:
		wall=Wall(Vector(-10-i,5))
		game.add(wall)
		walls.append(wall)
		i+=1
	i=0
	while i<15:
		wall=Wall(Vector(10+i,5))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	i=0
	while i<20:
		wall=Wall(Vector(-25,5-i))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	i=0
	while i<20:
		wall=Wall(Vector(25,5-i))
		game.add(wall)
		walls.append(wall)
		i+=1
	
	i=0
	while i<50:
		wall=Wall(Vector(-25+i,-15))
		game.add(wall)
		walls.append(wall)
		i+=1
	#**
	
	i=0
	while i<45:
		wall=Wall(Vector(-35,0+i))
		game.add(wall)
		walls.append(wall)
		i+=1
		if (i==20):
			j=0
			while j<20:
				wall=Wall(Vector(-35+j,20))
				game.add(wall)
				walls.append(wall)
				j+=1
				
	i=0
	while i<45:
		wall=Wall(Vector(35,0+i))
		game.add(wall)
		walls.append(wall)
		i+=1
		if (i==20):
			j=0
			while j<20:
				wall=Wall(Vector(35-j,20))
				game.add(wall)
				walls.append(wall)
				j+=1
				
def CreateObjectUpBoardWall():
	#Create Structure Object Up Board Wall
	i=0
	while i<49:
		wall=Wall(Vector(-24+i,44))
		game.add(wall)
		walls.append(wall)
		i+=1
		if(i==25):
			j=0
			while j<25:
				wall=Wall(Vector(0,44-j))
				game.add(wall)
				walls.append(wall)
				j+=1
				
	i=0
	while i<20:
		wall=Wall(Vector(-75+i,44))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	i=0
	while i<20:
		wall=Wall(Vector(75-i,44))
		game.add(wall)
		walls.append(wall)
		i+=1
	
	#LeftBlock
	i=0
	while i<20:
		wall=Wall(Vector(-75+i,65))
		game.add(wall)
		walls.append(wall)
		i+=1
	i=0
	while i<20:
		wall=Wall(Vector(-75+i,67))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	i=0
	while i<25:
		wall=Wall(Vector(-40+i,65))
		game.add(wall)
		walls.append(wall)
		i+=1
	i=0
	while i<25:
		wall=Wall(Vector(-40+i,67))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	#RightBlock
	
	i=0
	while i<20:
		wall=Wall(Vector(75-i,65))
		game.add(wall)
		walls.append(wall)
		i+=1
	i=0
	while i<20:
		wall=Wall(Vector(75-i,67))
		game.add(wall)
		walls.append(wall)
		i+=1
		
	i=0
	while i<25:
		wall=Wall(Vector(40-i,65))
		game.add(wall)
		walls.append(wall)
		i+=1
	i=0
	while i<25:
		wall=Wall(Vector(40-i,67))
		game.add(wall)
		walls.append(wall)
		i+=1

def CreateObjectPoint():
	#CreatePointDownBoardToUp
	i=0
	while i<170:
		point=Point(Vector(-80+i,-85))
		game.add(point)
		points.append(point)
		i+=20
		
	i=0
	while i<170:
		point=Point(Vector(-80+i,-70))
		game.add(point)
		points.append(point)
		if (i==60):
			i+=20
		i+=20
	i=0	
	while i<170:
		point=Point(Vector(-80+i,-55))
		game.add(point)
		points.append(point)
		if (i==40):
			i+=60
		i+=20
		
	i=0	
	while i<170:
		point=Point(Vector(-80+i,-40))
		game.add(point)
		points.append(point)
		if (i==40):
			i+=60
		i+=20
		
	i=40	
	while i<130:
		point=Point(Vector(-80+i,-25))
		game.add(point)
		points.append(point)
		if (i==40):
			i+=60
		i+=20
		
	i=40	
	while i<130:
		point=Point(Vector(-80+i,-10))
		game.add(point)
		points.append(point)
		if (i==40):
			i+=60
		i+=20
		
	i=40	
	while i<130:
		point=Point(Vector(-80+i,5))
		game.add(point)
		points.append(point)
		if (i==40):
			i+=60
		i+=20
		
	i=0	
	while i<170:
		point=Point(Vector(-80+i,20))
		game.add(point)
		points.append(point)
		if (i==40):
			i+=60
		i+=20
		
	i=0
	while i<170:
		point=Point(Vector(-80+i,35))
		game.add(point)
		points.append(point)
		if (i==60):
			i+=20
		i+=20
		
	i=0
	while i<170:
		point=Point(Vector(-80+i,50))
		game.add(point)
		points.append(point)
		i+=20
		
	i=0
	while i<170:
		point=Point(Vector(-80+i,65))
		game.add(point)
		points.append(point)
		if (i==0):
			i+=140
		i+=20
		
	i=0
	while i<170:
		point=Point(Vector(-80+i,80))
		game.add(point)
		points.append(point)
		if (i==60):
			i+=20
		i+=20
	
def CreateEnemyInBoard():
	global enemyCreate
	global VectorSpawnEnemyInBoard	
	#futurist time delay
	randEnemyInBoard=random.randint(0,60)
	
	if (enemyCreate==0):
		enemy=Enemy(Vector(-5+VectorSpawnEnemyInBoard,0))
		game.add(enemy)
		enemies.append(enemy)	
		enemyCreate+=1
		VectorSpawnEnemyInBoard+=5
	elif (randEnemyInBoard==3 and enemyCreate<4):
		enemy=Enemy(Vector(-5+VectorSpawnEnemyInBoard,0))
		game.add(enemy)
		enemies.append(enemy)	
		enemyCreate+=1
		VectorSpawnEnemyInBoard+=5
		
def CreateLiveUI():
	i=0
	while i<20:
		liveUI=LiveUI(Vector(-95+i,-95))
		game.add(liveUI)
		liveUIs.append(liveUI)
		i+=10
	
def PointCollect():
	global pointcollect
	global gameisOver
	global lvlChanger
	global pointcollectNextLvl
	if (gameisOver==False):
		pointcollect+=10
		if (pointcollect==pointcollectNextLvl):
			pointcollect_as_string=str(pointcollect)
			lvlChanger+=1
			lvlChanger_as_string=str(lvlChanger)
			if (language=="en"):
				print(message.show("The accumulated number of points is : "+pointcollect_as_string + " you go to the next level " + lvlChanger_as_string + " !"))
			elif (language=="pl"):
				print(message.show("Zebrana ilość punktów to : "+pointcollect_as_string + " przechodzisz do następnego lvl-u " + lvlChanger_as_string + " !"))
			pointcollectNextLvl+=680
			RestartLvl()
	elif (gameisOver==True):
		pointcollect=0
	

def ChceckInputBoxGameStart():
	global gameisOver
	global language
	
	if (language=="en"):
		messageStarted=message.show('Welcome to Pac-Man! If you want to start the game, enter yes or no if you want to pause it.') 
		if messageStarted=="yes":
			print(message.show("The game is starting! Press Enter!"))
			gameisOver=False
			GameManager()
		elif messageStarted=="no":
			print(message.show("The game will not start!"))
			game.stop()
		else:
			messageStarted=message.show("You did not enter it correctly, try again pressing the Enter key.")
			ChceckInputBoxGameStart()
	elif (language=="pl"):
		messageStarted=message.show('Witaj w grze Pac-Man! Jeżeli chcesz zacząć grę wpisz tak lub nie jeżeli chcesz ją przerwać.') 
		if messageStarted=="tak":
			print(message.show("Zaczyna się gra! Naciśnij Enter!"))
			gameisOver=False
			GameManager()
		elif messageStarted=="nie":
			print(message.show("Gra nie zacznie się!"))
			game.stop()
		else:
			messageStarted=message.show("Nie wpisałeś poprawnie spróbuj ponownie wciskając klawisz Enter.")
			ChceckInputBoxGameStart()
		
def CheckLanguage():
	global language
	
	messageLanguage=message.show("Hello, choose a language by typing en or pl! Default language is english.")
	
	if (messageLanguage=="en"):
		language="en"
	elif(messageLanguage=="pl"):
		language="pl"
	else:
		language="en"
	ChceckInputBoxGameStart()
	LevleManagerDifficulty()
	
def GameManager():
	game.background = Color(0, 0, 0)
	CreateFrame()
	CreateObjectDownBoardWall()	
	CreateObjectMiddleBoardWall()
	CreateObjectUpBoardWall()
	CreateObjectTeleport()
	CreateLiveUI()
	#CreateEnemyInBoard()
	CreateObjectPoint()
	
def RestartLvl():
	CreateObjectPoint()
	player.position=Vector(0,-50)
	BackEnemyToTheBoard()
	#enemy=Enemy(Vector(0,-50))
	#enemy.position=Vector(-5,0)

def BackEnemyToTheBoard():
	global enemyCreate
	i=0
	j=0
	while i<5*enemyCreate:
		enemies[j].position=Vector(-5+i,0)
		i+=5
		j+=1

def LevleManagerDifficulty():
	global language
	global speedEnemy
	global speedEnemyPatrol
	global patrolPathDistanceEnemy
	
	if (language=="en"):
		msgboxChosseDifficulty=message.show("Choose level difficulty write easy normal hard")
	elif(language=="pl"):
		msgboxChosseDifficulty=message.show("Wybierz poziom trudności wpisująć łatwy normalny trudny ")
		
		
	if (msgboxChosseDifficulty=="easy" or msgboxChosseDifficulty=="łatwy"):
		#Choose EasyDifficulty
		speedEnemy=1
		speedEnemyPatrol=0.5
		patrolPathDistanceEnemy=40
	elif(msgboxChosseDifficulty=="normal" or msgboxChosseDifficulty=="normalny"):
		#Choose NormalDifficulty
		speedEnemy=1.3
		speedEnemyPatrol=0.6
		patrolPathDistanceEnemy=45
	elif(msgboxChosseDifficulty=="hard" or msgboxChosseDifficulty=="trudny"):
		#Choose HardDifficulty
		speedEnemy=1.5
		speedEnemyPatrol=0.7
		patrolPathDistanceEnemy=50
	else:
		LevleManagerDifficulty()
		
def ChceckPlayerLive():
	global livePlayer
	global language
	if (livePlayer==2):
		livePlayer_as_String=str(livePlayer)
		if (language=="en"):
			print(message.show("Only left  : "+livePlayer_as_String+ " lifes"))
		elif (language=="pl"):
			print(message.show("Zostały Ci tylko  : "+livePlayer_as_String+ " życia"))
		game.remove(liveUIs[1])
		BackEnemyToTheBoard()
		player.position=Vector(0,-50)
		player.color=Color(255,128,128)
	elif (livePlayer==1):
		livePlayer_as_String=str(livePlayer)
		if (language=="en"):
			print(message.show("Only left  : "+livePlayer_as_String+ " lifes"))
		elif (language=="pl"):
			print(message.show("Zostały Ci tylko  : "+livePlayer_as_String+ " życia"))
		game.remove(liveUIs[0])
		BackEnemyToTheBoard()	
		player.position=Vector(0,-50)
		player.color=Color(255,211,211)
	elif (livePlayer==0):
		livePlayer_as_String=str(livePlayer)
		if (language=="en"):
			print(message.show("Game Over"))
		elif (language=="pl"):
			print(message.show("Koniec Gry"))		
		game.stop()
			
						
#Tables object (prefabs) in Hierarchy
walls=[]
teleports=[]	
points=[]
enemies=[]
liveUIs=[]

#Lives Player
livePlayer=3

#Value Enemy In Board
VectorSpawnEnemyInBoard=0

#Controlls Enemy 
enemyCreate=0
patrolPathDistanceEnemy=40

#Changer Lvl Vairables
lvlChanger=1
pointcollect=0
pointcollectNextLvl=680

#Declarate Speed Enemy and Player
speedPlayer=2
speedEnemy=1
speedEnemyPatrol=0.5

#Variable gameisOver=False game is running // Variable gameisOver=True game is over 
gameisOver=True
CheckLanguage()

#Variable Check Language Default Language is English //Choose is Polish or English
language="en"

player = Player(Vector(0,-50))				
game.add(player)
game.start()

#PicBlocks Pac-Man Create by Tomasz Jelito ©


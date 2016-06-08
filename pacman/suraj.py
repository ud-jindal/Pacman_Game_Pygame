import pygame 
pygame.init()
gameDisplay = pygame.display.set_mode((1000,1000))
# Different colours
white = (255 , 255 ,255)
black = (0 , 0 , 0)
red = (255 , 0 , 0)
green = (0 , 255 , 0)
lgreen= (100, 255 , 100)
blue= (0,0,255)
yellow=(255,255,0)
back=(0,0,0)
ghost=(51,0,102)
ghost2=(0,51,51)
ghost3=(51,51,0)
dot=(102,255,102)
bound=(0,0,153)

#This functions deals with the background and boundaries that appears on the main screen
def Boundaries():

		gameDisplay.fill(bound , rect=[0 , 0, 1000 ,10])
		gameDisplay.fill(bound , rect=[490 ,10,20 ,115])
		gameDisplay.fill(bound , rect=[50 ,50, 180 ,75])
		gameDisplay.fill(bound , rect=[270 ,50, 180 ,75])
		gameDisplay.fill(bound , rect=[550 , 50, 180 ,75])
		gameDisplay.fill(bound , rect=[770 , 50, 180 ,75])
		gameDisplay.fill(bound , rect=[0 , 50, 10 ,105])
		gameDisplay.fill(bound , rect=[0 , 165, 220 ,315])
		gameDisplay.fill(bound , rect=[260 , 165, 220 ,75])
		gameDisplay.fill(bound , rect=[520 , 165, 220 ,75])
		gameDisplay.fill(bound , rect=[780 , 165, 220 ,315])
		gameDisplay.fill(bound , rect=[990 , 50, 10 ,105])
		gameDisplay.fill(bound , rect=[0 , 990, 1000 ,10])
		gameDisplay.fill(bound , rect=[0 , 835, 10 ,155])
		gameDisplay.fill(bound , rect=[990 , 835, 10 ,155])
		gameDisplay.fill(bound , rect=[0 , 520, 220 ,315])
		gameDisplay.fill(bound , rect=[780 , 520, 220 ,315])
		gameDisplay.fill(bound , rect=[50 , 875, 430 ,75])
		gameDisplay.fill(bound , rect=[520 , 875, 430 ,75])
		gameDisplay.fill(bound , rect=[260 , 240, 75 ,595])
		gameDisplay.fill(bound , rect=[665 , 240, 75 ,595])
		gameDisplay.fill(bound , rect=[335 , 760, 330,75])
		gameDisplay.fill(black , rect=[ 260, 480, 75,40])


#This function displays the fruits on the game screen
def Fruits():

		for i in range(-30,471,5):	
			pygame.draw.circle(gameDisplay, dot, (i,30),1)
		for i in range(530,1030,5):	
			pygame.draw.circle(gameDisplay, dot, (i,30),1)
		for i in range(150,851,5):	
			pygame.draw.circle(gameDisplay, dot, (760,i),1)
		for i in range(150,851,5):	
			pygame.draw.circle(gameDisplay, dot, (240,i),1)
		for i in range(30,971,5):	
			pygame.draw.circle(gameDisplay, dot, (i,145),1)
		for i in range(30,971,5):	
			pygame.draw.circle(gameDisplay, dot, (i,855),1)
		for i in range(30,971,5):	
			pygame.draw.circle(gameDisplay, dot, (i,970),1)
		for i in range(-30,336,5):	
			pygame.draw.circle(gameDisplay, dot, (i,500),1)
		for i in range(760,1030,5):	
			pygame.draw.circle(gameDisplay, dot, (i,500),1)
		for i in range(30,145,5):	
			pygame.draw.circle(gameDisplay, dot, (30,i),1)
		for i in range(30,145,5):	
			pygame.draw.circle(gameDisplay, dot, (250,i),1)
		for i in range(30,145,5):	
			pygame.draw.circle(gameDisplay, dot, (470,i),1)
		for i in range(30,145,5):	
			pygame.draw.circle(gameDisplay, dot, (530,i),1)
		for i in range(30,145,5):	
			pygame.draw.circle(gameDisplay, dot, (750,i),1)
		for i in range(30,145,5):	
			pygame.draw.circle(gameDisplay, dot, (970,i),1)
		for i in range(860,966,5):	
			pygame.draw.circle(gameDisplay, dot, (30,i),1)
		for i in range(860,966,5):	
			pygame.draw.circle(gameDisplay, dot, (500,i),1)
		for i in range(860,966,5):	
			pygame.draw.circle(gameDisplay, dot, (970,i),1)
		for i in range(145,231,5):	
			pygame.draw.circle(gameDisplay, dot, (500,i),1)

# This function defines the pacman eating the  fruits 
def fruit_eat(lst):
	for i in lst:
		pygame.draw.circle(gameDisplay, black, (i[0],i[1]),20)

# This function defines the pacman eating the bonus fruits
def big_eat(lst):
	for i in lst:
		pygame.draw.circle(gameDisplay, black, (i[0],i[1]),20)

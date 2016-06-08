import pygame
import time
import random
from suraj import*
from charan import*
pygame.init()
# Diffrent Colors.
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
size=0
pos=0

#Use To Define No Of Frames Running Per Second.
clock = pygame.time.Clock()

#Its The Main Screen On Which All The Game Is Running.
gameDisplay = pygame.display.set_mode((1000,1000))

#Its The Caption Blits Above The Main Screen. 
pygame.display.set_caption('Pacman')

#Images Loaded Which Are Used In Game.
imgu = pygame.image.load('u.png')
imgl = pygame.image.load('l.png')
imgr = pygame.image.load('r.png')
g1 = pygame.image.load('g1.png')
g2 = pygame.image.load('g2.png')
g3 = pygame.image.load('g3.png')
f1 = pygame.image.load('f1.gif')
f2 = pygame.image.load('f2.gif')
f3 = pygame.image.load('f3.gif')
f4 = pygame.image.load('f4.gif')
f5 = pygame.image.load('f5.gif')

#Used To Set Game Icon.
pygame.display.set_icon(imgr)




# Its The Pause Screen Which Appears When Player Enters The Esc Key
def pause():
	pause = True
	while pause == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					pause = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_r:
					gameloop()
		gameDisplay.fill(white)
		message_to_screen("Paused!!!", red,-300,"large")
		message_to_screen("Continue(c)/Quit(q)/restart(r)" , black )
		pygame.display.update()

# Its The Main Game Loop Which is COntroling The Whole Moition Of Ghosts And Pacman.
def gameloop():
	gameExit = False
	gameover = False

	lead_x = 30
	lead_y = 30
	lead_x_change= 0
	lead_y_change= 0

	c=[]
	d=[]
	for i in range(355,646,5):
		for j in range (260,741,5):
			c.append((i,j))		
	x=imgr
	g1y=280
	g2x=580 
	g3x=375
	g4y=680
	g1c=3
	g2c=-3
	g3c=3
	g4c=-3
	g5x=450
	g5y=10
	g6x=510
	g6y=10
	g5cx=-3
	g5cy=0
	g6cx=3
	g6cy=0
	g7y=835
	g7x=950
	g7cx=-3
	g7cy=0
	#ghosts
	while not gameExit:

		while gameover == True:
			gameDisplay.fill(white)
			message_to_screen("You Made A",red,-220,size="large")
			message_to_screen("Tasty Snack!!!",red,size="large")
			message_to_screen("Score="+str(len(c)-5724),black,200)
			message_to_screen("Restart(c)/Quit(q)",blue,400)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameover=False
					gameExit= True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit= True
						gameover= False
					elif event.key== pygame.K_c:
						gameloop()
				

		prevx=lead_x_change
		prevy=lead_y_change

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_y_change= 0
					lead_x_change-=5
					x=imgl
					if lead_x==240 and 490<lead_y<510 :
						lead_y=500
				elif event.key == pygame.K_RIGHT:
					lead_y_change= 0
					lead_x_change+=5
					x=imgr
					if lead_x==240 and 490<lead_y<510 :
						lead_y=500
					if lead_x==760 and 490<lead_y<510 :
						lead_y=500
				elif event.key == pygame.K_DOWN:
					lead_x_change= 0
					lead_y_change+=5
					x=imgu
					if 230<lead_x<250 and lead_y==500 :
						lead_x=240
					if 750<lead_x<760 and lead_y==500 :
						lead_x=760	 	
				elif event.key == pygame.K_UP:	 
					lead_x_change=0
					lead_y_change-=5
					x=imgu
					if 230<lead_x<250 and lead_y==500 :
						lead_x=240
					if 750<lead_x<760 and lead_y==500 :
						lead_x=760

				elif event.key == pygame.K_ESCAPE:
					pause()

				if event.key == pygame.K_UP and lead_y_change==0:
					lead_y_change = -5
				if event.key == pygame.K_DOWN and lead_y_change==0:
					lead_y_change = 5
				if event.key == pygame.K_RIGHT and lead_x_change==0:
					lead_x_change = 5
				if event.key == pygame.K_LEFT and lead_x_change==0:
					lead_x_change = -5


		if lead_x_change>5:
			lead_x_change=5
		if lead_x_change<-5:
			lead_x_change=-5
		if lead_y_change>5:
			lead_y_change=5
		if lead_y_change<-5:
			lead_y_change=-5			


		if (lead_x>355 and lead_x<435 and lead_y>g1y-20 and lead_y<g1y+60) or (lead_x>g2x-20 and lead_x<g2x+55 and lead_y>260 and lead_y<340) or (lead_x>g3x-20 and lead_x<g3x+60 and lead_y>660 and lead_y<740) or (lead_x>565 and lead_x<645 and lead_y>g4y-20 and lead_y<g4y+60)or(lead_x>g5x-20 and lead_x<g5x+60 and lead_y>g5y-20 and lead_y<g5y+60 )or(lead_x>g6x-20 and lead_x<g6x+60 and lead_y>g6y-20 and lead_y<g6y+60)or(lead_x>g7x-20 and lead_x<g7x+60 and lead_y>g7y-20 and lead_y<g7y+60):
			gameover=True

	
		if lead_x>=1020 and (lead_y== 30 or lead_y== 500) :
			lead_x=0
		if lead_x <=-20 and (lead_y== 30 or lead_y== 500):
			lead_x=1000


		lead_x += lead_x_change
		lead_y += lead_y_change

		trace=trace_path()	
		
		if (lead_x, lead_y) not in trace:
			if (lead_x+5, lead_y) in  trace:
				lead_x+=5
				lead_y_change=prevy
				lead_x_change=0

				#lead_y_change=5
			elif (lead_x-5, lead_y) in  trace:
				lead_x-=5
				lead_y_change=prevy
				lead_x_change=0
				#lead_y_change=5
			elif (lead_x, lead_y+5) in  trace:
				lead_y+=5
				lead_x_change=prevx
				lead_y_change=0

				
			elif (lead_x, lead_y-5) in  trace:
				lead_y-=5
				lead_x_change=prevx
				lead_y_change=0
				


	

		
			elif event.key == pygame.K_RIGHT:
				lead_y=500
				lead_x_change=5


		if g1y <= 280:
			g1c=3
		if g1y >= 460:
			g1c=-3
		if g2x >= 585:
			g2c=-3
		if g2x <= 500:
			g2c=3

		if g3x <= 375:
			g3c=3
		if g3x >= 460:
			g3c=-3

		if g4y >= 680:
			g4c=-3
		if g4y <= 500:
			g4c=3


		if g5y<=10 and g5x <= 10:
			g5cy=3
			g5cx=0
		if g5y>=125 and g5x >= 9:
			g5cy=0
			g5cx=3
		if g5y>=123 and g5x >= 450:
			g5cy=-3
			g5cx=0
		if g5y<=9 and g5x >= 450:
			g5cy=0
			g5cx=-3	


		if g6y<=10 and g6x >= 950:
			g6cy=3
			g6cx=0
		if g6y>=125 and g6x >= 950:
			g6cy=0
			g6cx=-3
		if g6y>=123 and g6x <= 510:
			g6cy=-3
			g6cx=0
		if g6y<=9 and g6x >= 510 and g6x<950:
			g6cy=0
			g6cx=3	        
		

		if g7y<=835 and g7x <= 10:
			g7cy=3
			g7cx=0
		if g7y>=950 and g7x <= 20:
			g7cy=0
			g7cx=3
		if g7y>=950 and g7x >= 950:
			g7cy=-3
			g7cx=0
		if g7y<=835 and g7x >= 950:
			g7cy=0
			g7cx=-3		


		g1y+=g1c
		g2x+=g2c
		g3x+=g3c
		g4y+=g4c
		g5y+=g5cy
		g5x+=g5cx
		g6y+=g6cy
		g6x+=g6cx
		g7y+=g7cy
		g7x+=g7cx
		if (lead_x,lead_y) not in c:
			c.append((lead_x,lead_y))



		gameDisplay.fill(back)
		pygame.draw.circle(gameDisplay, black, (lead_x,lead_y),30)
		Boundaries()
		Fruits()
		
		fruit_eat(c)
		gameDisplay.blit(f1,(490,490))
		if (470<lead_x<530 and 470<lead_y<530):
			d.append((500,500))
			for i in range(1030,1035):
				if (i,i) not in c:
					c.append((i,i))	
		gameDisplay.blit(f2,(385,290))
		if (365<lead_x<425 and 270<lead_y<330):
			d.append((395,300))
			for i in range(1040,1045):
				if (i,i) not in c:
					c.append((i,i))
		gameDisplay.blit(f3,(590,290))
		if (570<lead_x<630 and 270<lead_y<330):
			d.append((600,300))
			for i in range(1050,1055):
				if (i,i) not in c:
					c.append((i,i))
		gameDisplay.blit(f4,(385,690))
		if (365<lead_x<425 and 670<lead_y<730):
			d.append((395,700))
			for i in range(1060,1065):
				if (i,i) not in c:
					c.append((i,i))
		gameDisplay.blit(f5,(595,690))
		if (575<lead_x<635 and 670<lead_y<730):
			d.append((605,700))
			for i in range(1070,1075):
				if (i,i) not in c:
					c.append((i,i))
		big_eat(d)

		score(c)


		gameDisplay.blit(g1,(375,g1y))
		gameDisplay.blit(g2,(g2x,280))
		gameDisplay.blit(g3,(g3x,680))
		gameDisplay.blit(g1,(585,g4y))
		gameDisplay.blit(g1,(g5x,g5y))
		gameDisplay.blit(g2,(g6x,g6y))
		gameDisplay.blit(g2,(g7x,g7y))

		if len(c)== 7126:
			end_game(c)



		pygame.draw.circle(gameDisplay, yellow, (lead_x,lead_y ),20)
		#gameDisplay.blit(x,(lead_x-20,lead_y-20 ))
		
		pygame.display.update()
		clock.tick(45) 

	pygame.quit()
	quit()


# Its The Screen Which Appears On Starting The GAme.
def start_screen():
	play = True
	while  play == True:
		gameDisplay.fill(white)
		message_to_screen("PACMAN",red,-400,"large")
		message_to_screen("You Have To Eat All The Fruits",black,-200)
		message_to_screen("And Make A ",black,-100)
		message_to_screen("High Score!!!",black,size="large")
		message_to_screen("'Beware Of Ghosts They Can Eat You!!'",black,200)

		message_to_screen("p to Enter and q to Exit..", blue, 400)
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				play = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					gameloop()
				elif event.key == pygame.K_q:
					play=False
		pygame.display.update()
	pygame.quit()
	quit()
#start_screen()




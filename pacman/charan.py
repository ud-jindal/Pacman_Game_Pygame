import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1000,1000))
# Differrent colours
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

# Different font sizes and font types
smallfont= pygame.font.SysFont("comicsansms", 50)
medfont= pygame.font.SysFont("comicsansms", 70)
largefont= pygame.font.SysFont("comicsansms", 200)

# This function defines the path the pacman can move. It returns the available co-ordinates into a list
def trace_path():
	a=[]
	for i in range(-30,471,5):
		a.append((i,30))
	for i in range(530,1030,5):
		a.append((i,30))
	for i in range(150,851,5):	
		a.append((760,i))
	for i in range(150,851,5):	
		a.append((240,i))
	for i in range(30,971,5):	
		a.append((i,145))
	for i in range(30,971,5):	
		a.append((i,855))
	for i in range(30,971,5):	
		a.append((i,970))
	for i in range(-30,356,5):	
		a.append((i,500))
	for i in range(760,1030,5):	
		a.append((i,500))
	for i in range(30,145,5):	
		a.append((30,i))
	for i in range(30,145,5):	
		a.append((250,i))
	for i in range(30,145,5):
		a.append((470,i))
	for i in range(30,145,5):	
		a.append((530,i))
	for i in range(30,145,5):	
		a.append((750,i))
	for i in range(30,145,5):	
		a.append((970,i))
	for i in range(860,966,5):	
		a.append((30,i))
	for i in range(860,966,5):	
		a.append((500,i))
	for i in range(860,966,5):	
		a.append((970,i))
	for i in range(145,261,5):	
		a.append((500,i))				
	for i in range(355,646,5):
		for j in range (260,741,5):
			a.append((i,j))
	return a

#The text_objects and message_to_screen are used to blit the sentences
def text_objects(text, color,size):
	if size == "small":
		textSurface = smallfont.render(text , True , color)
	elif size == "med":
		textSurface = medfont.render(text , True , color)
	elif size == "large":
		textSurface = largefont.render(text , True , color)


	return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,pos=0,size="med"):
	textSurf, textRect = text_objects(msg, color,size)
	textRect.center= (500) , (500)+pos
	gameDisplay.blit(textSurf, textRect)

#The pop up screen after completing the gaming , i.e , after winning the game
def end_game(lst):
	play = True
	while  play == True:
		gameDisplay.fill(white)
		message_to_screen("Give A High Five!!",black,-400,)
		message_to_screen("You Win!!",red, -100,size="large")
		message_to_screen("score="+str(len(lst)-5724),black,300)
		message_to_screen("r to restart and q to Exit..", blue, 400)
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				play = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					gameloop()
				elif event.key == pygame.K_q:
					play=False
		pygame.display.update()
	pygame.quit()
	quit() 



#It blits the score on the game screen
def score(lst):
	a=[]
	text= smallfont.render("Score: "+str(len(lst)-5724) , True , white)
	gameDisplay.blit(text, [0,0])

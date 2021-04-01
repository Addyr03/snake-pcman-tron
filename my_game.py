
import pygame 
import time 
import random

pygame.init()

fps = 15
applesize = 20
#change for an esier game
#no hardcodeing
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
dark_blue = (0,0,128)
light_blue =(0,0,100)
yellow = (255,255,0)
display_width = 800
display_height = 600
ten = 10 
#display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("dont touch anything")
#lading snake head in 
img1 = pygame.image.load ("snake1head.png")

#snake
def snake1 (block_size, snake1List):
    gameDisplay.blit(img1,(snake1List[-1][0],snake1List[-1][1]))
    for XnY in snake1List[:-1]:
        pygame.draw.rect(gameDisplay, white , [XnY[0],XnY[1],10,10])

#dead message
font = pygame.font.SysFont(None, 25)


def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/5,display_height/2])

#main loop
def gameLoop():
    gameExit = False
    gameOver = False
    block_size = 10
    clock = pygame.time.Clock ()
    #starting location and makes it move continuly
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    #snake getting longer difine change to 10 makes the snake 10
    snake1List = []
    snake1Length = 1
    #apple starting location
    apple_x1 = round (random.randrange (10, display_width-20)/10.0)*10.0
    apple_y1 = round (random.randrange (10, display_height-20)/10.0)*10.0
    apple_x2 = round (random.randrange (10, display_width-20)/10.0)*10.0
    apple_y2 = round (random.randrange (10, display_height-20)/10.0)*10.0

# set apple to spawn in set locations definded as  >x <y
#location 1 = x between 10,5 and y between 10 ,5
    #game loop
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("uwu you made a oopsie woopsie press C to go again or Q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True 
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if  event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                if  event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width-15 or lead_x <10 or lead_y >= display_height-15 or lead_y < 10:
            gameOver = True
            #hit sides you die



        lead_x += lead_x_change
        lead_y += lead_y_change
 
        #0 , 0 is top left
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, dark_blue, [0,0,800,10])
        pygame.draw.rect(gameDisplay, dark_blue, [0,590,800,10])
        pygame.draw.rect(gameDisplay, dark_blue, [0,0,10,800])
        pygame.draw.rect(gameDisplay, dark_blue, [790,10,10,800])
        #left/right less is left 
        #hight lower is highter 
        #legth 
        # wipth
    
        pygame.draw.rect(gameDisplay, dark_blue, [50,50,10,160])
        pygame.draw.rect(gameDisplay, dark_blue, [740,50,10,160])
        #top left and right 
        
        pygame.draw.rect(gameDisplay, dark_blue, [100,540,600,10])
        pygame.draw.rect(gameDisplay, dark_blue, [100,500,600,10])
        pygame.draw.rect(gameDisplay, dark_blue, [110,510,580,30])
        pygame.draw.rect(gameDisplay, dark_blue, [100,510,10,30])
        pygame.draw.rect(gameDisplay, dark_blue, [690,510,10,30])
        #bottom bar


        bottomleft = pygame.draw.rect(gameDisplay, dark_blue, [50,390,10,160])
        bottomleft
        pygame.draw.rect(gameDisplay, dark_blue, [740,390,10,160])
        #bottom left and right
        
        pygame.draw.rect(gameDisplay, red , [apple_x1,apple_y1,applesize,applesize])
        pygame.draw.rect(gameDisplay, red , [apple_x2,apple_y2,applesize,applesize])
        #apple

        snake1Head = []
        snake1Head.append(lead_x)
        snake1Head.append(lead_y)
        snake1List.append(snake1Head)
        if len (snake1List) > snake1Length:
            del snake1List [0]
        snake1 (block_size, snake1List)
        #smake gettign longer

        pygame.display.update()
 
        #hitting the apple         

        if lead_x >= apple_x1 and lead_x <= apple_x1+applesize-10:
            if lead_y >= apple_y1 and lead_y <= apple_y1+applesize-10 :
                apple_x1 = round (random.randrange (10, display_width-20)/10.0)*10.0
                apple_y1 = round (random.randrange (10, display_height-20)/10.0)*10.0
                snake1Length += 1
        
        if lead_x >= apple_x2 and lead_x <= apple_x2+applesize-10:
            if lead_y >= apple_y2 and lead_y <= apple_y2+applesize-10 :
                apple_x2 = round (random.randrange (10, display_width-20)/10.0)*10.0
                apple_y2 = round (random.randrange (10, display_height-20)/10.0)*10.0
                snake1Length += 1

        clock.tick(fps)
    pygame.quit()
    quit ()

gameLoop()

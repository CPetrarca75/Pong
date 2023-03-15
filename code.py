import pygame
from random import choice

pygame.init()
#Basic Variables
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
barrier_velo = 4
base_velo = 1.5
ball_xvelo = 1.5
ball_yvelo = 1.5
Size_X = 400
Size_Y = 400
Score1 = 0
Score2 = 0
game_state = 0


#Window Init
window = pygame.display.set_mode((Size_X,Size_Y))
pygame.display.set_caption("Pong")
window.fill(black)
#End Window Init

#Object Creation
    #Barrier Init
BarrierSize_Width = 10
BarrierSize_Length = 70
B1_X_Coord = 0
B1_Y_Coord = 165
B2_X_Coord = 390
B2_Y_Coord = 165
B1_Color = (255,0,0)
B2_Color = (0,0,255)

    #Ball Init
BallSize = 20
Ball_X_Coord = 190
Ball_Y_Coord = 190


#ScoreBoard
def pscore(i,j):
        if j == 0:  #Create  0
            if i == 0: #P1 = 0
                pygame.draw.rect(window,white,(100,25,20,5))
                pygame.draw.rect(window,white,(120,25,10,35))
                pygame.draw.rect(window,white,(100,60,30,5))
                pygame.draw.rect(window,white,(100,25,10,35))
            else:   #P2 = 0
                pygame.draw.rect(window,white,(300,25,20,5))  
                pygame.draw.rect(window,white,(320,25,10,35))
                pygame.draw.rect(window,white,(300,60,30,5))
                pygame.draw.rect(window,white,(300,25,10,35))
        if j == 1: #Create 1
            if i == 0:
                pygame.draw.rect(window,white,(100,25,10,35))
            else:
                pygame.draw.rect(window,white,(300,25,10,35))
        if j == 2: #Create 2
            if i ==0:
                pygame.draw.rect(window,white,(100,25,20,5))
                pygame.draw.rect(window,white,(120,25,8,20))
                pygame.draw.rect(window,white,(100,40,20,5))
                pygame.draw.rect(window,white,(100,40,8,15))
                pygame.draw.rect(window,white,(100,55,28,5))
            else:
                pygame.draw.rect(window,white,(300,25,20,5))
                pygame.draw.rect(window,white,(320,25,8,20))
                pygame.draw.rect(window,white,(300,40,20,5))
                pygame.draw.rect(window,white,(300,40,8,15))
                pygame.draw.rect(window,white,(300,55,28,5))
        if j == 3: #Create 3
            if i == 0:
                pygame.draw.rect(window,white,(120,25,5,35))
                pygame.draw.rect(window,white,(100,25,20,5))
                pygame.draw.rect(window,white,(100,40,20,5))
                pygame.draw.rect(window,white,(100,55,20,5))
            else:
                pygame.draw.rect(window,white,(320,25,5,35))
                pygame.draw.rect(window,white,(300,25,20,5))
                pygame.draw.rect(window,white,(300,40,20,5))
                pygame.draw.rect(window,white,(300,55,20,5))
        if j == 4: #Create 4
            if i == 0:
                pygame.draw.rect(window,white,(100,25,5,15))
                pygame.draw.rect(window,white,(100,40,20,5))
                pygame.draw.rect(window,white,(120,25,5,35))
            else:
                pygame.draw.rect(window,white,(300,25,5,15))
                pygame.draw.rect(window,white,(300,40,20,5))
                pygame.draw.rect(window,white,(320,25,5,35))
#Endgame Screen
def endgame():
    global game_state
    global Score1
    global Score2
    window.fill(black)
    pygame.display.update()
    pygame.time.delay(5)
    
    #P
    pygame.draw.rect(window,white,(100,35,5,35))  
    pygame.draw.rect(window,white,(105,35,20,5))
    pygame.draw.rect(window,white,(105,50,20,5))
    pygame.draw.rect(window,white,(120,35,5,20))
    if Score1 == 5:
        #1
        pygame.draw.rect(window,white,(140,35,5,35))
    if Score2== 5:
        #2
            pygame.draw.rect(window,white,(140,35,10,5))
            pygame.draw.rect(window,white,(150,35,5,15))
            pygame.draw.rect(window,white,(140,50,15,5))
            pygame.draw.rect(window,white,(140,55,5,10))
            pygame.draw.rect(window,white,(140,65,15,5))
    #W
    pygame.draw.rect(window,white,(170,35,5,30))
    pygame.draw.rect(window,white,(175,65,10,5))
    pygame.draw.rect(window,white,(185,35,5,30))
    pygame.draw.rect(window,white,(190,65,10,5))
    pygame.draw.rect(window,white,(200,35,5,30))
    #I
    pygame.draw.rect(window,white,(220,35,5,35))
    #N
    pygame.draw.rect(window,white,(240,35,5,35))
    pygame.draw.rect(window,white,(260,35,5,35))
    i = 0
    j=0
    while j < 3:
        pygame.draw.rect(window,white,(245+i,45+i,5,5))
        i+=5
        j+=1
    #S
    pygame.draw.rect(window,white,(285,35,20,5))
    pygame.draw.rect(window,white,(285,50,15,5))
    pygame.draw.rect(window,white,(280,65,20,5))
    pygame.draw.rect(window,white,(280,40,5,10))
    pygame.draw.rect(window,white,(300,55,5,10))

    pygame.display.update()
    pygame.time.delay(1000)
    pygame.display.update()

    restart_screen()
    

def cont():
    global game_state
    # game_state = 0
    # return
    global game_state
    global Score1
    global Score2
    flash  = 0
    select = 1  
    blink = True
    while blink:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game_state = 2
                return
        keys = pygame.key.get_pressed()
        pygame.event.pump() #Necessary to register key presses
        if select == 0:
            pygame.draw.rect(window,white,(140,240,127,55),2)
            if keys[pygame.K_SPACE]:
                    game_state = 0
                    Score1 = 0
                    Score2 = 0
                    return
            if keys[pygame.K_DOWN]:
                    select = 1
                    #pygame.time.delay(1)
                    #pygame.display.update()
                    flash = 0
                    continue
            if flash >= 0:    
                if flash == 2000:
                    flash *= -1
                pygame.draw.rect(window,white,(70,160,257,55),2)
                flash +=1
                pygame.display.update()
            if flash < 0:
                pygame.draw.rect(window,black,(70,160,257,55),2)
                flash +=1
                pygame.display.update()

        if select == 1:
            pygame.draw.rect(window,white,(70,160,257,55),2)
            if keys[pygame.K_SPACE]:
                    game_state = 2 
                    return
            if keys[pygame.K_UP]:
                    select = 0
                    #pygame.time.delay(1)
                    pygame.display.update()
                    flash = 0
                    continue
            if flash >= 0:
                if flash == 2000:
                    flash *= -1
                pygame.draw.rect(window,white,(140,240,127,55),2)
                flash +=1
                pygame.display.update()
            if flash < 0:
                pygame.draw.rect(window,black,(140,240,127,55),2)
                flash +=1
                pygame.display.update()
            
                



def restart_screen():
    global game_state
    
    #Restart
    #R
    pygame.draw.rect(window,white,(80,170,5,35))
    pygame.draw.rect(window,white,(80,170,15,5))
    pygame.draw.rect(window,white,(95,175,5,10))
    i = 0
    j=0
    while j < 4:
        pygame.draw.rect(window,white,(80+i,185+i,5,5))
        i+=5
        j+=1
    pygame.draw.rect(window,white,(80,185,15,5))
    #E
    pygame.draw.rect(window,white,(110,170,5,30))
    pygame.draw.rect(window,white,(110,170,20,5))
    pygame.draw.rect(window,white,(110,185,20,5))
    pygame.draw.rect(window,white,(110,200,20,5))
    #S
    pygame.draw.rect(window,white,(145,170,20,5))
    pygame.draw.rect(window,white,(145,185,15,5))
    pygame.draw.rect(window,white,(140,200,20,5))
    pygame.draw.rect(window,white,(140,175,5,10))
    pygame.draw.rect(window,white,(160,190,5,10))
    #T
    pygame.draw.rect(window,white,(175,170,30,5))
    pygame.draw.rect(window,white,(187,175,6,30))
    #A
    pygame.draw.rect(window,white,(215,175,5,30))
    pygame.draw.rect(window,white,(240,175,5,30))
    pygame.draw.rect(window,white,(220,170,20,5))
    pygame.draw.rect(window,white,(220,185,20,5))
    #R
    pygame.draw.rect(window,white,(255,170,5,35))
    pygame.draw.rect(window,white,(255,170,15,5))
    pygame.draw.rect(window,white,(270,175,5,10))
    i = 0
    j=0
    while j < 4:
        pygame.draw.rect(window,white,(255+i,185+i,5,5))
        i+=5
        j+=1
    pygame.draw.rect(window,white,(255,185,15,5))
    #T
    pygame.draw.rect(window,white,(285,170,30,5))
    pygame.draw.rect(window,white,(297,175,6,30))
    #Box        
    pygame.draw.rect(window,white,(70,160,257,55),2)
    
    
    #Exit

    #E
    pygame.draw.rect(window,white,(150,250,5,30))
    pygame.draw.rect(window,white,(150,250,20,5))
    pygame.draw.rect(window,white,(150,265,20,5))
    pygame.draw.rect(window,white,(150,280,20,5))
    #X
    pygame.draw.rect(window,white,(180,250,5,10))
    pygame.draw.rect(window,white,(180,280,5,5))
    pygame.draw.rect(window,white,(200,250,5,10))
    pygame.draw.rect(window,white,(200,280,5,5))
    x_c = 0
    x = 0
    while x_c < 4:
        pygame.draw.rect(window,white,(185+x,260+x,5,5))
        pygame.draw.rect(window,white,(195-x,260+x,5,5))
        x += 5
        x_c += 1
    #I
    pygame.draw.rect(window,white,(215,250,5,35))
    #T
    pygame.draw.rect(window,white,(230,250,30,5))
    pygame.draw.rect(window,white,(242,255,6,30))
    #Border
    pygame.draw.rect(window,white,(140,240,127,55),2)
    pygame.display.update() 
    cont()
    


        
            

def main_game():

    #help move objects
    #Object Creation
    #Barrier Init
    global BarrierSize_Width 
    global BarrierSize_Length 
    global B1_X_Coord 
    global B1_Y_Coord 
    global B2_X_Coord 
    global B2_Y_Coord
    global barrier_velo
    global B1_Color 
    global B2_Color 
    global Score1
    global Score2
    global game_state

        #Ball Init
    global BallSize
    global Ball_X_Coord 
    global Ball_Y_Coord 
    global ball_xvelo
    global ball_yvelo
    global base_velo
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game_state = 2
                return
        pygame.time.delay(10) #Necesary to keep game at stable pace
        Ball_X_Coord += ball_xvelo
        Ball_Y_Coord += ball_yvelo
        ball_xvelo *= 1.0005
        ball_yvelo *= 1.0005
        
        keys = pygame.key.get_pressed()
        pygame.event.pump() #Necessary to register key presses
        if keys[pygame.K_UP] and B2_Y_Coord > 0:
            B2_Y_Coord -= barrier_velo
        
        if keys[pygame.K_w] and B1_Y_Coord > 0:
            B1_Y_Coord -= barrier_velo

        if keys[pygame.K_DOWN] and B2_Y_Coord < Size_Y-BarrierSize_Length:
            B2_Y_Coord += barrier_velo

        if keys[pygame.K_s] and B1_Y_Coord < Size_Y-BarrierSize_Length:
            B1_Y_Coord += barrier_velo

        #Need to Continually Fill back the space as thepreviously created drawing stays
        window.fill((0,0,0))

        #Initial Creation of Objects
        Barrier_1 = pygame.draw.rect(window,B1_Color,(B1_X_Coord,B1_Y_Coord,BarrierSize_Width,BarrierSize_Length))
        Barrier_2 = pygame.draw.rect(window,B2_Color,(B2_X_Coord,B2_Y_Coord,BarrierSize_Width,BarrierSize_Length))
        Ball = pygame.draw.rect(window,white,(Ball_X_Coord,Ball_Y_Coord,BallSize,BallSize))

        #Ball Collision
        Ball_Collide = Ball.colliderect(Barrier_1) or Ball.colliderect(Barrier_2)

        #Ball Restart:
        if Ball_X_Coord < -25  or Ball_X_Coord + BallSize > 425:
            if Ball_X_Coord < -25:
                Score2 += 1 #Right Side
            else:
                Score1 += 1 #Right Side
            Ball_X_Coord = 190
            Ball_Y_Coord = 190
            pygame.time.wait(100)
            pygame.display.update()
            ball_yvelo = base_velo * choice([-1,1])
            ball_xvelo = base_velo * choice([-1,1])
            pscore(0,Score1) #Updating player 1 score (Left Side)
            pscore(1,Score2) #Updating Player 2 score (Right Side)
            pygame.display.update()
            #CREATE A SECOND BOX TAHT IS ONLY VISIBILE WHILE THE PAUSE OCCURS THEN REMOVE IT WHEN PAUSE ENDS 
            if Score1 == 5 or Score2 == 5:
                game_state = 1
                return

        if(Ball_X_Coord == 190 and Ball_Y_Coord == 190 and (Score1+Score2 >=0)):
            pygame.time.wait(500)
            
        #Ball Collision in Play    
        if Ball_Collide:
                if Ball_X_Coord < 380 or Ball_X_Coord > 20: 
                    ball_xvelo = -ball_xvelo
                    if abs(ball_xvelo) > 3.5:
                        ball_xvelo = ball_xvelo * choice([.6,.8,.9,1.01,1.05,1.3])
                        ball_yvelo = ball_yvelo * choice([.5,.75,1,1.25,1.5]) 
                    else:
                        ball_xvelo = ball_xvelo * choice([1,1.05,1.35,1.5])
                        ball_yvelo = ball_yvelo * choice([1,1.05,1.35,1.5])
                    
                
        
        if Ball_Y_Coord > 400 - BallSize or Ball_Y_Coord < 0:
            ball_yvelo = -ball_yvelo


#NEED TO ADJUST THE X COLLIDE OF THE BALL
        pygame.display.update()

running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    if game_state == 0:
        main_game()
    elif game_state == 1:
        endgame()
    else:
        running = False




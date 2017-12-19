# Snake Game

# game imports
import pygame, sys, random, time



check_errors = pygame.init()

# check for initializing errors
if (check_errors[1]):
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")
    #sys.exit(5)



# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game")
#time.sleep(2)


# Colors
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0, 255, 0) #snake color 1
darkGreen = pygame.Color(0, 102, 0) #snake color 2
black = pygame.Color(0, 0, 0)   #score
white = pygame.Color(255, 255, 255) #background 1
blue = pygame.Color(153, 255, 255) #background 2
brown = pygame.Color(165, 42, 42)   #food


# FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = "RIGHT"
changeto = direction

score = 0

# Game over function
def gameOver():
    myFont = pygame.font.SysFont("monaco", 72)
    GOsurf = myFont.render("Game Over!", True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit() #piygame exit
    sys.exit() #console exit   or just quit()

# Score function
def showScore(choice=1):
    scoreFont = pygame.font.SysFont("monaco", 40)
    scoreSurf = scoreFont.render("Score: {0}".format(score), True, black)
    scoreRect = scoreSurf.get_rect()
    if choice == 1:
        scoreRect.midtop = (80, 10)
    else:
        scoreRect.midtop = (360, 120)
    playSurface.blit(scoreSurf, scoreRect)
    #pygame.display.flip()

# Game intro

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))


        playSurface.fill(white)
        largeText = pygame.font.SysFont("monaco", 115)
        TextSurf = largeText.render("Snake Game", True, green)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((720/2), (460/2))
        playSurface.blit(TextSurf, TextRect)
        pygame.display.flip() #same as .flip()
        fpsController.tick(15)






# Main Logic of the game

while 1:

    #gameIntro()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                changeto = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                changeto = "LEFT"
            if event.key == pygame.K_UP or event.key == ord("w"):
                changeto = "UP"
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                changeto = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                #pygame.quit()
                #sys.exit(10)


    # validation of direction
    if changeto == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeto == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeto == "DOWN" and not direction == "UP":
        direction = "DOWN"

    # update snake position [x,y]
    if direction == "RIGHT":
        snakePos[0] += 10
    if direction == "LEFT":
        snakePos[0] -= 10
    if direction == "UP":
        snakePos[1] -= 10
    if direction == "DOWN":
        snakePos[1] += 10

    # snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    # Food spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playSurface.fill(blue)

    # Drawing the snake
    for pos in snakeBody[1::2]:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10)) #drawing the snake, rendering
    for pos in snakeBody[0::2]:
        pygame.draw.rect(playSurface, darkGreen, pygame.Rect(pos[0], pos[1], 10, 10)) #drawing the snake, rendering

    # Drawing the food
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10)) #drawing the food, rendering

    # Boundaries
    if (snakePos[0] < 0 or snakePos[0] > 710) or (snakePos[1] < 0 or snakePos[1] > 450): #boundaries are lowered by 10 so that only the head of the snake is able to go out of the screen before game over
        gameOver()

    # if snake eats itself
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()

    fpsController.tick(20) #game speed








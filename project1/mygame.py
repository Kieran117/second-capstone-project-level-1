
#layout concept is taken from the example provided and added my own extra elements to it
#images used are from the folder that they were provided in
import pygame
import random

pygame.init()

#selecting my own screen height and width to have the game displayed on

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

#assigning the images to the vraiable names
player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

#getting the respective measurements of the respective variables
image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

#assinging the images (variables) their place in the game screen
playerXPosition = 100
playerYPosition = 50


enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

#assigning keyboard inputs boolean values
keyUp = False
keyDown = False
keyLeft = False
keyRight = False
Youwin = False
Youlose = False

while 1:

#making sure that the images will load onto the game screen so that we can see them
    screen.fill(0)
    screen.blit(player,  (playerXPosition, playerYPosition))
    screen.blit(enemy,  (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()



    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


        if event.type == pygame.KEYDOWN:      #this will determine if the user inputs should move the player image according to the input


            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        if event.type == pygame.KEYUP:


            if event.key == pygame.K_UP:     #if the inputs are false then no action will occur with the player image
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False


    if keyUp == True:  # if the input is determined to be true then the player will move dependent on what the input is
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1


     #giving the player and enemy their own collision box so we can tell if they hit each other
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition


    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition


    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition


    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition


    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition


    #giving an action the the player collides with any of the enemy hit boxes
    if playerBox.colliderect(enemyBox):
        Youlose = True

    if playerBox.colliderect(enemy2Box):
        Youlose = True

    if playerBox.colliderect(enemy3Box):
        Youlose = True

    if playerBox.colliderect(prizeBox):
        Youwin = True

    if Youwin:
        print("You win!")

        pygame.quit()
        exit(0)


    if Youlose:
        print("You lose!")

        pygame.quit()
        exit(0)



    #if all the enemy players go off the screen the player wins
    if enemyXPosition < 0 - enemy_width and enemy2XPosition < 0 - enemy2_width and enemy3XPosition < 0 - enemy3_width:
        print("You win!")

        pygame.quit()
        exit(0)
            

   #giving the objects an amount to move towards the player
    enemyXPosition -= 0.80
    enemy2XPosition -= 0.60
    enemy3XPosition -= 0.40
    prizeXPosition -= 0.20


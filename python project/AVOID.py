# A.VOID game coded by Puya Mirkarimi for an EPQ project in 2015

import pygame
import math
import time
from random import randint

# Define colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# Load images
startScreen = pygame.image.load("startScreen.jpg")
background = pygame.image.load("background.jpg")
gameOverScreen = pygame.image.load("gameOver.jpg")
playerU = pygame.image.load("player.png")
playerU.set_colorkey(BLACK)                         # Set black to transparent for player image
playerR = pygame.image.load("playerR.png")
playerR.set_colorkey(BLACK)
playerD = pygame.image.load("playerD.png")
playerD.set_colorkey(BLACK)
playerL = pygame.image.load("playerL.png")
playerL.set_colorkey(BLACK)
asteroidImage = pygame.image.load("asteroid.png")
asteroidImage.set_colorkey(BLACK)                       # Set black to transparent for asteroidImage
death01 = pygame.image.load("death01.png")
death02 = pygame.image.load("death02.png")
death03 = pygame.image.load("death03.png")
death04 = pygame.image.load("death04.png")
death05 = pygame.image.load("death05.png")
death06 = pygame.image.load("death06.png")
death07 = pygame.image.load("death07.png")
death08 = pygame.image.load("death08.png")


# Setup
pygame.init()

# Set the width and height of the screen [width, height]
windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)

pygame.display.set_caption("A.VOID")

running = True
count = 0
score = 0
difficulty = 100
font = pygame.font.SysFont('Verdana', 23)
scoreText = font.render(str(0), True, WHITE)
gameStarted = False
gameOver = False
spacePressed = False
upPressed = False
rightPressed = False
downPressed = False
leftPressed = False
playerAlive = True
playerX = 380
playerY = 280
deltaX = 0
deltaY = -2
rotation = "U"
asteroidsUp = []
asteroidsRight = []
asteroidsDown = []
asteroidsLeft = []


# Set the screen update rate
clock = pygame.time.Clock()

# --- Functions
def start_screen():
    # Draws starting screen
    screen.blit(startScreen, [0, 0])

def draw_player(x, y):
    # Draws player in position and correct rotation
    if rotation == "R":
        screen.blit(playerR, [x, y])
    elif rotation == "L":
        screen.blit(playerL, [x, y])
    elif rotation == "U":
        screen.blit(playerU, [x, y])
    elif rotation == "D":
        screen.blit(playerD, [x, y])


def player_death():
    # Player explosion animation
    screen.blit(death01, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.3)

    screen.blit(death02, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.3)

    screen.blit(death03, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.3)

    screen.blit(death04, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.3)

    screen.blit(death05, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.3)

    screen.blit(death06, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.3)

    screen.blit(death07, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.3)

    screen.blit(death08, [playerX, playerY])
    pygame.display.flip()
    time.sleep(0.8)

def draw_asteroid(x, y):
    # Draw asteroid in position
    screen.blit(asteroidImage, [x, y])

def collided(x, y, asteroid_x, asteroid_y):
    # Collision detection with asteroids
    if asteroid_x + 20 > x > asteroid_x and asteroid_y + 20 > y > asteroid_y:
        return True
    if x + 40 > asteroid_x > x and y + 40 > asteroid_y > y:
        return True
    if x + 40 > asteroid_x > x and asteroid_y + 20 > y > asteroid_y:
        return True
    if asteroid_x + 20 > x > asteroid_x and y + 40 > asteroid_y > y:
        return True
    # Collision detection with edge of screen
    if x <= 0 or x >= 760 or y <= 0 or y >= 560:
        return True
    return False

def game_over():
    # Final screen
    screen.blit(gameOverScreen, [0, 0])     # Display game over screen
    final_score = font.render("You scored: " + str(score), True, WHITE)
    screen.blit(final_score, [307, 350])



# -------- Main Program Loop -----------
while running:
    # --- EVENT PROCESSING
    for event in pygame.event.get():        # If user did something
        if event.type == pygame.QUIT:       # If user clicked close
            running = False                 # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:    # User pressed down a key
            if event.key == pygame.K_SPACE:
                spacePressed = True         # Space pressed
            if event.key == pygame.K_UP:
                upPressed = True            # Up pressed
                rotation = "U"
            if event.key == pygame.K_RIGHT:
                rightPressed = True         # Right pressed
                rotation = "R"
            if event.key == pygame.K_DOWN:
                downPressed = True          # Down pressed
                rotation = "D"
            if event.key == pygame.K_LEFT:
                leftPressed = True          # Left pressed
                rotation = "L"

        if event.type == pygame.KEYUP:      # User let go of a key
            if event.key == pygame.K_SPACE:
                spacePressed = False        # Space not pressed
            if event.key == pygame.K_UP:
                upPressed = False           # Up not pressed
            if event.key == pygame.K_RIGHT:
                rightPressed = False        # Right not pressed
            if event.key == pygame.K_DOWN:
                downPressed = False         # Down not pressed
            if event.key == pygame.K_LEFT:
                leftPressed = False         # Deft not pressed

    # --- GAME LOGIC

    if not gameStarted:
        # Title screen
        if spacePressed:
            gameStarted = True
    else:
        # Game started
        if playerAlive:
            # Player is alive
            count += 1
            score = int(math.floor(count / 100)) * 10
            scoreText = font.render(str(score), True, WHITE)

            if int(count / difficulty) == count / difficulty:     # Every 'difficulty' counts
                # Spawn an asteroid
                side = randint(1, 4)
                if side == 1:
                    asteroidsUp.append([(randint(1, 15) * 50) - 10, -20])
                elif side == 2:
                    asteroidsRight.append([820, (randint(1, 11) * 50) - 10])
                elif side == 3:
                    asteroidsDown.append([(randint(1, 15) * 50) - 10, 600])
                elif side == 4:
                    asteroidsLeft.append([0, (randint(1, 11) * 50) - 10])

            # Check if any asteroids have collided with the player
            for i in range(len(asteroidsUp)):
                if collided(playerX, playerY, asteroidsUp[i][0], asteroidsUp[i][1]):
                    playerAlive = False
            for i in range(len(asteroidsRight)):
                if collided(playerX, playerY, asteroidsRight[i][0], asteroidsRight[i][1]):
                    playerAlive = False
            for i in range(len(asteroidsDown)):
                if collided(playerX, playerY, asteroidsDown[i][0], asteroidsDown[i][1]):
                    playerAlive = False
            for i in range(len(asteroidsLeft)):
                if collided(playerX, playerY, asteroidsLeft[i][0], asteroidsLeft[i][1]):
                    playerAlive = False

            # Update asteroid positions
            for i in range(len(asteroidsUp)):
                asteroidsUp[i][1] += 2
            for i in range(len(asteroidsRight)):
                asteroidsRight[i][0] -= 2
            for i in range(len(asteroidsDown)):
                asteroidsDown[i][1] -= 2
            for i in range(len(asteroidsLeft)):
                asteroidsLeft[i][0] += 2

            # Calculate player velocity
            if rightPressed:
                deltaX = 2
                deltaY = 0
            elif leftPressed:
                deltaX = -2
                deltaY = 0
            elif upPressed:
                deltaX = 0
                deltaY = -2
            elif downPressed:
                deltaX = 0
                deltaY = 2

            # Update player position
            playerX += deltaX
            playerY += deltaY

            if int(count / 250) == count / 250 and difficulty > 10:      # Make game harder as time moves on
                difficulty -= 5

        else:
            # Player has died
            a = 1

    # --- DRAWING CODE
    screen.blit(background, [0, 0])         # Clear screen to background

    # Start of drawing commands
    if not gameStarted:
        # Title screen
        start_screen()
    else:
        # Game started
        if playerAlive:
            # Player is alive
            draw_player(playerX, playerY)           # Draw player in position

            for i in range(len(asteroidsUp)):       # Draw asteroids in position
                draw_asteroid(asteroidsUp[i][0], asteroidsUp[i][1])
            for i in range(len(asteroidsRight)):
                draw_asteroid(asteroidsRight[i][0], asteroidsRight[i][1])
            for i in range(len(asteroidsDown)):
                draw_asteroid(asteroidsDown[i][0], asteroidsDown[i][1])
            for i in range(len(asteroidsLeft)):
                draw_asteroid(asteroidsLeft[i][0], asteroidsLeft[i][1])

            screen.blit(scoreText, [50, 550])       # Draw score on bottom left of screen
        else:
            # Player has died
            if not gameOver:
                player_death()
                gameOver = True
            if not spacePressed:
                game_over()
            else:
                running = False

    # End of drawing commands
    pygame.display.flip()                           # Update Screen

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()

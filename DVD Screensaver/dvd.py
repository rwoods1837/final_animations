#Ryan Woods
#2/1/18
#DVD Screensaver
#gold dvd is 75x34 pixels
#blue dvd is 75x43 pixels
#nick cage is 75x93 pixels

# Imports
import pygame

# Initialize game engine
pygame.init()

#image
dvd = pygame.image.load('bluedvd.png')

# Window
SIZE = (800, 600)
TITLE = "DVD Screensavers"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Sound Effects
pygame.mixer.music.load("elevator.ogg")

# Block
loc = [380, 280]
vel = [0, 0]
speed = 1

def draw_block(loc):
    x = loc[0]
    y = loc[1]
    
    screen.blit(dvd, (x,y))
    
# Game loop
pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vel[0] = 1
                vel[1] = 1        
        
    # Game logic
    loc[0] += vel[0]
    loc[1] += vel[1]
    
    if  loc[0] <= 0 or loc[0] >= 725:
        vel[0] = -1 * vel[0]
            
    elif  loc[1] <= 0 or loc[1] >= 557:
        vel[1] = -1 * vel[1]
    
    # Drawing code
    screen.fill(BLACK)
    draw_block(loc)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

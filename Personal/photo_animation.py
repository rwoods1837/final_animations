# Computer Programming 1
# im trying
# ryan woods
# a picture I TOOK with clouds in the back

# Imports
import pygame
import random

# Initialize game engine
pygame.init()
from pygame.locals import*
# Window
SIZE = (400, 600)
TITLE = "Photo-Animation"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
sky = pygame.image.load('imgs/IMG_7777.png')
# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)

# Make clouds
num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 800)
    y = random.randrange(-50, 400)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

pygame.mixer.music.load("songs/minecraft.ogg")
   
# Game loop
pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] -= 2

        if c[0] < -100:
           c[0] = random.randrange(400, 800)
           c[1] = random.randrange(-50, 400)
             
    # Drawing code
    '''background'''
    screen.fill(BLUE)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    '''sky'''
    screen.blit(sky, (0,0))

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

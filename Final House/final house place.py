# Computer Programming 1
# Pygame Graphics 
#
# The Final

# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "The Best Animation of All"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BROWN = (107, 69, 9)
YELLOW = (255, 208, 0)
GREY = (181, 170, 157)
LIGHTGREEN = (142, 222, 39)
DARKGREEN = (93, 120, 1)
LIGHTGREY = (195, 195, 195)
MOONSUN = (244, 255, 168)

#settings
sticky = True
lightning = False
'''make ground'''
ground = pygame.Surface([800, 200])
ground.fill(DARKGREEN)

def moon(a, b):
    pygame.draw.ellipse(screen, MOONSUN, [a, b, 100, 100])

def fence():
    y = 380
    for x in range(5, 800, 30):
        post = ([x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5])
        pygame.draw.polygon(screen, BROWN, post)

    pygame.draw.rect(screen, BROWN, [0, y+10, 800, 5])
    pygame.draw.rect(screen, BROWN, [0, y+30, 800, 5])

def house():
    pygame.draw.rect(screen, RED, [340, 265, 160, 140])
    pygame.draw.polygon(screen, BROWN, [[420, 185], [330,265], [510, 265]])
    window = pygame.draw.rect(screen, BLUE, [360, 305, 40, 40])
    pygame.draw.rect(screen, BROWN, [420, 325, 40, 80])

def trees(w, x, y, z):
    pygame.draw.rect(screen, BROWN, [w, x, 40, 160])
    pygame.draw.ellipse(screen, DARKGREEN, [y, z, 120, 140])

def snowman(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 20, 20])
    pygame.draw.ellipse(screen, WHITE, [x - 5, y + 15, 30, 30])
    pygame.draw.ellipse(screen, WHITE, [x - 10, y + 30, 40, 40])

def make_snow(flake):
    rect = flake[:4]
    pygame.draw.ellipse(screen, WHITE, rect)

def cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, LIGHTGREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, LIGHTGREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, LIGHTGREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, LIGHTGREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, LIGHTGREY, [x + 20, y + 20, 60, 40])

#make snow
num_flakes = 700
snow = []


# Sound Effects
pygame.mixer.music.load("minecraft.ogg")
thunder = pygame.mixer.Sound("thunder.ogg")

# Game loop
pygame.mixer.music.play(-1)

for i in range(num_flakes):
    x = random.randrange(-100, 900)
    y = random.randrange(-100, 600)
    r = random.randrange(4, 7)
    stop = random.randrange(400, 625)
    flake = [x, y, r, r, stop]
    snow.append(flake)
    
# Make farclouds
num_farclouds = 10
farclouds = []
for i in range(num_farclouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 100)
    speed = random.randrange(-5,-3)
    loc = [x, y, speed]
    farclouds.append(loc)

num_nearclouds = 10
nearclouds = []
for i in range(num_nearclouds):
    x = random.randrange(-800, 800)
    y = random.randrange(200, 340)
    speed = random.randrange(-2,-1)
    loc = [x, y, speed]
    nearclouds.append(loc)
    
# Game loop
done = False
daytime = True
lights_on = False


while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_BACKSPACE:
                lightning = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                lightning = False
                thunder.play()
        
                

    # Game logic
    for c in farclouds:
        c[0] -= c[2]

        if c[0] > 800:
           c[0] = random.randrange(-800, -100)
           c[1] = random.randrange(-50, 100)

    for n in nearclouds:
        n[0] -= n[2]

        if n[0] > 800:
           n[0] = random.randrange(-800, -100)
           n[1] = random.randrange(200, 340)

    for s in snow:
        s[0] += random.randrange(-1, 2)
        s[1] += random.randrange(1, 2)

        if s[1] >= s[4]:
            if sticky:
                pygame.draw.ellipse(ground, WHITE, [s[0], s[1] - 402, s[3], s[3]])

            s[0] = random.randrange(-100, 900)
            s[1] = random.randrange(-100, 0)

        

    # Drawing code

   
    '''sky'''
    if daytime:
        sky = GREY
    else:
        sky = BLACK
    
    if lightning == True:
        screen.fill(YELLOW)
    else:
        screen.fill(sky)

    '''nearclouds'''
    for n in nearclouds:
        cloud(n)
        
    ''' moon '''
    moon(660, 20)
    
    ''' grass '''
    #pygame.draw.rect(screen, DARKGREEN, [0, 400, 800, 200])
    screen.blit(ground, [0,400])

    '''house'''
    house()
    if lights_on == True:
        window = pygame.draw.rect(screen, YELLOW, [360, 305, 40, 40])
    elif lights_on == False:
        window = pygame.draw.rect(screen, BLUE, [360, 305, 40, 40])

    '''bushes'''

    pygame.draw.ellipse(screen, DARKGREEN, [600, 265, 30, 140])
    pygame.draw.ellipse(screen, DARKGREEN, [650, 265, 30, 140])
    pygame.draw.ellipse(screen, DARKGREEN, [700, 265, 30, 140])
    pygame.draw.ellipse(screen, DARKGREEN, [750, 265, 30, 140])
    
    ''' fence '''
    fence()

    '''trees'''
    trees(50, 300, 10, 200)
    ''' snowmen '''
    
    
    ''' snow '''
    for s in snow:
        make_snow(s)

    ''' farclouds '''
    for c in farclouds:
        cloud(c)

        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

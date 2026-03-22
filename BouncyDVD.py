# First game with Pygame
# Sept 23, 2023

import sys, pygame, random
pygame.init()

size = width, height = 960, 540
speed = [150, 150]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing DVD!")
clock = pygame.time.Clock()

dvd_colors = ["assets/cyandvd.png", "assets/yellowdvd.png", "assets/greendvd.png", "assets/magentadvd.png"]
dvd = pygame.image.load(random.choice(dvd_colors)).convert_alpha()
dvdrect = dvd.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    dt = clock.tick(60)/1000
    dvdrect.x += speed[0] * dt
    dvdrect.y += speed[1] * dt
    if dvdrect.left < 0 or dvdrect.right > width:
        speed[0] = -speed[0]
        dvd = pygame.image.load(random.choice(dvd_colors)).convert_alpha()
    if dvdrect.top < 0 or dvdrect.bottom > height:
        speed[1] = -speed[1]
        dvd = pygame.image.load(random.choice(dvd_colors)).convert_alpha()

    screen.fill(black)
    
    screen.blit(dvd, dvdrect)
    pygame.display.update()
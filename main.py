import pygame
from pygame.locals import *
from body import Body
import time
import sys
import pygame.font
import random

WIDTH, HEIGHT = 640 *2, 480*2
CHAOS = False
include_jupiter = True
jupiter_close = True
jupiter_heavier = True


#one frame is 1 second
FPS = 60


def main():
    t = 0

    sun_pos = (0, 0)
    sun_v = (0, 0)
    sun_mass = 1.9885*(10**30)
    sun_radius = 30
    sun_color = (255, 255, 0)
    sun = Body(sun_pos, sun_v, sun_mass, sun_radius, sun_color)

    earth_pos = (1.496*(10**8)*1000, 0)
    earth_v = (0, 107200 * 0.277777778)
    earth_mass = 5.972168*(10**24)
    earth_radius = 10
    earth_color = (0, 0, 255)
    earth = Body(earth_pos, earth_v, earth_mass, earth_radius, earth_color)

    moon_pos = (1.496*(10**8)*1000 + 384400 * 1000 + (10**10), 0)
    moon_v = (0, 107200 * 0.277777778 + 1023)
    moon_mass = 7.34767309 * (10**22)
    moon_radius = 3
    moon_color = (200, 200, 200)
    moon = Body(moon_pos, moon_v, moon_mass, moon_radius, moon_color)

    #stores the bodys in a list
    bodys = []
    bodys.append(sun)
    bodys.append(earth)
    pygame.init()
    pygame.font.init()
    bodys.append(moon)

    if include_jupiter:
        if jupiter_close:
            jupiter_pos = (778000000*500, 0)
        else:
            jupiter_pos = (778000000*1000, 0)
        jupiter_v = (0, 47051 * 0.277777778)
        if jupiter_heavier:
            jupiter_mass = (1898.13 * 10 ** 25)
        else:
            jupiter_mass = (1898.13 * 10**24)
        jupiter_radius = 15
        jupiter_color = (151, 134, 94)
        jupiter = Body(jupiter_pos, jupiter_v, jupiter_mass, jupiter_radius, jupiter_color)
        bodys.append(jupiter)

    if CHAOS:
        for i in range(20):
            rand_pos = (random.randint(-10**10, 10**10), random.randint(-10**10, 10**10))
            rand_vel = (random.randint(-10**1, 10**1), random.randint(-10**1, 10**1))
            rand_mass = random.randint(10**20, 10**25)
            rand_radius = random.randint(1, 10)
            rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            temp_body = Body(rand_pos, rand_vel, rand_mass, rand_radius, rand_color)
            bodys.append(temp_body)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    last_frame = time.time()
    font = pygame.font.SysFont(None, 30)
    while True:
        #clear page so that the old circle is not still there
        screen.fill((0, 0, 0))
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
        # Update.
        for i, b1 in enumerate(bodys):
            for b2 in bodys[i+1:]:
                b1.calc_velocity(b2)

        for b in bodys:
            b.update_pos()

        # Draw.
        for b in bodys:
            b.draw(screen)

        sleeptime = 1/FPS - (time.time() - last_frame)
        if t%365 == 0 and not CHAOS:
            sleeptime = 1
        
        if sleeptime < 0:
            sleeptime = 0
        time.sleep(sleeptime)
        last_frame = time.time()
        t = t + 1
        # Render text onto surface
        text_surface = font.render(f"T = {t//365} years and {t%365} days", False, (0,255,255))
        # Blit surface onto screen
        screen.blit(text_surface, (0,0))
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
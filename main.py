import pygame
from pygame.locals import *
from body import Body
import time
import sys
import pygame.font
import random
from planets import *

WIDTH, HEIGHT = 640 *2, 480*2
CHAOS = False
include_jupiter = True
jupiter_close = True
jupiter_heavier = True


#one frame is 1 second
FPS = 60


def main():
    t = 0

    #creates bodies
    sun = create_sun()
    earth = create_earth()
    moon = create_moon()

    #stores the bodies in a list
    bodys = []
    bodys.append(sun)
    bodys.append(earth)
    pygame.init()
    pygame.font.init()
    bodys.append(moon)

    #adds jupiter, can be choosen to be closer or heavier or not
    if include_jupiter:
        jupiter = create_jupiter(jupiter_close, jupiter_heavier)
        bodys.append(jupiter)

    #adds random bodies
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

    # MAIN LOOP
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

        # Draw bodies
        for b in bodys:
            b.draw(screen)

        sleeptime = time.time() - last_frame
        #if t%365 == 0 and not CHAOS:
        #      sleeptime = 1
        
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
import pygame
from pygame.locals import *
from body import Body
import time
import sys
import pygame.font

WIDTH, HEIGHT = 640, 480

#one frame is 1 second
FPS = 60


def main():
    t = 0
    #Sun position center = 0,0
    sun_pos = (0, 0)
    #Sun velocity = ???, 0 kanske??
    sun_v = (0, 0)
    #Sun mass = 1.9885×10^30 kg, 332950 x earths mass
    sun_mass = 1.9885*(10**30)
    #Sun radius = 696,342 km, 109 x earths radius, kan bli svårt med en helt skalenlig representation
    sun_radius = 30
    #Sun color = gul
    sun_color = (255, 255, 0)
    sun = Body(sun_pos, sun_v, sun_mass, sun_radius, sun_color)
    #Earth position. mean distance to sun = 1.496×10^8 km.
    #23481 x earths radius. and convert to m
    earth_pos = (1.496*(10**8)*1000, 0)
    #Earth velocity = 107,200 km/h orbiting around the sun
    # made to m/s = 29,7777778 m/s
    earth_v = (0, 107200 * 0.277777778)
    #Earth mass = 5.972168×10^24 kg
    earth_mass = 5.972168*(10**24)
    #Earth mean radius = 6371 km
    earth_radius = 10
    earth_color = (0, 0, 255)
    earth = Body(earth_pos, earth_v, earth_mass, earth_radius, earth_color)
    #earth = Body(earth_pos, (0, 0), earth_mass, earth_radius, earth_color)

    moon_pos = (1.496*(10**8)*1000 + 384400 * 1000, 0)
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
        if t%365 == 0:
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
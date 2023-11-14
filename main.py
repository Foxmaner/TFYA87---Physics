import pygame
from pygame.locals import *
from body import Body
import time
import sys

WIDTH, HEIGHT = 640, 480

#one frame is 1 second
FPS = 60

def main():

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
    #stores the bodys in a list
    bodys = []
    bodys.append(sun)
    bodys.append(earth)

    print("Hello World!")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    last_frame = time.time()

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
        if sleeptime < 0:
            sleeptime = 0
        time.sleep(sleeptime)
        last_frame = time.time()
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
import pygame
from pygame.locals import *
from body import Body
import time
import sys

WIDTH, HEIGHT = 640, 480

def main():

    b1 = Body((0, 0), (1, 1), 1, 30, (255, 255, 0))
    #stores the bodys in a list
    bodys = []
    bodys.append(b1)

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
                b2.calc_velocity(b1)

        for b in bodys:
            b.update_pos()

        # Draw.
        for b in bodys:
            b.draw(screen)

        sleeptime = 1/60 - (time.time() - last_frame)
        time.sleep(sleeptime)
        last_frame = time.time()
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
import pygame



class Body():
    def __init__(self, position, velocity, mass, radius, collor):
        self.mass = mass
        self.radius = radius
        self.position = [position[0], position[1]]    # (x, y)
        self.velocity = velocity    # (x, y)
        self.collor = collor        # (r, g, b)


    def draw(self, screen):
        #we take the position and add half of the screen size to it so that the center of the screen is 0,0
        coordsX = self.position[0] + screen.get_size()[0]/2
        coordsY = self.position[1] + screen.get_size()[1]/2

        #Prints the circle
        pygame.draw.circle(screen, self.collor, (coordsX, coordsY), self.radius)

    def update_pos(self):
        #update the position of the body
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def calc_velocity(self, other):
        #calculate the velocity of the body
        pass
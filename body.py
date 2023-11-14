import pygame



class Body():
    def __init__(self, position, velocity, mass, radius, collor):
        self.mass = mass
        self.radius = radius
        self.position = [position[0], position[1]]    # (x, y)
        self.velocity = [velocity[0], velocity[1]]    # (x, y)
        self.collor = collor        # (r, g, b)


    def draw(self, screen):
        #we take the position and add half of the screen size to it so that the center of the screen is 0,0
        coordsX = (self.position[0]/1000000000) + screen.get_size()[0]/2
        coordsY = (self.position[1]/1000000000) + screen.get_size()[1]/2

        #Prints the circle
        pygame.draw.circle(screen, self.collor, (coordsX, coordsY), self.radius)

    def update_pos(self):
        #update the position of the body
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def calc_velocity(self, other, time_step=86400*30):
        G = 6.6743e-11  # gravitational constant
        dx = other.position[0] - self.position[0]
        dy = other.position[1] - self.position[1]
        dist = (dx**2 + dy**2)**0.5
        force = G * (self.mass * other.mass) / (dist**2)
        ax = force / self.mass * (dx / dist)
        ay = force / self.mass * (dy / dist)

        self.velocity[0] += ax * time_step
        self.velocity[1] += ay * time_step
        other.velocity[0] -= ax * self.mass / other.mass * time_step
        other.velocity[1] -= ay * self.mass / other.mass * time_step
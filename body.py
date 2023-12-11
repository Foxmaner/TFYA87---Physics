import pygame

class Body():
    def __init__(self, position, velocity, mass, radius, collor):
        self.mass = mass
        self.radius = radius
        self.position = [position[0], position[1]]    # (x, y)
        self.velocity = [velocity[0], velocity[1]]    # (x, y)
        self.collor = collor        # (r, g, b)
        self.trail = []


    def draw(self, screen):
        #we take the position and add half of the screen size to it so that the center of the screen is 0,0
        coordsX = (self.position[0]/2000000000) + screen.get_size()[0]/2
        coordsY = (self.position[1]/2000000000) + screen.get_size()[1]/2

        #Prints the circle
        pygame.draw.circle(screen, self.collor, (coordsX, coordsY), self.radius)

        self.trail.insert(0, (coordsX, coordsY))
        if len(self.trail) > 100:
            self.trail.pop(100)
        for dot in self.trail:
            pygame.draw.circle(screen, self.collor, dot, 1)

    def update_pos(self):
        #update the position of the body
        #multiplied by seconds in a day
        self.position[0] += self.velocity[0] * 86400
        self.position[1] += self.velocity[1] * 86400

    def calc_velocity(self, other, time_step=86400, max_acceleration=1e-5):
        G = 6.6743e-11  # gravitational constant
        dx = other.position[0] - self.position[0]
        dy = other.position[1] - self.position[1]
        dist = (dx**2 + dy**2)**0.5
        force = G * (self.mass * other.mass) / (dist**2)
        ax = force / self.mass * (dx / dist)
        ay = force / self.mass * (dy / dist)

        #Limiting acceleration to avoid planets flying away
        ax = max(-max_acceleration, min(ax, max_acceleration))
        ay = max(-max_acceleration, min(ay, max_acceleration))

        # other body velocity is affected by mass
        self.velocity[0] += ax * time_step
        self.velocity[1] += ay * time_step
        other.velocity[0] -= ax * self.mass / other.mass * time_step
        other.velocity[1] -= ay * self.mass / other.mass * time_step

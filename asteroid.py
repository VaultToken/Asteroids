import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        angle1 = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)

        radius_new = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid1.velocity = angle1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid2.velocity = angle2 * 1.2
import pygame, sys, random
pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

class Rain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((self.random_size()))
        self.image.fill((self.random_color()))
        self.rect = self.image.get_rect(center=(self.spawn_location()))
        self.movement_speed = random.randint(2,10)
    def random_size(self):
        width = random.randint(2,10)
        height = random.randint(15,60)
        return width,height
    def random_color(self):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return red,green,blue
    def spawn_location(self):
        x = random.randint(0,600)
        y = -30
        return x,y       
    def update(self):
        if self.rect.centery >= 650:
            self.kill()
        else:
            self.rect.centery += self.movement_speed
rain_group = pygame.sprite.Group()
def spawn_rain():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        rain = Rain()
        rain_group.add(rain)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("black")
    spawn_rain()
    rain_group.draw(screen)
    rain_group.update()
    pygame.display.update()
    clock.tick(60)

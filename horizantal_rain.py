import pygame, sys, random
pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(self.random_size())
        self.image.fill(self.random_color())
        self.rect = self.image.get_rect(center=self.spawn_location())
        self.movement_speed = random.randint(1,4)
    def random_size(self):
        width = random.randint(10, 60)
        height = random.randint(1,3)
        size = (width, height)
        return size
    def random_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        a = 0.1
        return (r,g,b,a)
    def spawn_location(self):
        x = 630
        y = random.randint(0,600)
        return (x,y)
    def update(self):
        if self.rect.centerx < 0:
            self.kill()
            print("done")
        else:
            self.rect.centerx -= self.movement_speed
rects_group = pygame.sprite.Group()
def spawn_rects():
    rect = Rect()
    rects_group.add(rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    spawn_rects()
    rects_group.update()
    rects_group.draw(screen)
    pygame.display.update()
    clock.tick(60)

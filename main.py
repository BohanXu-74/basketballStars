import pygame
import player

pygame.init()

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Basket Stars")

clock = pygame.time.Clock()

curry = player.player(100, 100)

team = pygame.sprite.Group()
team.add(curry)

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    team.draw(screen)

    curry.update(dt)

    pygame.display.flip()

pygame.quit()
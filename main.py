import pygame

W = 400
H = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

player = [W // 2, H - 50, 50, 50]

while True:
    clock.tick(68)

    screen.fill(WHITE)

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        player[0] -= 5
    if key[pygame.K_RIGHT]:
        player[0] += 5
    if key[pygame.K_UP]:
        player[1] -= 5
    if key[pygame.K_DOWN]:
        player[1] += 5

    pygame.draw.rect(screen, BLACK, player)
    pygame.display.update()





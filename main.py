import pygame, sys
pygame.init()

width = 900
height = 500
screen = pygame.display.set_mode((width, height))

black = (0,0,0)
white = (255,255,255)

ph = 20
pw = 100
px = width//2-pw//2
py = height-50-ph//2

paddle = pygame.Rect(px, py, pw, ph)

blocks = []
for x in range(5, width, 60):
    for y in range(5, height-250, 60):
        blocks.append(pygame.Rect(x, y, 50, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if paddle.left != 0:
            px -= 0.2
    if pressed[pygame.K_RIGHT]:
        if paddle.right != width:
            px += 0.2
    paddle.x = round(px)
    paddle.y = round(py)
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    for block in blocks:
        pygame.draw.rect(screen, white, block)
    pygame.display.flip()

pygame.quit()

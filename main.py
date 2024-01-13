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

points = 0

blocks = []
for x in range(5, width, 60):
    for y in range(5, height-250, 60):
        blocks.append(pygame.Rect(x, y, 50, 50))

mx, my = 0, 0.1
ball = pygame.Rect(width//2-20, py-100, 40, 40)
ballx = ball.centerx
bally = ball.centery

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
    if ball.colliderect(paddle):
        dfm = ball.centerx - paddle.centerx
        mx = dfm/100
        print(mx)
        if mx > 10:
            mx = 10
        my = -my
    if ball.top <= 0:
        my = -my
    if ball.bottom >= height:
        points += 1
        ballx = width//2
        bally = py-100
        mx = 0
        my = 1
    if ball.left <= 0 or ball.right >= width:
        mx = -mx
    ballx += mx
    bally += my
    ball.y = round(bally)
    ball.x = round(ballx)
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    for block in blocks:
        pygame.draw.rect(screen, white, block)
    pygame.draw.circle(screen, white, ball.center, 20)
    pygame.display.flip()

pygame.quit()

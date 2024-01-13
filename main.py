import pygame, sys
pygame.init()
pygame.font.init()

font = pygame.font.SysFont("comicsans", 30)

width = 900
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout by Xander")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,165,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
indigo = (75,0,135)
violet = (127,0,255)
colours = [red, orange, yellow, green, blue, indigo, violet]

ph = 20
pw = 100
px = width//2-pw//2
py = height-50-ph//2

paddle = pygame.Rect(px, py, pw, ph)

points = 0

blocks = []
ci = 0
for y in range(5, (7*40)+5, 40):
    color = colours[ci]
    for x in range(5, width, 60): 
        blocks.append([pygame.Rect(x, y, 50, 35), color])
    ci += 1

mx, my = 0, 0.1
ball = pygame.Rect(width//2-20, py-100, 40, 40)
ballx = ball.centerx
bally = ball.centery

choosing = True
mouseSelected = False
keysSelected = False
while choosing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RETURN):
                keysSelected = True
                choosing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseSelected = True
            choosing = False
    text = font.render("To use mouse, click. ", 0, white)
    text2 = font.render("To use left and right arrows, click them or enter.", 0, white)
    screen.blit(text, (0,0))
    screen.blit(text2, (0,text.get_height()))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    if keysSelected:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and not (paddle.colliderect(ball) and ballx < width//2):
            if paddle.left != 0:
                px -= 0.5
        if pressed[pygame.K_RIGHT]:
            if paddle.right != width and not (paddle.colliderect(ball) and ballx > width//2):
                px += 0.5
    elif mouseSelected:
        px = pygame.mouse.get_pos()[0] - paddle.width//2
        if px < 0:
            px = 0
        if px > width-paddle.width:
            px = width-paddle.width
    paddle.x = round(px)
    paddle.y = round(py)
    if ball.colliderect(paddle):
        dfm = ball.centerx - paddle.centerx
        mx = dfm/100
        if mx > 0.5 and mx >= 0:
            mx = 0.5
        if mx > -0.5 and mx <= -0:
            mx = -0.5
        print(mx)
        if mx > 10:
            mx = 10
        my = -my
    for block in blocks:
        if ball.colliderect(block[0]):
            del blocks[blocks.index(block)]
            mx = -mx
            my = -my
    if ball.top <= 0:
        my = -my
    if ball.bottom >= height:
        points += 1
        ballx = width//2
        bally = py-100
        mx = 0
        my = 0.1
    if ball.left <= 0 or ball.right >= width:
        mx = -mx
    ballx += mx
    bally += my
    ball.y = round(bally)
    ball.x = round(ballx)
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    for block in blocks:
        pygame.draw.rect(screen, block[1], block[0])
    pygame.draw.circle(screen, white, ball.center, 20)
    pygame.display.flip()

pygame.quit()

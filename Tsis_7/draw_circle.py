import pygame

pygame.init()
w,h = 500,500
screen = pygame.display.set_mode((w,h))
run = True
red = (255,0,0)
white = (255,255,255)
w_1 = w//2
h_1 = h//2
while run:
    screen.fill(white)
    pygame.draw.circle(screen, red,(w_1,h_1),25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                 if h_1 <= 30: # подбирал пиксили если меньше 30 то уже сверху шар выходит из облости нашего приложения в остальных случаях тоже подбирал
                     continue
                 h_1 -= 20# отнимаем 20 пиксилей значит шар будет находиться выше на 20 пикселей
                 pygame.draw.circle(screen, red,(w_1,h_1),25)

            if event.key == pygame.K_DOWN:
                if h_1 >= h-30:
                    continue
                h_1 += 20
                pygame.draw.circle(screen,red,(w_1,h_1),25)

            if event.key == pygame.K_RIGHT:
                if w_1 >= w -30:
                    continue
                w_1 += 20
                pygame.draw.circle(screen,red,(w_1,h_1),25)

            if event.key == pygame.K_LEFT:
                if w_1 <= 30:
                    continue
                w_1 -= 20
                pygame.draw.circle(screen, red,(w_1,h_1),25)

    pygame.display.flip()
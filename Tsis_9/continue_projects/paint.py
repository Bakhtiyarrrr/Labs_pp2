import pygame
import math
class Draw:
    def __init__(self,screen):
        self.screen = screen
        self.image_pencil = pygame.image.load("Labs_pp2/Tsis_8/for_paint/pencil.png")
        self.rect_pencil = self.image_pencil.get_rect(center = (25,25))
        # self.image_eraser = pygame.transform.scale(pygame.image.load("Labs_pp2/Tsis_8/for_paint/eraser.png"), (50, 47)) #подстроил размер как у первой картинки

        self.image_eraser = pygame.image.load("Labs_pp2/Tsis_8/for_paint/eraser.png")
        self.rect_eraser = self.image_eraser.get_rect(center = (70,26))

    def output(self):
        self.screen.blit(self.image_pencil,self.rect_pencil)
        self.screen.blit(self.image_eraser,self.rect_eraser)
        pygame.draw.rect(self.screen,black,(110,7,15,15))
        pygame.draw.rect(self.screen, gray,(110,35,15,15))
        pygame.draw.rect(self.screen, red,(140,7,15,15))
        pygame.draw.rect(self.screen,green,(140,35,15,15))
        pygame.draw.rect(self.screen,blue,(170,7,15,15))
        pygame.draw.rect(self.screen,yellow,(170,35,15,15))
       
pygame.init()
w,h = 700,600
screen = pygame.display.set_mode((w,h))
surface = pygame.Surface((w,h))
pygame.display.set_caption("Paint")
run = True
white = (255,255,255)
black = (0,0,0)
gray = (128, 128, 128)
red = (255,0,0)
green = (0,255,0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
fps = 60
pencil_black = False
pencil_gray = False
pencil_red = False
pencil_green = False
pencil_blue = False
pencil_yellow = False
pencil = False
eraser = False
rect = False
circle = False
isosceles_triangle = False
rhombus = False
right_triangle = False
EquilateralTriangle = False
square = False
truth = True
color = white
radius = 10
vertices = []

cord = []
width,height = 0,0
screen.fill(white)
surface.fill(white)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_x <= 50 and mouse_y <= 50:
                pencil = True
                eraser = False
                rect = False
                circle = False
                isosceles_triangle = False
                rhombus = False
                EquilateralTriangle = False
                right_triangle = False
                square = False
            elif mouse_x <= 90 and mouse_x > 50 and mouse_y <= 50:
                pencil = False
                eraser = True
                circle = False
                rect = False
                isosceles_triangle = False
                rhombus = False
                EquilateralTriangle = False
                right_triangle = False
                square = False

            if mouse_x <= 120 and mouse_x > 90 and mouse_y <= 25: #условия когда мышка окажется на кнопке черного цвета 
                pencil_black = True
                pencil_gray = False
                pencil_red = False
                pencil_green = False
                pencil_blue = False
                pencil_yellow = False
            elif mouse_x <= 120 and mouse_x >90 and mouse_y <= 50 and mouse_y > 25:
                pencil_black = False
                pencil_gray = True
                pencil_red = False
                pencil_green = False
                pencil_blue = False
                pencil_yellow = False
            elif mouse_x <= 150 and mouse_x > 140 and mouse_y <=25:
                pencil_red = True
                pencil_black = False
                pencil_gray = False
                pencil_green = False
                pencil_blue = False
                pencil_yellow = False
            elif mouse_x <= 150 and mouse_x > 140 and mouse_y <= 50 and mouse_y > 25:
                pencil_green = True
                pencil_red = False
                pencil_black = False
                pencil_gray = False
                pencil_blue = False
                pencil_yellow = False
            elif mouse_x <= 180 and mouse_x > 170 and mouse_y <= 25:
                pencil_green = False
                pencil_red = False
                pencil_black = False
                pencil_gray = False
                pencil_blue = True
                pencil_yellow = False
            elif mouse_x <= 180 and mouse_x > 170 and mouse_y <= 50 and mouse_y > 25:
                pencil_green = False
                pencil_red = False
                pencil_black = False
                pencil_gray = False
                pencil_blue = False
                pencil_yellow = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                radius += 1
            elif event.key == pygame.K_DOWN and radius != 5:
                radius -= 1
            elif event.key == pygame.K_1: # Равнобедренный треугольник
                isosceles_triangle = True
                rect = False
                pencil = False
                eraser = False
                circle = False
                rhombus = False
                EquilateralTriangle = False
                right_triangle = False
                square = False
            elif event.key == pygame.K_2: # Ромб
                isosceles_triangle = False
                rect = False
                pencil = False
                eraser = False
                circle = False
                rhombus = True
                EquilateralTriangle = False
                right_triangle = False
                square = False
            elif event.key == pygame.K_3: # Прямоугольный треугольник
                right_triangle = True
                isosceles_triangle = False
                rect = False
                pencil = False
                eraser = False
                circle = False
                rhombus = False
                EquilateralTriangle = False
                square = False
            elif event.key == pygame.K_4: # Равносторонний треугольник
                right_triangle = False
                isosceles_triangle = False
                rect = False
                pencil = False
                eraser = False
                circle = False
                rhombus = False
                square = False
                EquilateralTriangle = True
            elif event.key == pygame.K_5: # Квадрат
                square = True
                right_triangle = False
                isosceles_triangle = False
                rect = False
                pencil = False
                eraser = False
                circle = False
                rhombus = False
                EquilateralTriangle = False
            elif event.key == pygame.K_6:
                rect = True
                pencil = False
                eraser = False
                circle = False
                rhombus = False
                isosceles_triangle = False
                EquilateralTriangle = False
                right_triangle = False
                square = False
            elif event.key == pygame.K_7:
                rect = False
                pencil = False
                eraser = False
                circle = True
                rhombus = False
                isosceles_triangle = False
                EquilateralTriangle = False
                right_triangle = False
                square = False

        
    draw = Draw(screen)
    draw.output()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pos = (mouse_x,mouse_y)
    mouse = pygame.mouse.get_pressed()

    if pencil_black:
       color = black
    elif pencil_gray:
        color = gray
    elif pencil_red:
        color = red
    elif pencil_green:
        color = green
    elif pencil_blue:
        color = blue
    elif pencil_yellow:
            color = yellow

    if pencil:
       if mouse[0] == 1 and mouse_y >= 50:
          cord.append(mouse_x)
          cord.append(mouse_y)
          if truth:
             x_1,y_1 = cord[0],cord[1]

          x_2,y_2 = cord[len(cord) - 2],cord[len(cord) - 1]
          dx = abs(x_2 - x_1)
          dy = abs(y_2 - y_1)
          iterations = max(dx,dy)
          for x in range(iterations):
             progress = 1.0 * x / iterations
             aprogress = 1 - progress
             x = int(aprogress * x_1 + progress * x_2)
             y = int(aprogress * y_1 + progress * y_2)
             pygame.draw.circle(screen,color,(x,y),radius)
          
          x_1,y_1 = x_2,y_2
          truth = False
       elif mouse[0] == 0:
          cord.clear()
          truth = True
          
    if eraser:
       color = white
       if mouse[0] == 1 and mouse_y >= 50:
          cord.append(mouse_x)
          cord.append(mouse_y)
          if truth:
             x_1,y_1 = cord[0],cord[1]

          x_2,y_2 = cord[len(cord) - 2],cord[len(cord) - 1]
          dx = abs(x_2 - x_1)
          dy = abs(y_2 - y_1)
          iterations = max(dx,dy)
          for x in range(iterations):
             progress = 1.0 * x / iterations
             aprogress = 1 - progress
             x = int(aprogress * x_1 + progress * x_2)
             y = int(aprogress * y_1 + progress * y_2)
             pygame.draw.circle(screen,color,(x,y),radius)
          
          x_1,y_1 = x_2,y_2
          truth = False
       elif mouse[0] == 0:
          cord.clear()
          truth = True

    if rect:
       if mouse[0] == 1 and mouse_y >= 50:
          screen.blit(surface,(0,0))
          cord.append(mouse_x)
          cord.append(mouse_y)
          x_1,y_1 = cord[0],cord[1]
          x_2,y_2 = cord[len(cord) - 2],cord[len(cord) - 1]
          width = abs(x_2 - x_1)
          height = abs(y_2 - y_1)
          pygame.draw.rect(screen,color,(min(x_1,x_2),min(y_1,y_2),width,height),5)
       elif mouse[0] == 0:
           surface.blit(screen,(0,0))
           cord.clear()

    if circle:
        if mouse[0] == 1 and mouse_y >= 50:
            screen.blit(surface,(0,0))
            cord.append(mouse_x)
            cord.append(mouse_y)
            x_1,y_1 = cord[0],cord[1]
            x_2,y_2 = cord[len(cord) - 2],cord[len(cord) - 1]
            x = (x_1 + x_2) / 2
            y = (y_1 + y_2) / 2
            radius = abs(x_1 - x_2) / 2
            pygame.draw.circle(screen,color,(x,y),radius,5)
        elif mouse[0] == 0:
            surface.blit(screen,(0,0))
            cord.clear()

    if isosceles_triangle:
        if mouse[0] == 1 and mouse_y >= 50:
            screen.blit(surface,(0,0))
            cord.append(mouse_x)
            cord.append(mouse_y)
            x_1,y_1 = cord[0],cord[1]
            x_2,y_2 = cord[len(cord) - 2],cord[len(cord)- 1]
            if x_2 < x_1:
                 x_3,y_3 = x_1 + abs(x_2 - x_1),y_2 # левый угол когда тянем влево
                 pygame.draw.line(screen,color,(x_1,y_1),(x_2,y_2),5)
                 pygame.draw.line(screen,color,(x_1,y_1),(x_3,y_3),5)
                 pygame.draw.line(screen,color,(x_2,y_2),(x_3,y_3),5)
            elif x_2 > x_1:
                 x_3,y_3 = abs(x_1 - abs(x_2 - x_1)),y_2 # правый угол когда тянем вправо
                 pygame.draw.line(screen,color,(x_1,y_1),(x_2,y_2),5)
                 pygame.draw.line(screen,color,(x_1,y_1),(x_3,y_3),5)
                 pygame.draw.line(screen,color,(x_2,y_2),(x_3,y_3),5)

        elif mouse[0] == 0:
            surface.blit(screen,(0,0))
            cord.clear()

    if rhombus:
        if mouse[0] == 1 and mouse_y >= 50:
            screen.blit(surface,(0,0))
            cord.append(mouse_x)
            cord.append(mouse_y)
            x_1,y_1 = cord[0],cord[1] # верхний угол
            x_2,y_2 = cord[len(cord) - 2],cord[len(cord)- 1]
            x_3,y_3 = x_2,  y_1 + abs(y_2 - y_1)/2 # правый угол
            x_4,y_4 = abs(x_1 - abs(x_2 - x_1)), y_1 + abs(y_2 - y_1)/2 # левый угол
            x_5,y_5 = x_1,y_2 # нижний угол
            vertices = [(x_1,y_1),(x_3,y_3),(x_5,y_5),(x_4,y_4)]
            pygame.draw.polygon(screen,color,vertices,5)
        elif mouse[0] == 0:
            surface.blit(screen,(0,0))
            cord.clear()

    if right_triangle:
        if mouse[0] == 1 and mouse_y >= 50:
           screen.blit(surface,(0,0))
           cord.append(mouse_x)
           cord.append(mouse_y)
           x_1,y_1 = cord[0],cord[1] # верхний угол
           x_2,y_2 = cord[len(cord) - 2],cord[len(cord)- 1]
           x_3,y_3 = x_1,y_2
           pygame.draw.line(screen,color,(x_1,y_1),(x_2,y_2),5)
           pygame.draw.line(screen,color,(x_1,y_1),(x_3,y_3),5)
           pygame.draw.line(screen,color,(x_2,y_2),(x_3,y_3),5)
        elif mouse[0] == 0:
            surface.blit(screen,(0,0))
            cord.clear()
    
    if EquilateralTriangle:
        if mouse[0] == 1 and mouse_y >= 50:
           screen.blit(surface,(0,0))
           cord.append(mouse_x)
           cord.append(mouse_y)
           x_1,y_1 = cord[0],cord[1] # верхний угол
           x_2,y_2 = cord[len(cord) - 2],cord[len(cord)- 1]
           length = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)**0.5 # длина стороны
           if x_2 > x_1 and y_2 > y_1:
              x_3,y_3 = x_1 - length * math.cos(math.pi/3), y_1 + length * math.sin(math.pi/3)
              pygame.draw.line(screen,color,(x_1,y_1),(x_2,y_2),5)
              pygame.draw.line(screen,color,(x_1,y_1),(x_3,y_3),5)
              pygame.draw.line(screen,color,(x_2,y_2),(x_3,y_3),5)
           elif x_1 > x_2 and y_2 > y_1:
              x_3,y_3 = x_1 + length * math.cos(math.pi/3), y_1 + length * math.sin(math.pi/3)
              pygame.draw.line(screen,color,(x_1,y_1),(x_2,y_2),5)
              pygame.draw.line(screen,color,(x_1,y_1),(x_3,y_3),5)
              pygame.draw.line(screen,color,(x_2,y_2),(x_3,y_3),5)
           elif x_2 > x_1 and y_1 > y_2:
              x_3,y_3 = x_1 - length * math.cos(math.pi/3), y_1 - length * math.sin(math.pi/3)
              pygame.draw.line(screen,color,(x_1,y_1),(x_2,y_2),5)
              pygame.draw.line(screen,color,(x_1,y_1),(x_3,y_3),5)
              pygame.draw.line(screen,color,(x_2,y_2),(x_3,y_3),5)
           elif x_1 > x_2 and y_1 > y_2:
              x_3,y_3 = x_1 + length * math.cos(math.pi/3), y_1 - length * math.sin(math.pi/3)
              pygame.draw.line(screen,color,(x_1,y_1),(x_2,y_2),5)
              pygame.draw.line(screen,color,(x_1,y_1),(x_3,y_3),5)
              pygame.draw.line(screen,color,(x_2,y_2),(x_3,y_3),5)
        
        elif mouse[0] == 0:
            surface.blit(screen,(0,0))
            cord.clear()

    if square:
        if mouse[0] == 1 and mouse_y >= 50:
           screen.blit(surface,(0,0))
           cord.append(mouse_x)
           cord.append(mouse_y)
           x_1,y_1 = cord[0],cord[1]
           x_2,y_2 = cord[len(cord) - 2],cord[len(cord) - 1]
           width = abs(x_2 - x_1)
           height = abs(y_2 - y_1)
           pygame.draw.rect(screen,color,(min(x_1,x_2),min(y_1,y_2),height,height),5)
        elif mouse[0] == 0:
           surface.blit(screen,(0,0))
           cord.clear()
    
    pygame.display.flip()
pygame.quit()

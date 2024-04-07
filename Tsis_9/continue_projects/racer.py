import pygame
import random
import time
pygame.init()
class Player:
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.player = pygame.image.load("Labs_pp2/Tsis_8/for_racer/Player.png")
        self.player_rect = self.player.get_rect(center = (self.x,self.y))
    def output(self):
        self.screen.blit(self.player,self.player_rect)

class Enemy:
    def __init__(self,screen,z,t):
        self.z = z
        self.t = t
        self.screen = screen
        self.enemy = pygame.image.load("Labs_pp2/Tsis_8/for_racer/Enemy.png")
        self.enemy_rect = self.enemy.get_rect(center = (self.z,self.t))
    def output(self):
        self.screen.blit(self.enemy,self.enemy_rect)
class Game_over:
    def __init__(self, screen,font,truth):
        self.screen = screen
        self.truth = truth
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.text = font.render("Game Over!", True,self.black)
        self.text_rect = self.text.get_rect(center = (200,300))
    def output(self):
        if self.truth:
           pygame.mixer.music.load("Labs_pp2/Tsis_8/for_racer/crash.wav")
           pygame.mixer.music.play()
        time.sleep(1)
        screen.fill(self.red)
        screen.blit(self.text,self.text_rect)
class Coin:
    def __init__(self,screen,u,v,counter,number):
        self.screen = screen
        self.counter = counter
        self.u = u
        self.v = v
        self.number = number
        

        self.image_gold = pygame.image.load("Labs_pp2/Tsis_8/for_racer/coin.png")
        self.rect = self.image_gold.get_rect(center = (self.u,self.v))

        self.image_silver = pygame.image.load("Labs_pp2/Tsis_8/for_racer/coin_silver.png")
        self.rect = self.image_silver.get_rect(center = (self.u,self.v))

        self.image_bronze = pygame.image.load("Labs_pp2/Tsis_8/for_racer/coin_bronze.png")
        self.rect = self.image_bronze.get_rect(center = (self.u,self.v))

        self.text = font_for_score.render(f"Coin: {counter}",True,(0,0,0))
        self.text_rect = self.text.get_rect(center = (350,17))
    def output(self):
        
        
        if self.number == 1:
           self.screen.blit(self.image_gold,self.rect)
        elif self.number == 2:
           self.screen.blit(self.image_silver,self.rect)
        elif self.number == 3:
           self.screen.blit(self.image_bronze,self.rect)

        self.screen.blit(self.text,self.text_rect)
    
def scoree(score,screen,font_for_score):
    text = font_for_score.render(f"{score}",True,(0,0,0))
    text_rect = text.get_rect(center = (17,17))
    screen.blit(text,text_rect)
def music_background():
    pygame.mixer.music.load("Labs_pp2/Tsis_8/for_racer/background.wav")
    pygame.mixer.music.play()
    

    
pygame.mixer.music.set_endevent(pygame.USEREVENT)
truth = True
font = pygame.font.SysFont("Times New Roman",50)
fps = 30
w,h = (400,600)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Racer")
run = True
roud = pygame.image.load("Labs_pp2/Tsis_8/for_racer/AnimatedStreet.png")
rect_roud = roud.get_rect()
x,y = w//2,550
z,t = random.choice(range(20,400)),-50
player = Player(screen,x,y)
move_y = True
move_x = True
Game = True
score = 0
font_for_score = pygame.font.SysFont('Times New Roman',30)
q = 10
u,v = random.choice(range(20,400)),-50
counter = 0
once = True
number = 1 #служит для выбора монеты

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
       
    if abs(x - z) <= 40 and abs(y - t) <= 80:
        move_y = False
        move_x = False
        Game = False
        game = Game_over(screen,font,truth)
        truth = False
        game.output()
   
        
    if Game:
       if once:
          music_background()
       once = False
       if pygame.mixer.music.get_busy() == False: #если False значит музыка завершилась
           once = True
           
       keys = pygame.key.get_pressed()
       screen.blit(roud,rect_roud)
       enemy = Enemy(screen,z,t)
       enemy.output()
       coin = Coin(screen,u,v,counter,number)
       coin.output()
       player = Player(screen,x,y)
       player.output()
       if move_y:
          t += q # меняем координыты высоты монеты и машин чтобы они двигались вниз 
          v += q
          if t >= h:
             if (score % 2 == 0 and score != 0) or counter == 20: # ecли съел 20 монет скорость тоже увеличивается
                q += 2 # если число счета четное то увеличиваем скорость движения на два пикселя
             score += 1
             z,t = random.choice(range(40,360)),-50
          if abs(x - u) <= 40 and abs(y - v) <= 20: #cъедание монеты
             if number == 1: # если золотая монета то +3 к счету монет если серебрянная то +2 если бронзовая то +1
                 counter += 3
             elif number == 2:
                 counter += 2
             elif number == 3:
                 counter += 1
             u,v = random.choice(range(30,370)),-50 #если монету съела машина то меняем координаты
             number = random.choice(range(1,4))
             
          if v >= h or (abs(z - u) <= 60 and abs(t - v) <= 75): # если монета выйдет из дороги или создатся на машине то занова меняем координаты монетки
             u,v = random.choice(range(30,370)),-50
             number = random.choice(range(1,4))

       if move_x:
          if keys[pygame.K_RIGHT]:
             if x >= w - 20:
                continue
             x += 10
          elif keys[pygame.K_LEFT]:
             if x <= 20:
                continue
             x -= 10
            
       scoree(score,screen,font_for_score)
    clock = pygame.time.Clock()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
import pygame
import os



pygame.init()
w,h = 800, 533
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Music player")
run = True
black = (0,0,0)

image = pygame.image.load("Labs_pp2/Tsis_7/for_music_player/photo_music_player.webp")
rect = image.get_rect()
screen.blit(image, rect)

songs = os.listdir("Labs_pp2/Tsis_7/for_music_player/songs")

stop_m = False
n = len(songs)
i = 0
j = 0
pygame.mixer.music.load("Labs_pp2/Tsis_7/for_music_player/songs/" + songs[i])
pygame.mixer.music.play()
font = pygame.font.Font(None, 30)

            
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and stop_m == False:
                     pygame.mixer.music.pause()
                     stop_m = True
               elif event.key == pygame.K_SPACE and stop_m == True:
                         pygame.mixer.music.unpause()
                         stop_m = False
               if event.key == pygame.K_LEFT and i == 0:
                     pygame.mixer.music.load("Labs_pp2/Tsis_7/for_music_player/songs/" + songs[n-1])
                     pygame.mixer.music.play()
                     i = n - 1
               elif event.key == pygame.K_LEFT and i != 0:
                     pygame.mixer.music.load("Labs_pp2/Tsis_7/for_music_player/songs/" + songs[i-1])
                     pygame.mixer.music.play()
                     i = i - 1
               if event.key == pygame.K_RIGHT and i == n - 1:
                     pygame.mixer.music.load("Labs_pp2/Tsis_7/for_music_player/songs/" + songs[0])
                     pygame.mixer.music.play()
                     i = 0
               elif event.key == pygame.K_RIGHT and i != n - 1:
                     pygame.mixer.music.load("Labs_pp2/Tsis_7/for_music_player/songs/" + songs[i+1])
                     pygame.mixer.music.play()
                     i = i + 1

        screen.blit(image, rect)
        text_surface = font.render(songs[i], True, black)
        text_rect = text_surface.get_rect(center = (w//2, h//2+10))
        screen.blit(text_surface, text_rect)
    pygame.display.flip()
    
    

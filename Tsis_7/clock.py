import pygame
import datetime


pygame.init()
w,h = (838,837)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Mickey's clock")
run = True

image_clock = pygame.image.load("Labs_pp2/Tsis_7/for_clock/mainclock.png")
left_hand = pygame.image.load("Labs_pp2/Tsis_7/for_clock/leftarm.png")
right_hand = pygame.image.load("Labs_pp2/Tsis_7/for_clock/rightarm.png")
rect = image_clock.get_rect()


left_hand = pygame.transform.rotate(left_hand, -4)
right_hand = pygame.transform.rotate(right_hand, -55.5)

while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False
    screen.blit(image_clock, rect)
    current_time = datetime.datetime.now()
    current_seconds = current_time.second
    current_minutes = current_time.minute

    angle_lh = current_seconds * 6
    rotated_left_hand = pygame.transform.rotate(left_hand, -angle_lh)
    rotated_rect_lh = rotated_left_hand.get_rect(center=rect.center)
    screen.blit(rotated_left_hand, rotated_rect_lh)

    angle_rh = (current_minutes * 60 + current_seconds) * 0.1
    rotated_right_hand = pygame.transform.rotate(right_hand, -angle_rh)
    rotated_right_rh = rotated_right_hand.get_rect(center = rect.center)
    screen.blit(rotated_right_hand, rotated_right_rh)
    pygame.display.flip()
    
    
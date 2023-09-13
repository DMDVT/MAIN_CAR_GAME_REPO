import pygame
from pygame.locals import *
import random

pygame.init()


win_size = HEIGHT,WIDTH = (800, 800)


running = True
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("DipVidTime's Car Game")

screen.fill((61,221,1))


#GAME GRAPHIC VARIABLES
road_w = int(WIDTH/1.6)
roadmark_w = int(WIDTH/80)

## --> LANES
right_lane = WIDTH/2 + road_w/4
left_lane = WIDTH/2 - road_w/4

pygame.display.update()
#OUR CAR STUFF
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = (right_lane,HEIGHT*0.8)

#ENEMY CAR STUFF
car2 = pygame.image.load("enemycar.png")
car2_loc = car.get_rect()
car2_loc.center = (left_lane,HEIGHT*0.1)

# MAIN VARIABLES
counter = 0
speed  = 1


while running:
    counter += 1

    if counter == 2500:
        speed += 1.1
        counter - 0
        print("speed leveled up, now is: ",speed)

    car2_loc[1] += speed
    if car2_loc[1] > HEIGHT:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane,-200
        else:
            car2_loc.center = left_lane, -200

    if car2_loc[0] == car_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("YOU CRASHED BE A BETTER DRIVER")
        break


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a,K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2),0])
            if event.key in [K_d,K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2),0])


    pygame.draw.rect(screen,(50,50,50),(WIDTH/2-road_w/2,0,road_w,HEIGHT))
    pygame.draw.rect(screen,(255,241,60),((WIDTH/2-roadmark_w/2,0,roadmark_w,HEIGHT)))
    pygame.draw.rect(screen,(255,255,255),(WIDTH/2-road_w/2 + roadmark_w*2,0,roadmark_w,HEIGHT))
    pygame.draw.rect(screen,(255,255,255),(WIDTH/2+road_w/2 - roadmark_w*3,0,roadmark_w,HEIGHT))

    screen.blit(car,car_loc)
    screen.blit(car2,car2_loc)

    pygame.display.update()

pygame.quit()
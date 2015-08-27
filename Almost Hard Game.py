import pygame
from rect_levels import *
from obstacles import Obstacle_v
from obstacles import Obstacle_h

pygame.init()

home_img = [ pygame.image.load("home.png"), pygame.image.load("home_1.png") ]
bg = [ pygame.image.load("level_1.png"), pygame.image.load("level_2.png"), pygame.image.load("level_3.png"),
       pygame.image.load("level_4.png"), pygame.image.load("level_last.png") ]
ball_img = pygame.image.load("ball.png")
pause_img = pygame.image.load("pause.png")
deaths_img = pygame.image.load("deaths.png")
arrow_img = pygame.image.load("arrow.png")

collision = pygame.mixer.Sound("collision.wav")

w, h = bg[0].get_size()
screen = pygame.display.set_mode((w, h), 0, 32)

d_img = ball_img.get_width()
x_ball = y_ball = d_img*2
x_hole, y_hole = d_img, h - (d_img*3)

obstacles = []

speed = 250.
level_index = 0
deaths = 0

home_index = 0
home_index_img = 0
home_pos = [(120, 340), (120, 400)]

pause = False

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

font_1 = pygame.font.SysFont("Bauhaus", 32)
font_2 = pygame.font.SysFont("Bauhaus", 20)

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if home_index == 0:
                    home_index = 1
            elif event.key == pygame.K_UP:
                if home_index == 1:
                    home_index = 0
            elif event.key == pygame.K_RETURN:
                if home_index == 0:
                    home_index_img = 1
                elif home_index == 1:
                    start = False
            elif event.key == pygame.K_b:
                if home_index_img == 1:
                    home_index_img = 0
            elif event.key == pygame.K_ESCAPE:
                pygame.display.quit()
    screen.blit(home_img[home_index_img], (0, 0))
    if home_index_img == 0:
        screen.blit(arrow_img, home_pos[home_index])
    pygame.display.update()

running = True
while running == True:
    screen.fill((0,0,0))
    text_1 = font_1.render(("Level "+str(level_index+1)), True, (255, 255, 255))
    screen.blit(text_1, (260, 284))
    pygame.display.update()
    pygame.time.wait(500)
    level = True
    while level:   
        if pause == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                    if event.key == pygame.K_p:
                        if pause == True:
                            pause = False
                        elif pause == False:
                            pause = True
            screen.blit(pause_img, (250, 267))
            pygame.display.update()
        elif pause == False:
            ball = pygame.Rect(x_ball, y_ball, d_img, d_img)
            hole = pygame.Rect(x_hole, y_hole, 40, 40)
            time = clock.tick(60)
            time_sec = time/1000.
            d = speed*time_sec
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                    if event.key == pygame.K_p:
                        if pause == True:
                            pause = False
                        elif pause == False:
                            pause = True                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        speed = 250.
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                y_ball -= d  
            if key[pygame.K_DOWN]:
                y_ball += d
            if key[pygame.K_RIGHT]:
                x_ball += d
            if key[pygame.K_LEFT]:
                x_ball -= d
            if key[pygame.K_SPACE]:
                speed = 50.

            level = levels[level_index]
            for wall in range(0, len(level)):
                if ball.colliderect(level[wall]):
                    collision.play()
                    pygame.time.wait(50)
                    x_ball = y_ball = d_img*2
                    deaths += 1

            if len(obstacles) != 0:
                for z in range(0, len(obstacles)):
                    obstacle = obstacles[z]
                    obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, d_img, d_img)
                    level = levels[level_index]
                    for rect in range(0, len(level)):
                        if obstacle_rect.colliderect(level[rect]):
                            obstacle.speed = -obstacle.speed
                    obstacle.moves()
                    if ball.colliderect(obstacle_rect):
                        collision.play()
                        pygame.time.wait(50)
                        x_ball = y_ball = d_img*2
                        deaths += 1

            if hole.contains(ball):
                x_ball = y_ball = d_img*2
                level_index += 1
                if level_index == 2:
                    obstacles.append(Obstacle_v(140, 20, d_img, 4))
                    obstacles.append(Obstacle_v(340, 20, d_img, 2))
                    obstacles.append(Obstacle_h(500, 260, d_img, 3))
                if level_index == 3:
                    obstacles.append(Obstacle_h(120, 440, d_img, 2))
                    obstacles.append(Obstacle_h(120, 460, d_img, 4))
                if level_index == 4:
                    level = False
                    running = False
                level = False

            if level_index >= 3:
                if x_ball >= 280 and y_ball >= 540:
                    x_ball -= 300*time_sec
            
            screen.blit(bg[level_index], (0,0))
            screen.blit(deaths_img, (500, 0))
            text_3 = font_2.render((str(deaths)), True, (0, 0, 0))
            screen.blit(text_3, (570, 3))
            if level_index != 4:
                screen.blit(ball_img, (x_ball, y_ball))
            if len(obstacles) != 0:
                for z in range(0, len(obstacles)):
                    obstacle = obstacles[z]
                    screen.blit(obstacle.img, (obstacle.x, obstacle.y))
            pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()

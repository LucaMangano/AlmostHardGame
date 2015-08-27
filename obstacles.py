import pygame
import random

class Obstacle_v():

    def __init__(self, x, y, d_img, d):
        self.x = x
        self.y = y
        self.img = pygame.image.load("wall.png")
        self.d_img = d_img
        speed = (-d, d)
        self.speed = random.choice(speed)

    def moves(self):
        self.y += self.speed

        
class Obstacle_h():

    def __init__(self, x, y, d_img, d):
        self.x = x
        self.y = y
        self.img = pygame.image.load("wall.png")
        self.d_img = d_img
        speed = (-d, d)
        self.speed = random.choice(speed)

    def moves(self):
        self.x += self.speed

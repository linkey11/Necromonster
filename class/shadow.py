import pygame
from pygame.transform import *
from math import *
import time

class Shadow():
    def __init__(self, game, surface, pos):
        self.game = game
        self.sun = [0, 650]
        self.center = self.game.center_point
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        self.current_alpha = 50

        self.shadow_strips = self.make_shadow()

    def make_shadow(self):
        shadow_strips = []
        for j in range(self.rect.height):
            strip = pygame.Surface((self.rect.width,1)).convert_alpha()
            strip.fill((0,0,0,0))
            for i in range(self.rect.width):
                pixel = self.image.get_at((i,j))
                if pixel != (0,0,0,0):
                    #alpha = min(j*5, 255)
                    strip.set_at((i,0), (0,0,0,50))
            shadow_strips.append(strip)
        return shadow_strips[::-1]
 
    def draw_shadow(self, surface, sun):
        slope = self.get_sun_slope(sun)
        sign = 1 if sun[1] < self.rect.centery else -1
        for i,strip in enumerate(self.shadow_strips):
            pos = (self.rect.x+i*slope*sign, self.rect.bottom+i*sign)
            if not self.game.HUD.daytime > 780:
                surface.blit(strip, self.game.off(pos))
 
    def get_sun_slope(self, sun):
        rise = sun[0]-self.center[0]
        run = sun[1]-self.center[1]
        try:
            return rise/float(run)
        except ZeroDivisionError:
            return 0

    def moveSun(self, mouse):
        self.sun[0] = 700 - self.game.HUD.daytime*0.5

    def setAlpha(self, alpha):
        for strip in self.strips:
            strip.fill((0, 0, 0, alpha))

    def getAlpha(self):
        return self.strips[0].get_alpha()

    def update(self, screen):
        self.moveSun(pygame.mouse.get_pos())

        self.draw_shadow(screen, self.sun)




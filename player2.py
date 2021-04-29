import pygame
from projectilej2 import Projectilej2
import imageall


# creer une premiere classe qui va representer notre joueur
class Joueur2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.current_frame, self.update_frame = 0, 0
        # stance
        self.frame0 = imageall.Itachi_stance0
        self.frame1 = imageall.Itachi_stance1
        self.frame2 = imageall.Itachi_stance2
        self.frame3 = imageall.Itachi_stance3
        # stance inversée
        self.frame4 = imageall.Itachi_Lstance0
        self.frame5 = imageall.Itachi_Lstance1
        self.frame6 = imageall.Itachi_Lstance2
        self.frame7 = imageall.Itachi_Lstance3
        # walkL
        self.frame8 = imageall.Itachi_walk0
        self.frame9 = imageall.Itachi_walk1
        self.frame10 = imageall.Itachi_walk2
        self.frame11 = imageall.Itachi_walk3
        self.frame12 = imageall.Itachi_walk4
        self.frame13 = imageall.Itachi_walk5
        # walkR
        self.frame14 = imageall.Itachi_Lwalk0
        self.frame15 = imageall.Itachi_Lwalk1
        self.frame16 = imageall.Itachi_Lwalk2
        self.frame17 = imageall.Itachi_Lwalk3
        self.frame18 = imageall.Itachi_Lwalk4
        self.frame19 = imageall.Itachi_Lwalk5

        self.image_load()
        self.image = self.corp_frame[0]
        self.image = self.corp_frame_invers[0]
        self.image = self.corp_frame_walkR[0]
        self.image = self.corp_frame_walkL[0]
        self.image = pygame.transform.scale(self.image, (66, 112))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 347

    def image_load(self):
        self.corp_frame = [self.frame0, self.frame1, self.frame2, self.frame3]
        self.corp_frame_invers = [self.frame4, self.frame5, self.frame6, self.frame7]
        self.corp_frame_walkR = [self.frame8, self.frame9, self.frame10, self.frame11, self.frame12, self.frame13]
        self.corp_frame_walkL = [self.frame14, self.frame15, self.frame16, self.frame17, self.frame18, self.frame19]

    def animate_corp(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 140:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame)
            self.image = self.corp_frame[self.current_frame]
            self.image = pygame.transform.scale(self.image, (52, 112))

    def animate_corp_invers(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 140:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_invers)
            self.image = self.corp_frame_invers[self.current_frame]
            self.image = pygame.transform.scale(self.image, (106, 112))


    def launch_projectilej2(self):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectilej2(self))

    def animate_corp_walkR(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 120:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_walkR)
            self.image = self.corp_frame_walkR[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def animate_corp_walkL(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 120:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_walkL)
            self.image = self.corp_frame_walkL[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def move_right(self):
        self.rect.x += self.velocity
        self.animate_corp_walkR()

    def move_left(self):
        self.rect.x -= self.velocity
        self.animate_corp_walkL()

    def stance(self):
        self.animate_corp_invers()

    def stanceinvers(self):
        self.animate_corp()




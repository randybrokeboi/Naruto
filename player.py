import pygame
from projectile import Projectile
from animation import AnimateSprite
import imageall
# creer une premiere classe qui va representer notre joueur
class Joueur(AnimateSprite):

    def __init__(self):
        super().__init__(self, 1)
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.current_frame, self.update_frame = 0, 0
        # stance ..................................
        self.frame0 = imageall.Naruto_stance0
        self.frame1 = imageall.Naruto_stance1
        self.frame2 = imageall.Naruto_stance2
        self.frame3 = imageall.Naruto_stance3
        self.frame4 = imageall.Naruto_stance4
        self.frame5 = imageall.Naruto_stance5
        # stance inversée .............................................
        self.frame6 = imageall.Naruto_Lstance6
        self.frame7 = imageall.Naruto_Lstance1
        self.frame8 = imageall.Naruto_Lstance2
        self.frame9 = imageall.Naruto_Lstance3
        self.frame10 = imageall.Naruto_Lstance4
        self.frame11 = imageall.Naruto_Lstance5
        # walkR .............................................
        self.frame12 = imageall.Naruto_walk0
        self.frame13 = imageall.Naruto_walk1
        self.frame14 = imageall.Naruto_walk2
        self.frame15 = imageall.Naruto_walk3
        self.frame16 = imageall.Naruto_walk4
        self.frame17 = imageall.Naruto_walk5
        # walkL .................................................
        self.frame18 = imageall.Naruto_Lwalk0
        self.frame19 = imageall.Naruto_Lwalk1
        self.frame20 = imageall.Naruto_Lwalk2
        self.frame21 = imageall.Naruto_Lwalk3
        self.frame22 = imageall.Naruto_Lwalk4
        self.frame23 = imageall.Naruto_Lwalk5
        # Combo 1..........................................
        self.frame24 = imageall.Naruto_combo0
        self.frame25 = imageall.Naruto_combo1
        self.frame26 = imageall.Naruto_combo2
        self.frame27 = imageall.Naruto_combo3

        self.frame28 = imageall.Naruto_Lcombo0
        self.frame29 = imageall.Naruto_Lcombo1
        self.frame30 = imageall.Naruto_Lcombo2
        self.frame31 = imageall.Naruto_Lcombo3

        self.image_load()
        self.image = self.corp_frame[0]
        self.image = self.corp_frame_invers[0]
        self.image = self.corp_frame_walkR[0]
        self.image = self.corp_frame_walkL[0]
        self.image = self.corp_frame_combo1[0]
        self.image = pygame.transform.scale(self.image, (76, 112))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 347


    def image_load(self):
        self.corp_frame = [self.frame0, self.frame1, self.frame2, self.frame3, self.frame4, self.frame5]
        self.corp_frame_invers = [self.frame6, self.frame7, self.frame8, self.frame9, self.frame10, self.frame11]
        self.corp_frame_walkR = [self.frame12, self.frame13, self.frame14, self.frame15, self.frame16, self.frame17]
        self.corp_frame_walkL = [self.frame18, self.frame19, self.frame20, self.frame21, self.frame22, self.frame23]
        self.corp_frame_combo1 = [self.frame24, self.frame25, self.frame26, self.frame27]
        self.corp_frame_comboL1 = [self.frame28, self.frame29, self.frame30, self.frame31]


    def animate_corp(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 120:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame)
            self.image = self.corp_frame[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def animate_corp_invers(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 120:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_invers)
            self.image = self.corp_frame_invers[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

    def animate_corp_walkR(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 90:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_walkR)
            self.image = self.corp_frame_walkR[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def animate_corp_walkL(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 90:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_walkL)
            self.image = self.corp_frame_walkL[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def animate_corp_combo1(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 110:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_combo1)
            self.image = self.corp_frame_combo1[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def animate_corp_comboL1(self):
        now = pygame.time.get_ticks()
        if now - self.update_frame > 110:
            self.update_frame = now
            self.current_frame = (self.current_frame + 1) % len(self.corp_frame_comboL1)
            self.image = self.corp_frame_comboL1[self.current_frame]
            self.image = pygame.transform.scale(self.image, (76, 112))

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [self.rect.x, self.rect.y + -7, 100, 5])
        pygame.draw.rect(surface, (69, 139, 0), [self.rect.x, self.rect.y + -7, self.health, 5])

    def move_right(self):
        self.rect.x += self.velocity
        self.animate_corp_walkR()

    def move_left(self):
        self.rect.x -= self.velocity
        self.animate_corp_walkL()

    def stance(self):
        self.animate_corp()

    def stanceinvers(self):
        self.animate_corp_invers()

    def combo1(self):
        self.animate_corp_combo1()

    def comboL1(self):
        self.animate_corp_comboL1()





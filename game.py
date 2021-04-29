import pygame
from pygame.locals import *

from player import Joueur
from player2 import Joueur2
from sound import SoundManager


# classe du jeu
class Game:

    def __init__(self, window):

        self.is_playing = False
        self.pressed = {}
        self.pressed2 = {}
        self.pressed3 = {}
        self.sound_manager = SoundManager()
        self.screen = window.screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.floor = 500

        # player
        self.all_sprites = pygame.sprite.Group()

        self.player = Joueur()
        self.player2 = Joueur2()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)




    def update_projectiles(self):
        for projectiles in self.player.all_projectiles:
            projectiles.move(self.player, self.player2)



    def check_collision(self, sprite1, sprites):
        return pygame.sprite.spritecollide(sprite1, sprites, False, pygame.sprite.collide_mask)

    def update_alls(self):
        if self.pressed.get(K_RIGHT) and self.player.rect.x + self.player.rect.width < self.screen.get_width():
            self.player.move_right()
        elif self.pressed.get(K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        if not self.pressed.get(pygame.K_RIGHT) and not self.pressed.get(pygame.K_LEFT) or\
                self.player.rect.x + self.player.rect.width == self.screen.get_width() or self.player.rect.x == 0:
            if self.player.rect.x <= self.player2.rect.x:
                self.player.stance()
            # orienté le joueur1 en fonction du joueur2
            elif self.player.rect.x > self.player2.rect.x:
                self.player.stanceinvers()

        if self.pressed2.get(pygame.K_d) and self.player2.rect.x + self.player2.rect.width < self.screen.get_width():
            self.player2.move_right()
        elif self.pressed2.get(pygame.K_q) and self.player2.rect.x > 0:
            self.player2.move_left()
        if not self.pressed2.get(pygame.K_d) and not self.pressed2.get(pygame.K_q) or\
                self.player2.rect.x + self.player2.rect.width == self.screen.get_width() or self.player2.rect.x == 0:
            if self.player2.rect.x >= self.player.rect.x:
                self.player2.stance()
            # orienté le joueur2 en fonction du joueur1
            elif self.player2.rect.x < self.player.rect.x:
                self.player2.stanceinvers()
        if self.pressed3.get(pygame.K_m):
            if self.player.rect.x < self.player2.rect.x:
                self.player.combo1()
            if self.player.rect.x > self.player2.rect.x:
                self.player.comboL1()
        # dessine tout les groupes
        self.all_sprites.draw(self.screen)
        self.player.all_projectiles.draw(self.screen)

        # updates
        self.player.start()
        self.player.update_health_bar(self.screen)
        self.update_projectiles()

    def reset_game(self):
        self.player.health = 100
        self.is_playing = False
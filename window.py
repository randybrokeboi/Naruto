import pygame

# importation des utilitaires
from pygame.locals import *
from game import Game


class WindowScreen:
    pygame.init()

    def __init__(self, name, width, height):
        pygame.display.set_caption(name)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background = None
        self.banner = None
        self.play_button = None
        self.game = Game(self)
        self.running = True

    def set_background(self, name):
        self.background = pygame.image.load('assets/' + name)

    def set_banner(self, name, scale_x, scale_y):
        self.banner = pygame.image.load('assets/' + name)
        self.banner = pygame.transform.scale(self.banner, (scale_x, scale_y))

    def set_play_button(self, name, scale, pos_x, pos_y):
        self.play_button = pygame.image.load('assets/' + name)
        self.play_button = pygame.transform.scale(self.play_button, scale)
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = pos_x
        self.play_button_rect.y = pos_y

    def loop(self):

        while self.running:

            # dessin du fond et du joueur
            self.game.screen.fill((0, 0, 0))
            self.game.screen.blit(self.background, (0, 0))

            # update sur le jeu est en cours
            #if self.game.is_playing:
            self.game.update_alls()
            #else:
                #self.game.screen.blit(self.play_button, self.play_button_rect)
                #self.game.screen.blit(self.banner,
                                      #(int(self.game.screen_width / 4), int(-self.game.screen_height / 20)))

            # actualisation
            pygame.display.flip()
            # verifier si le joueur ferme cette fenetre
            for event in pygame.event.get():
                # verifier que l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print("Fermeture du jeu")

                # detecter si un joueur lache une touche du clavier
                elif event.type == pygame.KEYDOWN:
                    self.game.pressed[event.key] = True
                    self.game.pressed2[event.key] = True
                    self.game.pressed3[event.key] = True

                    # detecter si la touche espace est enclenchée pour lancer notre projectile
                    if event.key == pygame.K_l:
                        self.game.player.launch_projectile()
                    if event.key == pygame.K_q:
                        self.game.player2.launch_projectilej2()
                elif event.type == pygame.KEYUP:
                    self.game.pressed[event.key] = False
                    self.game.pressed2[event.key] = False
                    self.game.pressed3[event.key] = False

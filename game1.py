import pygame
from pygame.locals import *

from player import Joueur
from player2 import Joueur2
#from sound import SoundManager


# creer une seconde classe qui va representer le jeu
class Game:

    def __init__(self):
        self.is_playing = False
        # generer le joueur
        self.player = Joueur()
        # generer le joueur 2
        self.player2 = Joueur2()
        self.pressed = {}
        self.pressed2 = {}
        self.pressed3 = {}
        self.sound_manager = SoundManager()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        # player
        self.all_sprites = pygame.sprite.Group()

        self.player = Joueur(self)
        self.all_sprites.add(self.player)

#######################################################################
    pygame.init()

    # Generer la fenetre du jeu
    pygame.display.set_caption("Naruto 4 Storm Ninja Ultimate")
    screen = pygame.display.set_mode((1022, 480))

    # importer charger l'arriere plan de notre jeu
    background = pygame.image.load('assets/naruto_background1.png')
    background = pygame.transform.scale(background, (1200, 612))
    # charger le jeu
    self = self()
 # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -132))

    # appliquer l'image de mon joueur
    screen.blit(self.player.image, self.player.rect)

    # appliquer l'image du joueur 2
    screen.blit(self.player2.image, self.player2.rect)

    # recuperer les projectile du joueur
    for projectile in self.player.all_projectiles:
        projectile.move()
    for projectile2 in self.player.all_projectiles:
        projectile2.move()

    # applique l'ensemble des images de mon groupe de projectiles
    self.player.all_projectiles.draw(screen)


    def update_alls(self):

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if not self.pressed.get(pygame.K_RIGHT) and not self.pressed.get(pygame.K_LEFT):
            if self.player.rect.x < self.player2.rect.x:
                self.player.stance()
            # orienté le joueur1 en fonction du joueur2
            elif self.player.rect.x > self.player2.rect.x:
                self.player.stanceinvers()
        self.player.update_health_bar(screen)
        self.all_sprites.draw(self.screen)

        # updates
        self.player.animate()
        # pour connaitre la position du joueur
        print(self.player.rect.x)


        # verifier si le joueur2 souhaite aller a gauche ou a droite
        if self.pressed2.get(pygame.K_d) and self.player2.rect.x + self.player2.rect.width < screen.get_width():
            self.player2.move_right()
        elif self.pressed2.get(pygame.K_q) and self.player2.rect.x > 0:
            self.player2.move_left()
        if not self.pressed2.get(pygame.K_d) and not self.pressed2.get(pygame.K_q):
            if self.player2.rect.x > self.player.rect.x:
                self.player2.stance()
            # orienté le joueur2 en fonction du joueur1
            elif self.player2.rect.x < self.player.rect.x:
                self.player2.stanceinvers()
        # pour connaitre la position du joueur2
        print(self.player2.rect.x)
    # mettre a jour l'ecran
    pygame.display.flip()

    # combo
    if self.pressed3.get(pygame.K_1):
        if self.player.rect.x < self.player2.rect.x:
            self.player.combo1()
        if self.player.rect.x > self.player2.rect.x:
            self.player.comboL1()



    # verifier si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # verifier que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            self.pressed[event.key] = True
            self.pressed2[event.key] = True
            self.pressed3[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SLASH:
                self.player.launch_projectile()
            if event.key == pygame.K_q:
                self.player2.launch_projectilej2()
        elif event.type == pygame.KEYUP:
            self.pressed[event.key] = False
            self.pressed2[event.key] = False
            self.pressed3[event.key] = False
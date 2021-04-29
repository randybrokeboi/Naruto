import pygame

# definir la classe qui va gerer le projectile du joueur2
class Projectilej2(pygame.sprite.Sprite):

    # definir le constucteur de cette classe
    def __init__(self, player2):
        super().__init__()
        self.velocity = 7
        self.player = player2
        self.image = pygame.image.load('assets/image_naruto/naruto_shuriken1.png')
        self.image = pygame.transform.scale(self.image, (30,  30))
        self.rect = self.image.get_rect()
        self.rect.x = player2.rect.x + 65
        self.rect.y = player2.rect.y + 15
        self.origin_image = self.image
        self.angle = 0

    def sens(self, player, player2):
        if player2.rect.x < player.rect.x:
            self.rect.x = player2.rect.x + 65
            self.rect.y = player2.rect.y + 15
        elif player2.rect.x > player.rect.x:
            self.rect.x = player2.rect.x - 65
            self.rect.y = player2.rect.y - 15

    def rotate(self, player2, player):
        # tourner le projectile en deplacement
        if player2.rect.x < player.rect.x:
            self.angle += -14
        elif player2.rect.x > player.rect.x:
            self.angle += 14
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self, player2, player):
        if player2.rect.x < player.rect.x:
            self.rect.x += self.velocity
        if player2.rect.x > player.rect.x:
            self.rect.x -= self.velocity
        self.rotate()

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1000 or self.rect.x < 0:
            # supprimer le projectile en dehors de l'ecran
            self.remove()
            print("projectile supprimer")
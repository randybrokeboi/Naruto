import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name, size, animation_enabled=False):
        super().__init__()

        # parameters
        self.name = name
        self.size = size
        self.animation = animation_enabled

        # super class
        #self.image = pygame.image.load('assets/' + name + '/' + name + '1.png')
        #self.image = pygame.transform.scale(self.image, (size, size))
        #self.rect = self.image.get_rect()

        self.costumes = []
        self.current_costume = 0
        self.load_animation()

    def start(self):
        self.animation = True

    def animate(self, loop=True):

        if self.animation is True:
            self.current_costume += 1  # image suivante
            if self.current_costume > (len(self.costumes) - 1):
                self.current_costume = 0  # remet l'image numero 1

                # si le mode boucle est desactivée une action est attendu
                if loop == False:
                    self.animation = False

            self.image = self.costumes[self.current_costume]
            self.image = pygame.transform.scale(self.image, (self.rect.height, self.rect.height))

    def load_animation(self):
        for i in range(1, 12):
            path = "assets/" + "image_naruto" + "/" + "Naruto_combo" + "/" + "Naruto_combo" + str(i) + ".png"
            image = pygame.image.load(path)
            self.costumes.append(image)
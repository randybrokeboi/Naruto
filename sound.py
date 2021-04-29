import pygame

class SoundManager:

    def __init__(self):

        self.all_sounds = {
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg"),
            'meteorite': pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            'gameover': pygame.mixer.Sound("assets/sounds/game_over.ogg")
        }

    def play(self, name):
        self.all_sounds[name].play()
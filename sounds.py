import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'hit': pygame.mixer.Sound("assets/sounds2/hit.wav"),
            'game_over': pygame.mixer.Sound("assets/sounds2/dead.wav"),
            'shoot': pygame.mixer.Sound("assets/sounds2/shoot.wav"),
            'start': pygame.mixer.Sound("assets/sounds2/start.wav")
        }


    def play(self, name):
        self.sounds[name].play()

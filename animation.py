import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.running = False
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation =  False

    def start_animations(self):
        self.animation = True

    def animate(self, loop=False):

        if self.animation:
            self.current_image += 1

            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]

    def load_animation(self, path, frame_durations):
        animation_frame_data = []
        animations_name = path.split('/')[-1]
        n = 1
        for frame in frame_durations:
            animation_frame_id = animations_name + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            for i in range(frame):
                animation_frame_data.append(pygame.image.load(img_loc))
            n += 1
        self.current_image +=1
        if self.current_image >= len(animation_frame_data):
            self.current_image = 0
        self.image = animation_frame_data[self.current_image]







def load_animations_images(sprite_name):
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"

    for num in range(1, 25):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images



animations = {
    "wizard": load_animations_images('wizard'),
    "player": load_animations_images('player')
}

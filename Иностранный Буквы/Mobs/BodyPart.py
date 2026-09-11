import os
import pygame

class BodyPart():
    def __init__(self, file_path, size):
        if os.path.isfile(file_path):
            image = pygame.image.load(candidate).convert_alpha()
            self.body_part_sprite = pygame.transform.smoothscale(image, size)

        raise FileNotFoundError(f"No image found for '{file_path}'")

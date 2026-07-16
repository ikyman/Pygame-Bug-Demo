import os
import pygame


# What the AI considered Reasonable default sizes for each body part (width, height).
# I disagree: these are quite small
HAIR_BACK_SIZE = (48, 48)
HEAD_SIZE = (48, 48)
ARM_SIZE = (32, 48)
LEG_SIZE = (32, 48)
TORSO_SIZE = (48, 64)
WAIST_SIZE = (48, 32)


class SpriteSheet:
    def __init__(self, folder_name: str, body_part_mapping = dict()) -> None:
        """
        Load and scale all body-part sprites from the given folder.

        Expects image files named (case-insensitive):
        - hair_back.*
        - head.*
        - arm.*
        - leg.*
        - torso.*
        - waist.*
        """
        self.folder_name = folder_name

        # Individual body-part surfaces, scaled to their respective sizes.
        #self.hair_back = self._load_and_scale("hair_back", HAIR_BACK_SIZE, body_part_mapping)
        self.head = self._load_and_scale("head", HEAD_SIZE, body_part_mapping)
        self.arm = self._load_and_scale("arm", ARM_SIZE, body_part_mapping)
        self.leg = self._load_and_scale("leg", LEG_SIZE, body_part_mapping)
        self.torso = self._load_and_scale("torso", TORSO_SIZE, body_part_mapping)
        self.waist = self._load_and_scale("waist", HIPS_SIZE, body_part_mapping)

    def _load_and_scale(self, base_name: str, size: tuple[int, int], body_part_mapping) -> pygame.Surface:
        """
        Helper to load an image by base name from the folder and scale it.

        Tries common image extensions; raises FileNotFoundError if none found.
        """
        body_part_name = body_part_mapping.get(base_name, base_name)
        # Try a few common extensions.
        for ext in (".png", ".jpg", ".jpeg", ".bmp"):
            candidate = os.path.join(self.folder_name, base_name + ext)
            if os.path.isfile(candidate):
                image = pygame.image.load(candidate).convert_alpha()
                return pygame.transform.smoothscale(image, size)

        raise FileNotFoundError(f"No image found for '{base_name}' in '{self.folder_name}'")
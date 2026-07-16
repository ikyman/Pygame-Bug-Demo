from tkinter import *
import pygame

from Mobs.PlayerAvatar import PlayerAvatar
from Mobs.SpriteSheet import SpriteSheet

DEFAULT_CANVAS_WIDTH = 500
DEFAULT_CANVAS_HEIGHT = 500
DEFAULT_CANVAS_BACKGROUND_COLOR = 'whitesmoke'
DEFAULT_SIDEBAR_WIDTH = 200

all_torso_dict = {
    "hair_back" : "torso",
    "head" : "torso",
    "arm" : "torso",
    "leg" : "torso",
    "torso" : "torso",
    "waist" : "torso",
}


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Puzzling Pummeling")
    running = True
    clock = pygame.time.Clock()
    
    
    all_display = pygame.display.set_mode((DEFAULT_CANVAS_WIDTH + DEFAULT_SIDEBAR_WIDTH, DEFAULT_CANVAS_HEIGHT))
    polygonCanvas = pygame.Surface( (DEFAULT_CANVAS_WIDTH, DEFAULT_CANVAS_HEIGHT) )

    player = PlayerAvatar(SpriteSheet("Upperclassman", all_torso_dict))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        pressed_keys = pygame.key.get_pressed()
        
        all_display.blit(polygonCanvas, (0,0) )       
        polygonCanvas.fill("seagreen1")  
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    quit()
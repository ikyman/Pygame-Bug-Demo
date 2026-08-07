import pygame
from pixelArray import RandomMosaic

pygame.init()

class displayScreen:
    SCREEN_SIZE_X = 800
    SCREEN_SIZE_Y = 600
    SCREEN_CAPTION = "Random Mosaic"
    SCREEN_EMPTY_COLOR = "lightskyblue1"

    def __init__(self):
        self.screen = pygame.display.set_mode((displayScreen.SCREEN_SIZE_X, displayScreen.SCREEN_SIZE_Y))
        pygame.display.set_caption(displayScreen.SCREEN_CAPTION)
    

if __name__ == "__main__":
    width = int(input("Enter mosaic width (squares): "))
    height = int(input("Enter mosaic height (squares): "))
    
    clock = pygame.time.Clock()
    dis_screen = displayScreen()
    mosaic = RandomMosaic(width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        dis_screen.screen.fill(displayScreen.SCREEN_EMPTY_COLOR)  
        mosaic.draw(dis_screen.screen, 10, 10, 0 ,0 )
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

import pygame


class RandomMosaic():
 def __init__(self, width, height, scale_factor=1, mosaic_type="deep_ocean", direction=S):
  self.width = width
  self.height = height
  self.scale_factor = scale_factor
  self.mosaic_type = mosaic_type
  self.direction = direction
    
 def draw(self, parent_surface,  map_center_x, map_center_y, offset_x, offset_y):
  
  mosaic_width = self.scale_factor * self.width
  mosaic_height = self.scale_factor * self.height
  
  mosaic_surface = pygame.Surface( (self.mosaic_width, self.height))
  mosaic_surface.fill(pygame.Color( "magenta") )
  
  pixelated_mosaic = pygame.PixelArray(mosaic_surface);
  for rindex in range(0, mosaic_height):
   for cindex in range(0, mosaic_width):
    pixelatedMap[(self.scale_factor*cindex):(self.scale_factor*(cindex+1)), (rindex*self.scale_factor):(rindex+1)*self.scale_factor] = pygame.Color("white")
    
  pixelatedMap.close()
    
  mosaic_surface.blit(parent_surface (map_center_x, map_center_y))
 
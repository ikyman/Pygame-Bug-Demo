This is a program making gradient Mosaics, mostly to test the bug https://github.com/pygame/pygame/issues/4728

The inputs are: Mosaic sizes, Mosaic offsets, the scale factor, the gradient direction, and the mosaic type.

What this pogram does is it creates a mosaic with a pattern in the specified direction.
The mosaic is mosaic_width squares wide and mosaic_height squares tall. Each square of the mosaic is scale factor pixels.

The offsets are used to set pixels out-of-bounds from the PixelArray's Surface. 

This program, as stated before, tests the bug https://github.com/pygame/pygame/issues/4728 in a more pure and accessable environment than the one I found the bug in.

If my Bug Report is correct, the Mosaic program should crash if I have an offset and the size of the Mosaic (in total pixels) is small.

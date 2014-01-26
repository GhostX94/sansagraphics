import pygame
from pygame.locals import *
import sys, os
from math import *
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

##import Settings
##width, height, width2, height2 = Settings.main()

(width,height) = (800,600)
(width2,height2) = (400,300)
Screen = (width,height)
pygame.display.set_caption("Mandelbrot Set - Ian Mallett - v.2.0.0 - 2008")
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
Resolution = 1.5
MandelbrotSet = pygame.Surface((width2,height2))
MaxIteration = 255

ViewPosition = [0,0]

ColourPalette = [(255, 140, 140),(255, 145, 135), (255, 150, 130), (254, 155, 124), (254, 160, 119), (253, 165, 113), (252, 170, 107), (251, 174, 102), (250, 179, 96), (249, 183, 90), (247, 188, 84), (246, 192, 78),
                 (244, 196, 72), (242, 200, 66), (240, 204, 60), (238, 207, 54), (236, 211, 48), (233, 214, 42), (231, 218, 36), (228, 221, 29), (225, 224, 23), (222, 227, 17), (219, 230, 11), (215, 232, 4), (212, 235, 2), (208, 237, 8), (205, 239, 14), (201, 242, 21), (197, 243, 27), (193, 245, 33), (189, 247, 39), (185, 248, 45), (180, 250, 52), (176, 251, 58), (171, 252, 64), (167, 253, 70), (162, 254, 76), (157, 254, 82), (152, 255, 88), (147, 255, 94), (142, 255, 99), (136, 255, 105), (131, 255, 111), (126, 254, 116), (120, 254, 122), (115, 253, 127), (109, 253, 133), (103, 252, 138), (98, 250, 143), (92, 249, 148), (86, 248, 153), (80, 246, 158), (74, 245, 163), (68, 243, 168), (62, 241, 173), (56, 239, 177), (50, 236, 182), (44, 234, 186), (37, 231, 190), (31, 229, 194), (25, 226, 198), (19, 223, 202), (13, 220, 206), (6, 216, 210), (0, 213, 213), (6, 210, 216), (13, 206, 220), (19, 202, 223), (25, 198, 226), (31, 194, 229), (37, 190, 231), (44, 186, 234), (50, 182, 236), (56, 177, 239), (62, 173, 241), (68, 168, 243), (74, 163, 245), (80, 158, 246), (86, 153, 248), (92, 148, 249), (98, 143, 250), (103, 138, 252), (109, 133, 253), (115, 127, 253), (120, 122, 254), (126, 116, 254), (131, 111, 255), (136, 105, 255), (142, 99, 255), (147, 94, 255), (152, 88, 255), (157, 82, 254), (162, 76, 254), (167, 70, 253), (171, 64, 252), (176, 58, 251), (180, 52, 250), (185, 45, 248), (189, 39, 247), (193, 33, 245), (197, 27, 243), (201, 21, 242), (205, 14, 239), (208, 8, 237), (212, 2, 235), (215, 4, 232), (219, 11, 230), (222, 17, 227), (225, 23, 224), (228, 29, 221), (231, 36, 218), (233, 42, 214), (236, 48, 211), (238, 54, 207), (240, 60, 204), (242, 66, 200), (244, 72, 196), (246, 78, 192), (247, 84, 188), (249, 90, 183), (250, 96, 179), (251, 102, 174), (252, 107, 170), (253, 113, 165), (254, 119, 160), (254, 124, 155), (255, 130, 150), (255, 135, 145), (255, 140, 140), (255, 145, 135), (255, 150, 130), (254, 155, 124), (254, 160, 119), (253, 165, 113), (252, 170, 107), (251, 174, 102), (250, 179, 96), (249, 183, 90), (247, 188, 84), (246, 192, 78), (244, 196, 72), (242, 200, 66), (240, 204, 60), (238, 207, 54), (236, 211, 48), (233, 214, 42), (231, 218, 36), (228, 221, 29), (225, 224, 23), (222, 227, 17), (219, 230, 11), (215, 232, 4), (212, 235, 2), (208, 237, 8), (205, 239, 14), (201, 242, 21), (197, 243, 27), (193, 245, 33), (189, 247, 39), (185, 248, 45), (180, 250, 52), (176, 251, 58), (171, 252, 64), (167, 253, 70), (162, 254, 76), (157, 254, 82), (152, 255, 88), (147, 255, 94), (142, 255, 99), (136, 255, 105), (131, 255, 111), (126, 254, 116), (120, 254, 122), (115, 253, 127), (109, 253, 133), (103, 252, 138), (98, 250, 143), (92, 249, 148), (86, 248, 153), (80, 246, 158), (74, 245, 163), (68, 243, 168), (62, 241, 173), (56, 239, 177), (50, 236, 182), (44, 234, 186), (37, 231, 190), (31, 229, 194), (25, 226, 198), (19, 223, 202), (13, 220, 206), (6, 216, 210), (0, 213, 213), (6, 210, 216), (13, 206, 220), (19, 202, 223), (25, 198, 226), (31, 194, 229), (37, 190, 231), (44, 186, 234), (50, 182, 236), (56, 177, 239), (62, 173, 241), (68, 168, 243), (74, 163, 245), (80, 158, 246), (86, 153, 248), (92, 148, 249), (98, 143, 250), (103, 138, 252), (109, 133, 253), (115, 127, 253), (120, 122, 254), (126, 116, 254), (131, 111, 255), (136, 105, 255), (142, 99, 255), (147, 94, 255), (152, 88, 255), (157, 82, 254), (162, 76, 254), (167, 70, 253), (171, 64, 252), (176, 58, 251), (180, 52, 250), (185, 45, 248), (189, 39, 247), (193, 33, 245), (197, 27, 243), (201, 21, 242), (205, 14, 239), (208, 8, 237), (212, 2, 235), (215, 4, 232), (219, 11, 230), (222, 17, 227), (225, 23, 224), (228, 29, 221), (231, 36, 218), (233, 42, 214), (236, 48, 211), (238, 54, 207), (240, 60, 204), (242, 66, 200), (244, 72, 196), (246, 78, 192), (247, 84, 188), (249, 90, 183), (250, 96, 179), (251, 102, 174), (252, 107, 170), (253, 113, 165), (254, 119, 160), (254, 124, 155), (255, 130, 150), (255, 135, 145)]

def CalculateMandelbrotSet():
    width = MandelbrotSet.get_width()
    height = MandelbrotSet.get_height()
    #row = 0
    for ypixel in xrange(height):
        for xpixel in xrange(width):
            x = -2 + (3*(float(xpixel)/float(width)))
            y = -1 + (2*(float(ypixel)/float(height)))
            z = complex(x,y)
            c = z
            Colour = (0,0,0)
            for iteration in xrange(MaxIteration):
                z = (z*z)+c
                if abs(z) > 2.236:
                    break
                else:
                    if iteration == MaxIteration-1:
                        Colour = (0,0,0)
                    else:
                        Colour = iteration
            MandelbrotSet.set_at((xpixel,height-ypixel),Colour)
        #row += 1
        #PercentDone = round( (float(row)/float(height)), 3 ) * 100
        #print "Row "+str(row)+"/"+str(height)+" ("+str(PercentDone)+"%) Complete!"
    print 'Saving Image as "Mandelbrot Set.png"...'
    pygame.image.save(MandelbrotSet,"Mandelbrot Set.png")
    print "Image Saved!"

mouseDown = False

def GetInput():
    global ViewPosition
    global mouseDown
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or key[K_ESCAPE]:
		pygame.quit()	
		sys.exit()
	elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
		x,y = event.pos
		mouseDown = True
		prevx = x
		prevy = y




    if key[K_LEFT ]: ViewPosition[0] += 1
    if key[K_RIGHT]: ViewPosition[0] -= 1
    if key[K_UP   ]: ViewPosition[1] += 1
    if key[K_DOWN ]: ViewPosition[1] -= 1
    if key[K_r    ]: ViewPosition = [0,0]
def Draw():
    Surface.fill((0,0,0))
    Surface.blit(MandelbrotSet,ViewPosition)
    pygame.display.flip()
def main():
    global Surface
    CalculateMandelbrotSet()
    Surface = pygame.display.set_mode(Screen)
    MandelbrotSet.convert()
    print "You can use the arrow keys (r resets view) to move around the set.  Have fun!"
    while True:
        GetInput()
        Draw()
if __name__ == '__main__': main()

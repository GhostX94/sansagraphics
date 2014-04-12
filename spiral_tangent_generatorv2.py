
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Import a library of functions called 'pygame'
import pygame
import math
import prime_list
 
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

PI = 3.141592653
right_angle=PI/2
 
# Set the height and width of the screen
xscreen=900
yscreen=480
centerx=xscreen/2.0
centery=yscreen/2.0
size = [xscreen,yscreen]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
xorigin=999.9
yorigin=999.9
n=3
max_spiral_angle=PI/3.0

def spiral(n, min_radius, max_radius, nos_parts, centerx, centery, max_spiral_angle):
    gap = (max_radius - min_radius)/nos_parts
    angle_increment=max_spiral_angle/nos_parts
    phi = 2*PI/n
    xorigin=999.9
    sub_parts=3
    cx=0.5
    cy=0.5
    cz=0.5

    for i in range(0, n+1):
	angle = i*phi
	radius = min_radius
	spiral_angle=angle
	xorigin = 999.9
    	for j in range(0, nos_parts+1):
		x_offset = radius*(math.cos(spiral_angle))+centerx
		y_offset = radius*(math.sin(spiral_angle))+centery
		x_offset1 = radius*(math.cos(spiral_angle+right_angle))+centerx
		y_offset1 = radius*(math.sin(spiral_angle+right_angle))+centery
		radius = radius + gap
		spiral_angle=spiral_angle + angle_increment

		if (j>0) and (xorigin!=999.9):
			cx=int(120*(math.sin(2*(spiral_angle))+1)+10)
			cy=int(120*(math.sin(spiral_angle)+1)+10)
			cz=int(120*(math.sin(spiral_angle-PI)+1)+10)
       		 	pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[x_offset,y_offset],2)
			if (sub_parts==0):
       		 		pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[xorigin+30*(x_offset-xorigin),yorigin+30*(y_offset-yorigin)],2)
       		 		pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[xorigin+30*(x_offset1-xorigin),yorigin+30*(y_offset1-yorigin)],2)
			else:
				sub_parts=sub_parts-1
		else:
       			pygame.draw.line(screen,[cx,cy,cz],[centerx,centery],[x_offset,y_offset],2)

		xorigin = x_offset
		yorigin = y_offset

while done == False:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    #screen.fill(white)
    # move the angle from 0 to x
    # draw the point from radius a (which can be 0 or not) to radius b (slowly increasin)
    # the point as a series of contour which spiral...ie spiral of spiral
 
    min_radius=10.0
    max_radius=100.0
    nos_parts=10
    spiral(n, min_radius, max_radius, nos_parts, centerx, centery, max_spiral_angle)

    n = n + 1 
    pygame.display.flip()
    print "Press enter.."
    raw = raw_input()
    screen.fill(black)
 
# Be IDLE friendly
pygame.quit()


# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
##  http://mathworld.wolfram.com/Epicycloid.html
# Import a library of functions called 'pygame'
import pygame
import math
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

PI = 3.141592653
r=0
R=100
 
# Set the height and width of the screen
size = [800,480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
colour=red
thickness=2
i=0
ntotal=6
delta=2*PI/ntotal
a=2.0
b=1.0

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
    screen.fill(white)
 
    # Draw on the screen several green lines from (0,10) to (100,110) 
    # 5 pixels wide using a loop
    colour=red
    prevx = R*math.sin((0.0))+r*math.sin((0.0)) + 400.0
    prevy = R*math.cos((0.0))+r*math.cos((0.0)) + 240.0
    for n in range(1,ntotal+1):
        ##pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
        theta = n * delta
	y_offset = R*math.cos((theta))+r*math.cos((theta)) + 240.0
	x_offset = R*math.sin((theta))+r*math.sin((theta)) + 400.0
        cx=int(120*(math.sin((theta)/10)+1)+10)
	cy=int(120*(math.sin((theta)*6/10)+1)+10)
        cz=int(120*(math.sin((theta)/10-PI)+1)+10)

	if (n>0):
        	pygame.draw.line(screen,[cx,cy,cz],[prevx,prevy],[x_offset,y_offset],thickness)
#		pygame.draw.circle(screen, [cx,cy,cz], (int(prevx),int(prevy)), R, thickness)
	prevx=x_offset
	prevy=y_offset
	
    	##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    ##delta += ddelta
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()

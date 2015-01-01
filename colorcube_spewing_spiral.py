import sys
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ''' Error: PyOpenGL not installed properly '''
  sys.exit(  )

import math
import array
import signal
import random

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

import math

PI = 3.141592653
ngon=120
angle_step=2*PI/ngon
r1_step = 0.005
r2_step = 0.001
delta=0.6
theta1 = 2*PI/ngon

fullscreen = False
mouseDown = False

xrot = 0.2
yrot = 0.0

xdiff = 0.0
ydiff = 0.0
ndisc = 20

def init():
#	glClearColor(0.93, 0.93, 0.93, 0.0)
	glClearColor(1.0,1.0,1.0,0.0)
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClearColor(0.0, 0.0, 0.0, 0.0)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glClearDepth(1.0)

	return True

import sys
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

Vertices = ((-1,-1,-1), (1,-1,-1),
            (1,1,-1), (-1,1,-1),
            (-1,-1,1), (1,-1,1),
            (1,1,1), (-1,1,1))
central_vector = (0,0,0)

Colors   = ((0,0,0), (1,0,0),
            (1,1,0), (0,1,0),
            (0,0,1), (1,0,1),
            (1,1,1), (0,1,1))

def draw_translate_vector(target_vector, central_vector, max_delta):
	glBegin(GL_LINES)
	for delta in range(max_delta):
		new_vector=(delta*(target_vector[0]-central_vector[0])+central_vector[0], delta*(target_vector[1]-central_vector[1])+central_vector[1], delta*(target_vector[2]-central_vector[2])+central_vector[2])
    		glVertex3fv((new_vector[0],new_vector[1],new_vector[2]));
    	glEnd()
	

def face(a,b,c,d):
    '''draw a face defined by four vertex indices'''
    glBegin(GL_QUADS)
    glColor3fv(Colors[a]);    glVertex3fv(Vertices[a]);
    glColor3fv(Colors[b]);    glVertex3fv(Vertices[b]);
    glColor3fv(Colors[c]);    glVertex3fv(Vertices[c]);
    glColor3fv(Colors[d]);    glVertex3fv(Vertices[d]);
    glEnd()

def draw_radiating_spiral(central_vector, nos_turns):
    a=0
    cx=central_vector[0]
    cy=central_vector[1]
    cz=central_vector[2]
    r=0.5
    ngon=18
    glBegin(GL_LINES)
    theta=math.pi/ngon
    glColor3fv(Colors[a]);    
    angle=0.0
    z_delta=0.01
    vec_delta=0.1
    z=0
    for i in range(nos_turns*ngon):
	x=r*math.cos(angle)
	y=r*math.sin(angle)
	z+=z_delta
	fx=(x-cx)*vec_delta+cx
	fy=(y-cy)*vec_delta+cy
	fz=(z-cz)*vec_delta+cz
	glVertex3fv((fx,fy,fz));
    	glColor3fv(Colors[a]);    
	angle+=theta
	vec_delta+=0.01
	r+=0.01
	a+=1
	a = a % 8
    glEnd()
		
	
	
def colorcube():
    '''Draws the entire cube, six faces'''
    face(0,3,2,1)
    face(2,3,7,6)
    face(0,4,7,3)
    face(1,2,6,5)
    face(4,5,6,7)
    face(0,1,5,4)

def edge(A, B):
    '''Sends two vertices down the pipeline.  Presumably they form an edge'''
    glVertex3fv(Vertices[A]);
    glVertex3fv(Vertices[B]);

def wireCube():
    glBegin(GL_LINES)
    ## back
    edge(0,1)
    edge(1,2)
    edge(2,3)
    edge(3,0)
    ## front
    edge(4,5)
    edge(5,6)
    edge(6,7)
    edge(7,4)
    ## sides
    edge(0,4)
    edge(1,5)
    edge(2,6)
    edge(3,7)
    glEnd()


def normal_face():
	norm_face(3,6,2,7)
	norm_face(2,1,3,6)
	norm_face(6,4,1,3)
	norm_face(1,6,2,5)
	norm_face(4,7,6,5)
	norm_face(5,1,6,4)
	norm_face(7,6,3,4)
	norm_face(0,4,3,1)
	
def display():
	global xrot, yrot
	global ndisc
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 10.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

#    	glutWireCube(1)
	wireCube()
 	glColor3f(0.5, 0.0, 1.0)
##	glutWireDodecahedron(2)
#	colorcube()
	draw_radiating_spiral(central_vector, 100)
	##draw_translate_vector(Vertices[0], central_vector, max_delta):
    ##	glVertex3fv(Vertices[d]);

    	glFlush()
    	glutSwapBuffers()





def resize(*args):
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	glViewport(0, 0, args[0], args[1])

	gluPerspective(45.0, 1.0 * args[0] / args[0], 1.0, 100.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()


def idle():
	global xrot, yrot
	global mouseDown
	if not (mouseDown):
		xrot += 0.3
		yrot += 0.4

	glutPostRedisplay()


def keyboard(*args):
	##print args[0]
	if (args[0]==27):
	##	print args[0]
		sys.exit(1)


def specialKeyboard(*args):
	##print args[0]
	if (args[0] == GLUT_KEY_F1):
		fullscreen = not(fullscreen)

		if (fullscreen):
			glutFullScreen()
		else:
			glutReshapeWindow(500, 500)
			glutPositionWindow(50, 50)

def mouse(*args):
	global xrot, yrot
	global xdiff, ydiff
	global mouseDown
	if (args[0] == GLUT_LEFT_BUTTON and args[1] == GLUT_DOWN):
		mouseDown = True
		xdiff = args[2] - yrot
		ydiff = -args[3] + xrot
	else:
		mouseDown = False


def mouseMotion(*args):
	global xrot, yrot
	global xdiff, ydiff
	global mouseDown
	if (mouseDown):
		yrot = args[0] - xdiff
		xrot = args[1] + ydiff
	glutPostRedisplay()


def main():
	glutInit(sys.argv)
	glutInitWindowPosition(50, 50)
	glutInitWindowSize(500, 500)

	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

	glutCreateWindow("13 - Solid Shapes")

	glutDisplayFunc(display)
	glutKeyboardFunc(keyboard)
	glutSpecialFunc(specialKeyboard)
	glutMouseFunc(mouse)
	glutMotionFunc(mouseMotion)
	glutReshapeFunc(resize)

	if not (init()):
		return 1

	glutIdleFunc(idle)

	glutMainLoop()

	return 0

if __name__ == "__main__":
    main()

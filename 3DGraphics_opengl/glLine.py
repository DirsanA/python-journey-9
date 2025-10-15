from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
gluOrtho2D(0, 800, 0, 600)

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)
    
    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex2f(100, 200)
    glVertex2f(150, 200)
    glVertex2f(150, 250)
    glVertex2f(200, 250)
    glEnd()

    pygame.display.flip()

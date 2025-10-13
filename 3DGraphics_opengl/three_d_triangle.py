from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import sys

def draw_pyramid():
    glBegin(GL_TRIANGLES)

    # Front face (Red)
    glColor3f(1, 0, 0)
    glVertex3f(0, 1, 0)    # Top
    glVertex3f(-1, -1, 1)  # Bottom left
    glVertex3f(1, -1, 1)   # Bottom right

    # Right face (Green)
    glColor3f(0, 1, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)

    # Back face (Blue)
    glColor3f(0, 0, 1)
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)

    # Left face (Yellow)
    glColor3f(1, 1, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)

    glEnd()

    # Draw the base (square)
    glBegin(GL_QUADS)
    glColor3f(0, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glEnd()


def main():
    pygame.init()
    display = (900, 700)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("🔥 3D Rotating Pyramid Demo")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -6)
    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get mouse position for interactive rotation
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x_rot = (mouse_y / display[1] - 0.5) * 360
        y_rot = (mouse_x / display[0] - 0.5) * 360

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        glRotatef(x_rot, 1, 0, 0)
        glRotatef(y_rot, 0, 1, 0)
        draw_pyramid()

        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

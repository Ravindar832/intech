// 3D Solar System Simulation in OpenGL

#include <GL/glut.h>
#include <cmath>

float earthOrbitAngle = 0.0f;
float moonOrbitAngle = 0.0f;

void init() {
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);
    glShadeModel(GL_SMOOTH);

    GLfloat light_pos[] = {0.0, 0.0, 0.0, 1.0}; // Light at Sun
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos);
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    // Camera setup
    gluLookAt(0.0, 10.0, 20.0,  // eye
              0.0, 0.0, 0.0,   // center
              0.0, 1.0, 0.0);  // up

    // Draw Sun
    glPushMatrix();
        glColor3f(1.0, 1.0, 0.0); // Yellow
        glutSolidSphere(2.0, 50, 50);
    glPopMatrix();

    // Earth orbiting Sun
    glPushMatrix();
        glRotatef(earthOrbitAngle, 0.0, 1.0, 0.0);
        glTranslatef(7.0, 0.0, 0.0);

        // Draw Earth
        glColor3f(0.0, 0.0, 1.0); // Blue
        glutSolidSphere(1.0, 50, 50);

        // Moon orbiting Earth
        glRotatef(moonOrbitAngle, 0.0, 1.0, 0.0);
        glTranslatef(2.0, 0.0, 0.0);

        // Draw Moon
        glColor3f(0.5, 0.5, 0.5); // Gray
        glutSolidSphere(0.3, 50, 50);
    glPopMatrix();

    glutSwapBuffers();
}

void timer(int value) {
    earthOrbitAngle += 0.2f;
    if (earthOrbitAngle >= 360.0f) earthOrbitAngle -= 360.0f;

    moonOrbitAngle += 2.0f;
    if (moonOrbitAngle >= 360.0f) moonOrbitAngle -= 360.0f;

    glutPostRedisplay();
    glutTimerFunc(16, timer, 0); // ~60 FPS
}

void reshape(int w, int h) {
    if (h == 0) h = 1;
    float ratio = 1.0f * w / h;
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, ratio, 1.0, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Simple 3D Solar System");

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutTimerFunc(0, timer, 0);

    glutMainLoop();
    return 0;
}

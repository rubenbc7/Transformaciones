from OpenGL.GL import *
from glew_wish import *
import glfw

rotacion = 0.0

def dibujar():
    global rotacion
    #rutinas de dibujo
    #glColor3f(1.0,0.8,0.0)

    #glTranslatef(-0.5,0,0)
    #glRotatef(rotacion,1,1,1)
    #glScalef(-1,-1,-1)
    glPushMatrix()
    glTranslate(0.2,0.4,0)
    glRotate(rotacion,0,1,0)
    glBegin(GL_TRIANGLES)

    glColor3f(1,1,0.4)
    glVertex3f(0,0.2,0)
    glColor3f(0.8,0.8,0.3)
    glVertex3f(-0.2,-0.2,0)
    glColor3f(1,1,1)
    glVertex3f(0.2,-0.2,0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glRotate(rotacion,0,1,0)
    glBegin(GL_TRIANGLES)
    
    glColor3f(1,1,0.4)
    glVertex3f(0,0.2,0)
    glColor3f(0.8,0.8,0.3)
    glVertex3f(-0.2,-0.2,0)
    glColor3f(1,1,1)
    glVertex3f(0.2,-0.2,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.4,0,0)
    glRotate(rotacion,0,1,0)
    glBegin(GL_TRIANGLES)
    
    glColor3f(1,1,0.4)
    glVertex3f(0,0.2,0)
    glColor3f(0.8,0.8,0.3)
    glVertex3f(-0.2,-0.2,0)
    glColor3f(1,1,1)
    glVertex3f(0.2,-0.2,0)
    glEnd()
    glPopMatrix()

    
   # glPopMatrix()
    rotacion = rotacion + 2
    if rotacion > 360:
        rotacion = 0.0

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,600,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,600)
        #Establece color de borrado
        glClearColor(0.4,0.6,0.1,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()
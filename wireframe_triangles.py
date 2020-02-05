import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy


def main():

    # initialize glfw
    if not glfw.init():
        return
    #(width, height, title, monitor, share)
    window = glfw.create_window(600, 600, "My OpenGL window", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    # positions / vertex        
    triangle = [ 0.0,  0.0,
                 0.5,  0.0,
                 0.5,  0.5,
                 
                 0.0,  0.0,
                 0.0,  0.5, 
                -0.5,  0.5, 
                
                 0.0,  0.0,
                -0.5,  0.0,
                -0.5, -0.5,
                
                 0.0,  0.0,
                 0.0, -0.5,
                 0.5, -0.5]

    triangle = numpy.array(triangle, dtype = numpy.float32)

    vertex_shader = """
    #version 330
    in vec4 position;
    void main()
    {
        gl_Position = position;
    }
    """

    fragment_shader = """
    #version 330
    void main()
    {
       gl_FragColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
    }
    """
     
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

# Creating Vertex Buffer Object
    VBO = glGenBuffers(1)
# Making the VBO as active array buffer
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
# Copy the data to the buffer
    glBufferData(GL_ARRAY_BUFFER, 144, triangle, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 2, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(position)

    glUseProgram(shader)
    
    # background color
    glClearColor(1.0, 0.0, 0.0, 0.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_LINE_LOOP, 0,12)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()

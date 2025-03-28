import glfw

# Initialize the library
if not glfw.init():
    raise Exception("GLFW initialization failed")

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(640, 480, "Hello World", None, None)
if not window:
    glfw.terminate()
    raise Exception("GLFW window creation failed")

# Make the window's context current
glfw.make_context_current(window)

# Loop until the user closes the window
while not glfw.window_should_close(window):
    # Render here, e.g. using OpenGL
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()

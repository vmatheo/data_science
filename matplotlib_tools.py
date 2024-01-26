import matplotlib.pyplot as plt
import numpy as np

""" Plotting a single point in 3-D """
ax = plt.axes(projection='3d')  # Specifies dimension of matplotlib
ax.scatter(3, 5, 7)  # Specifies length of x,y,z axes in 3-D
plt.show()

""" Plotting multiple points in 3-D using numpy to generate data """
ax = plt.axes(projection='3d')
x_data = np.random.randint(0, 100, 100)  # Specify various different data
y_data = np.random.randint(0, 100, 100)
z_data = np.random.randint(0, 100, 100)
ax.scatter(x_data, y_data, z_data, s=100)  # s = specifies the size of points
ax.view_init(45, 45)  # Specify the direction you want to view the graph from
plt.show()

""" Plotting a flat function (no surface) """
ax = plt.axes(projection='3d')
x_data = np.arange(0, 50, 0.1)  # Define data
y_data = np.arange(0, 50, 0.1)
z_data = np.cos(x_data) * y_data  # Define the functional relationship
ax.plot(x_data, y_data, z_data)
ax.set_title("Function")  # Customize the graph as wanted
ax.set_xlabel("x-values")
ax.set_ylabel("y-vales")
plt.show()

""" Plotting a parametric equation """
ax = plt.axes(projection='3d')
z_data = np.linspace(0, 10, 20)  # Define z_data first
x_data = np.cos(z_data)  # Solve for x, y data backwards
y_data = np.sin(z_data)
ax.plot3D(x_data, y_data, z_data, lw=5)  # Can choose to make thicker line
plt.show()

""" Plotting a 3-D surface """
ax = plt.axes(projection='3d')
x_data = np.arange(-5, 5, 0.4)  # Create data
y_data = np.arange(-5, 5, 0.4)

X, Y = np.meshgrid(x_data, y_data)  # Create a grid of values instead of a number line
Z = np.cos(X)+np.sin(Y)  # Specify the functional relation
ax.plot_surface(X, Y, Z, cmap='jet')  # All sorts of different cmaps exist!
plt.show()

""" Plotting 3-D Wireframe structure """
ax = plt.axes(projection='3d')
x_data = np.linspace(-5, 5, 15)  # Create x,y data
y_data = np.linspace(-5, 5, 15)
X, Y = np.meshgrid(x_data, y_data)  # Put data into a grid for surface rendering
Z = 50 - (X**2 + Y**2)  # Define functional relationship
ax.plot_wireframe(X, Y, Z, color='black')  # Add extra features as wanted (like color)
plt.show()


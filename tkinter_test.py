import tkinter as tk
import math

# A simple function to project 3D points onto a 2D canvas
def project_point(x, y, z):
    # Assuming the camera is at (0, 0, -500) looking towards the origin
    camera_z = -500
    # Simple perspective projection formula
    projection_factor = 500 / (500 + z)
    x_2d = x * projection_factor
    y_2d = y * projection_factor
    return x_2d, y_2d

# Drawing function for our cube
def draw_cube(canvas, points):
    # List of points that make up the cube's edges
    edges = [(0, 1), (1, 3), (3, 2), (2, 0),  # front face
             (4, 5), (5, 7), (7, 6), (6, 4),  # back face
             (0, 4), (1, 5), (2, 6), (3, 7)]  # connecting lines
    
    # Draw each edge
    for edge in edges:
        point1 = points[edge[0]]
        point2 = points[edge[1]]
        
        # Project points onto 2D
        x1, y1 = project_point(*point1)
        x2, y2 = project_point(*point2)
        
        # Draw line on canvas
        canvas.create_line(x1 + 250, -y1 + 250, x2 + 250, -y2 + 250)

# Function to rotate a point around the X axis
def rotate_x(angle, point):
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    y = point[1] * cos_angle - point[2] * sin_angle
    z = point[1] * sin_angle + point[2] * cos_angle
    return (point[0], y, z)

# Function to rotate a point around the Y axis
def rotate_y(angle, point):
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    x = point[0] * cos_angle + point[2] * sin_angle
    z = -point[0] * sin_angle + point[2] * cos_angle
    return (x, point[1], z)

# Function to rotate a point around the Z axis
def rotate_z(angle, point):
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    x = point[0] * cos_angle - point[1] * sin_angle
    y = point[0] * sin_angle + point[1] * cos_angle
    return (x, y, point[2])
    
# Function to apply all three rotations to a point
def rotate_point(x_angle, y_angle, z_angle, point):
    return rotate_z(z_angle, rotate_y(y_angle, rotate_x(x_angle, point)))

# Set up the Tkinter window
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Define points of a cube
cube_points = [(-50, -50, -50), (50, -50, -50), (-50, 50, -50), (50, 50, -50),
               (-50, -50, 50), (50, -50, 50), (-50, 50, 50), (50, 50, 50)]


# Draw the cube
#draw_cube(canvas, cube_points)

angle_x, angle_y, angle_z = 0, 3, 3  # Rotation angles

# Rotate and draw the cube with the new angles
rotated_points = [rotate_point(angle_x, angle_y, angle_z, point) for point in cube_points]
draw_cube(canvas, rotated_points)

# Start the Tkinter loop
window.mainloop()

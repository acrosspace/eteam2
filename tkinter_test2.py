import tkinter as tk
import math

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

def draw():
    global angle_x, angle_y, angle_z
    canvas.delete("all")  # Clear the canvas

    # Rotate and draw the cube with the new angles
    rotated_points = [rotate_point(angle_x, angle_y, angle_z, point) for point in cube_points]
    draw_cube(canvas, rotated_points)

    # Update the angles for the next frame
    angle_x += 0.05
    angle_y += 0.05
    angle_z += 0.05

    window.after(33, draw)  # Schedule the next draw

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()

cube_points = [(-50, -50, -50), (50, -50, -50), (-50, 50, -50), (50, 50, -50),
               (-50, -50, 50), (50, -50, 50), (-50, 50, 50), (50, 50, 50)]

angle_x, angle_y, angle_z = 0, 0, 0  # Initial rotation angles

draw()  # Start the drawing loop

window.mainloop()

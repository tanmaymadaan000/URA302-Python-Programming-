# q1
# import tkinter as tk

# root = tk.Tk()
# root.title("Robot Control Panel")
# root.geometry("500x400")
# root.configure(bg="yellow")

# root.mainloop()

# q2
# import tkinter as tk


# root = tk.Tk()
# canvas = tk.Canvas(root, width=300, height=300)
# canvas.pack()

# # A point = tiny circle
# canvas.create_oval(100, 100, 103, 103, fill="black")

# root.mainloop()

# q3
# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()

# points = [20,50, 100,120, 180,90, 250,150]

# canvas.create_line(points, fill="blue", width=3)

# root.mainloop()

# q4
# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=200)
# canvas.pack()

# p = canvas.create_oval(10, 90, 30, 110, fill="red")

# x_speed = 2

# def move_point():
#     canvas.move(p, x_speed, 0)
#     root.after(20, move_point)

# move_point()
# root.mainloop()

# q5
# import tkinter as tk

# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=300)
# canvas.pack()

# # body
# canvas.create_rectangle(100, 100, 250, 150, fill="gray")

# # wheels
# canvas.create_oval(110, 150, 140, 180, fill="black")
# canvas.create_oval(210, 150, 240, 180, fill="black")

# root.mainloop()
# q6
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

robot = canvas.create_oval(150, 150, 170, 170, fill="red")

def move(dx, dy):
    canvas.move(robot, dx, dy)

tk.Button(root, text="Up", command=lambda: move(0, -10)).pack()
tk.Button(root, text="Down", command=lambda: move(0, 10)).pack()
tk.Button(root, text="Left", command=lambda: move(-10, 0)).pack()
tk.Button(root, text="Right", command=lambda: move(10, 0)).pack()

root.mainloop()


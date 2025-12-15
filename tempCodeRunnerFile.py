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
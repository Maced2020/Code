# this is a UI test


import tkinter as tk


root = tk.Tk()
root.title("My Windows UI")


label = tk.Label(root, text="Hello, Windows UI!")
label.pack()

button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked!"))
button.pack()


root.mainloop()
from tkinter import *

class Block():
    def __init__(self, root):
        background.create_text(100, 100, text="Hello")

class Item():
    def __init__(self, root):
        pass

root = Tk()

root.title("Minecraft Model Generator")
root.geometry("1024x640")
root.resizable(False, False)
root.update()

# Create background Image
backgroundImg = PhotoImage(file="bg_main.png")
background = Canvas(root, width=root.winfo_width(), height=root.winfo_height(), highlightthickness=0)
background.create_image(0, 0, anchor=NW, image=backgroundImg)
background.pack()

# Load Separate GUI Frames
Block(root)
Item(root)

root.mainloop()
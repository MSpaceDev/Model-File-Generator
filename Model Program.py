from tkinter import *

class Block():
    def __init__(self, root):
        self.frameBlock = Canvas(root, width=root.winfo_width(), height=root.winfo_height() / 2, highlightthickness=0)
        self.frameBlock.grid_propagate(False)
        self.frameBlock.grid(row=0)

class Item():
    def __init__(self, root):
        print(root.winfo_height() / 2)
        self.frameItem = Canvas(root, width=root.winfo_width(), height=root.winfo_height() / 2, highlightthickness=0, bg="red")
        self.frameItem.grid_propagate(False)
        self.frameItem.grid(row=1)

        self.label = Button(self.frameItem, text="Item")
        self.label.grid(row=1, column=10)

root = Tk()

root.title("Minecraft Model Generator")
root.geometry("1024x640")
root.resizable(False, False)
root.update()

# Load Separate GUI Frames
Block(root)
Item(root)

root.mainloop()
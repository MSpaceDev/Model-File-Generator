from tkinter import *

class CreateField():
    def __init__(self, name, x, y):
        self.name = name + ":"
        background.create_text(padX + x, padY + y - 3, text=self.name, font="Neoteric 15", fill="#9ababc", anchor=NW)
        self.entry = Entry(background, bg="#2f3136", fg="#9ababc", insertbackground="white")
        background.create_window(padX + x + 130, padY + y, window=self.entry, anchor=NW)

    def getValue(self):
        return self.entry.get()

class Block():
    def __init__(self, root):
        background.create_text(mainWidth / 2, padY / 2, text="MINECRAFT MODEL GENERATOR", font="Neoteric 30", fill="#9ababc", anchor=CENTER)
        background.create_rectangle(padX, padY, padX + length, padY + height, fill="#36393e", width=1)
        background.create_text(padX + 10, padY, text="Block Generator", font="Neoteric 20", fill="#808387", anchor=NW)

        self.modelNameEntry = CreateField("Model Name", 10, 50)
        self.textureNameEntry = CreateField("Texture Name", 10, 80)

        self.button = Button(background, text="Test", command=lambda: self.printEntry())
        background.create_window(400, 400, window=self.button)

    def printEntry(self):
        if(self.modelNameEntry.getValue() == "stone"):
            print("Is stone!!y")

class Item():
    def __init__(self, root):
        startX = padX
        startY = padY*2 + height
        background.create_rectangle(startX, startY, padX + length, padY*2 + height*2, fill="#36393e", width=1)
        background.create_text(startX + 10, startY, text="Item Generator", font="Neoteric 20", fill="#808387", anchor=NW)


# Main Program
root = Tk()

height = 250
padX = 50
padY = 50
sizeY = str(padY*3 + height*2)
size = str(1024)+"x"+sizeY

root.title("Minecraft Model Generator")
root.geometry(size)
root.resizable(False, False)
root.update()

# Setup global static variables
mainWidth = root.winfo_width()
mainHeight = root.winfo_height()
length = mainWidth - padX*2

# Create background
background = Canvas(root, width=mainWidth, height=mainHeight, highlightthickness=0, bg="#2f3136")
background.pack()

# Load Separate GUI Frames
Block(root)
Item(root)

root.mainloop()
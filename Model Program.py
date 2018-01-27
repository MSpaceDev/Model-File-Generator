from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import platform

class CreateCheckbox():
    def __init__(self, x, y, text, function, isChecked):
        self.isChecked = IntVar()
        self.checkbox = Checkbutton(background, text=text, bg="#36393e", activebackground="#36393e", bd=1,
                                       font="Neoteric 15", fg="#9ababc", activeforeground="#9ababc",
                                       selectcolor="#36393e", highlightbackground="#36393e", command=lambda: function(),
                                       variable=self.isChecked, disabledforeground="#808387"
                                    )
        background.create_window(x, y, window=self.checkbox, anchor=NW)

        if (isChecked == True):
            self.checkbox.select()

    def setState(self, state):
        if(state == "disabled"):
            self.checkbox.config(state=DISABLED)
        elif (state == "normal"):
            self.checkbox.config(state=NORMAL)
        else:
            print("Improper state provided")

class CreateField():
    def __init__(self, x, y, name, state=True, defaultText="", charWidth=20, distance=130):
        self.name = name + ":"
        self.text = background.create_text(x, y - 3, text=self.name, font="Neoteric 15", fill="#9ababc", anchor=NW)

        self.entry = Entry(background, bg="#2f3136", fg="#9ababc", insertbackground="white", insertborderwidth=1,
                           disabledbackground="#25262b", disabledforeground="#808387", highlightthickness=0,
                           width=charWidth, textvariable=StringVar(root, defaultText)
                           )

        background.create_window(x + distance, y, window=self.entry, anchor=NW)

        if (state == False):
            self.setState("disabled")

    def getValue(self):
        return self.entry.get()

    def setState(self, state):
        if(state == "disabled"):
            self.entry.config(state=DISABLED, relief=FLAT)
            background.itemconfig(self.text, fill="#808387")
        elif(state == "normal"):
            self.entry.config(state=NORMAL, relief=SUNKEN)
            background.itemconfig(self.text, fill="#9ababc")
        else:
            print("Improper state provided")

class CreateButton():
    color = "#ffffff"

    def __init__(self, x, y, sizeX, sizeY, text, color, textColor, font, function):
        self.color = color

        # Create button graphic
        self.buttonBG = background.create_rectangle(x, y, x + sizeX, y + sizeY, fill=color)
        self.buttonText = background.create_text(x + sizeX/2, y + sizeY/2, text=text, fill=textColor, font=font)

        # Button Events
        background.tag_bind(self.buttonBG, "<Button-1>", self.buttonAnims)
        background.tag_bind(self.buttonText, "<Button-1>", self.buttonAnims)
        background.tag_bind(self.buttonBG, "<Enter>", self.buttonAnims)
        background.tag_bind(self.buttonText, "<Enter>", self.buttonAnims)
        background.tag_bind(self.buttonBG, "<Leave>", self.buttonAnims)
        background.tag_bind(self.buttonText, "<Leave>", self.buttonAnims)
        background.tag_bind(self.buttonBG, "<ButtonRelease-1>", self.buttonAnims)
        background.tag_bind(self.buttonText, "<ButtonRelease-1>", self.buttonAnims)

        background.tag_bind(self.buttonBG, "<Button-1>", lambda x: function())
        background.tag_bind(self.buttonText, "<Button-1>", lambda x: function())

    def buttonAnims(self, event):
        if (event.type == EventType.Enter):
            background.itemconfig(self.buttonBG, fill="#202225")
        elif (event.type == EventType.Leave):
            background.itemconfig(self.buttonBG, fill=self.color)
        elif (event.type == EventType.ButtonPress):
            background.itemconfig(self.buttonBG, fill=self.color)
        elif (event.type == EventType.ButtonRelease):
            background.itemconfig(self.buttonBG, fill="#202225")

class Block():
    def __init__(self, root):
        ### Seperators and borders ###
        background.create_rectangle(padX, padY, padX + length, padY + height, fill="#36393e", width=1)
        background.create_line(padX + 290, padY + 10, padX + 290, padY + height - 10)
        background.create_line(padX + 595, padY + 10, padX + 595, padY + height - 10)

        ### Text ###
        background.create_text(padX + 10, padY, text="Block Generator", font="Neoteric 20", fill="#808387", anchor=NW)
        background.create_text(padX + 700, padY, text="Animation Properties", font="Neoteric 10 underline", fill="#808387", anchor=NW)
        background.create_text(padX + 700, padY + 177, text="Texture Properties", font="Neoteric 10 underline", fill="#808387", anchor=NW)

        ### Entries ###
        # Main Properties
        self.modelNameEntry = CreateField( padX + 10, padY + 50, "Model Name")
        self.textureNameEntry = CreateField(padX + 10, padY + 80, "Texture Name")
        self.modNameEntry = CreateField(padX + 10, padY + 110, "Mod Name")
        # Different Sided Properties
        self.up = CreateField(padX + 315, padY + 95, "Up", False)
        self.down = CreateField(padX + 315, padY + 120, "Down", False)
        self.north = CreateField(padX + 315, padY + 145, "North", False)
        self.south = CreateField(padX + 315, padY + 170, "South", False)
        self.east = CreateField(padX + 315, padY + 220, "East", False)
        self.west = CreateField(padX + 315, padY + 195, "West", False)
        # Animation Properties
        self.frameWidth = CreateField(padX + 615, padY + 50, "Width", True, "1", 7, 75)
        self.frameHeight = CreateField(padX + 750, padY + 50, "Height", True, "1", 7, 75)
        self.speed = CreateField(padX + 615, padY + 75, "Frame Speed", True, "1")
        self.frameIndex = CreateField(padX + 615, padY + 130, "Frame Index", False)
        self.frameSpeed = CreateField(padX + 615, padY + 155, "Frame Speed", False)

        ### Checkboxes ###
        self.isAnimation = CreateCheckbox(padX + 310, padY + 5, "Is Animation", self.printEntry, False)
        self.genItemBlock = CreateCheckbox(padX + 310, padY + 30, "Generate ItemBlock", self.printEntry, True)
        self.differentSided = CreateCheckbox(padX + 310, padY + 55, "Is model differently sided", self.toggleSideEntries, False)

        self.interpolate = CreateCheckbox(padX + 615, padY + 15, "Interpolate", self.passFunc, False)
        self.customSpeed = CreateCheckbox(padX + 615, padY + 95, "Custom Frame Speeds", self.toggleFrameEntries, False)
        self.blur = CreateCheckbox(padX + 615, padY + 185, "Blur", self.toggleFrameEntries, False)
        self.clamp = CreateCheckbox(padX + 615, padY + 210, "Clamp", self.toggleFrameEntries, False)

        ### Buttons ###
        self.button = CreateButton(padX + 45, padY + height - 100, 200, 75, "GENERATE!", "#3d4046", "#9ababc", "Neoteric 30", self.printEntry)

    def printEntry(self):
        print("Function run")
        pass
        # self.filename = askopenfilename(initialdir=os.path.expanduser("~") + "/Desktop/",
        #                                 filetypes =(("PNG", "*.png"), ("JPEG", "*.jpg"),("All Files","*.*")),
        #                                 title = "Choose a file")

    def passFunc(self):
        pass

    def toggleFrameEntries(self):
        if(self.customSpeed.isChecked.get() == 0):
            self.frameIndex.setState("disabled")
            self.frameSpeed.setState("disabled")
            self.speed.setState("normal")
        else:
            self.frameIndex.setState("normal")
            self.frameSpeed.setState("normal")
            self.speed.setState("disabled")

    def toggleSideEntries(self):
        if(self.differentSided.isChecked.get() == 0):
            self.up.setState("disabled")
            self.down.setState("disabled")
            self.north.setState("disabled")
            self.south.setState("disabled")
            self.east.setState("disabled")
            self.west.setState("disabled")
        else:
            self.up.setState("normal")
            self.down.setState("normal")
            self.north.setState("normal")
            self.south.setState("normal")
            self.east.setState("normal")
            self.west.setState("normal")

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
background.create_text(mainWidth / 2, padY / 2, text="MINECRAFT MODEL GENERATOR", font="Neoteric 30", fill="#9ababc", anchor=CENTER)

# Load Separate GUIs
Block(root)
Item(root)

root.mainloop()
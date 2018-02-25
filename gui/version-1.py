from tkinter import *
from PIL import Image, ImageTk
from numpy import array


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Manipulation GUI")
        self.root.minsize(width=500, height=500)

        # ***** globals *****
        self.imageString = ""
        self.image = None
        self.photo = None
        self.data = None
        self.red = None
        self.green = None
        self.blue = None
        self.alpha = None

        # ***** menu bar *****
        self.mainMenu = Menu(self.root)
        self.root.config(menu=self.mainMenu)

        self.fileMenu = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Open Image...", command=self.openImage)
        self.fileMenu.add_command(label="Close Image...", command=self.closeImage)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quit", command=self.quit)

        self.editMenu = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Undo", command=self.undo)

        # ***** content frame *****
        self.contentFrame = Frame(self.root)
        self.contentFrame.pack(expand=True, fill=BOTH)

        # ***** left frame *****
        self.leftFrame = Frame(self.contentFrame, bg="black")
        self.leftFrame.pack(side=LEFT, expand=True, fill=BOTH)

        self.imageLabel = Label(self.leftFrame, bg="black")
        self.imageLabel.pack(expand=True)

        # ***** right frame *****
        self.rightFrame = Frame(self.contentFrame, bg="green")
        self.rightFrame.pack(side=RIGHT, fill=Y, expand=False, padx=10, pady=10)

        self.fileLabel = Label(self.rightFrame, text="Enter filename:")
        self.fileLabel.grid(row=0, sticky=W+E)

        self.fileEntry = Entry(self.rightFrame)
        self.fileEntry.bind('<Return>', self.openImage)
        self.fileEntry.grid(row=1)

        self.openButton = Button(self.rightFrame, text="Open Image", command=self.openImage)
        self.openButton.grid(row=2, sticky=W+E)

        self.openButton = Button(self.rightFrame, text="Close Image", command=self.closeImage)
        self.openButton.grid(row=3, sticky=W+E)

        self.separator1 = Frame(self.rightFrame, relief=RIDGE, height=30, bg="white")
        self.separator1.grid(row=4, sticky=W+E)

        self.redLabel = Label(self.rightFrame, text="Red Mask: ")
        self.redLabel.grid(row=5, sticky=W+E)

        self.redSlider = Scale(self.rightFrame, from_=0, to=255, orient=HORIZONTAL)
        self.redSlider.set(240)
        self.redSlider.grid(row=6, sticky=W+E)

        self.separator2 = Frame(self.rightFrame, relief=RIDGE, height=30, bg="white")
        self.separator2.grid(row=7, sticky=W+E)

        self.quitButton = Button(self.rightFrame, text="Quit", command=self.quit)
        self.quitButton.grid(row=8, sticky=W+E)

        # ***** status bar *****
        self.status = Label(self.root, text="No Image Open", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def openImage(self, event=None):
        self.imageString = self.fileEntry.get()
        if "." not in self.imageString:
            self.imageString += ".jpg"
        self.status.configure(text="Opening " + self.imageString)
        if self.imageString == "":
            pass
        else:
            try:
                self.image = Image.open(self.imageString)
                self.photo = ImageTk.PhotoImage(self.image)
                self.imageLabel.configure(image=self.photo)
                self.status.configure(text="Editing " + self.imageString)
            except FileNotFoundError as e:
                self.status.configure(text="File not found")

    def closeImage(self):
        self.status.configure(text="No Image Open")
        self.fileEntry.delete(0, END)
        self.imageLabel.configure(image="")

    def quit(self):
        self.root.quit()

    def undo(self):
        print("undoing your shit")

    def imageManipulation(self):
        self.data = array(self.image)
        [self.red, self.green, self.blue, self.alpha] = self.data.T


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Main().run()

"""
# TODO
Feature list
- before after shots (under the main image?)
- set background color for image
- sliders, masking?
- adding borders to pictures
- cropping?
- export to exe
- do something with status bar
    - name of image loaded
- file extension optional
"""

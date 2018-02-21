from tkinter import *
from PIL import Image, ImageTk
from numpy import array


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Manipulation GUI")
        self.root.minsize(width=500, height=500)
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))

        # ***** globals *****
        self.imageString = ""
        self.image = None
        self.photo = None
        self.data = None
        self.redData = None
        self.greenData = None
        self.blueData = None
        self.alphaData = None
        self.redMask = 220
        self.greenMask = 220
        self.blueMask = 220
        self.alphaMask = 255
        self.maskBoolean = BooleanVar(value=True)

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
        self.leftFrame = Frame(self.contentFrame, bg="grey")
        self.leftFrame.pack(side=LEFT, expand=True, fill=BOTH)

        self.imageLabel = Label(self.leftFrame, bg="grey")
        self.imageLabel.pack(expand=True)

        # ***** right frame *****
        self.rightFrame = Frame(self.contentFrame)
        self.rightFrame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

        # ***** top right frame *****
        self.topRightFrame = Frame(self.rightFrame)
        self.topRightFrame.pack(side=TOP)

        self.fileLabel = Label(self.topRightFrame, text="Enter filename:")
        self.fileLabel.pack(fill=X, expand=True)

        self.fileEntry = Entry(self.topRightFrame)
        self.fileEntry.bind('<Return>', self.openImage)
        self.fileEntry.pack(fill=X, expand=True)

        self.openButton = Button(self.topRightFrame, text="Open Image", command=self.openImage)
        self.openButton.pack(fill=X, expand=True)

        self.closeButton = Button(self.topRightFrame, text="Close Image", command=self.closeImage)
        self.closeButton.pack(fill=X, expand=True)

        # ***** middle right frame *****
        self.middleRightFrame = Frame(self.rightFrame)
        self.middleRightFrame.pack(side=TOP, fill=X, pady=30)

        self.redLabel = Label(self.middleRightFrame, text="RGBA Sliders")
        self.redLabel.pack(fill=X, expand=True)

        self.redSlider = Scale(self.middleRightFrame, from_=0, to=255, orient=HORIZONTAL, bg="red")
        self.redSlider.set(self.redMask)
        self.redSlider.pack(fill=X, expand=True)

        self.greenSlider = Scale(self.middleRightFrame, from_=0, to=255, orient=HORIZONTAL, bg="green")
        self.greenSlider.set(self.greenMask)
        self.greenSlider.pack(fill=X, expand=True)

        self.blueSlider = Scale(self.middleRightFrame, from_=0, to=255, orient=HORIZONTAL, bg="blue")
        self.blueSlider.set(self.blueMask)
        self.blueSlider.pack(fill=X, expand=True)

        self.alphaSlider = Scale(self.middleRightFrame, from_=0, to=255, orient=HORIZONTAL, bg="black", fg="white")
        self.alphaSlider.set(self.alphaMask)
        self.alphaSlider.pack(fill=X, expand=True)

        self.maskButton = Checkbutton(self.middleRightFrame, text="Above Slider Values", variable=self.maskBoolean)
        self.maskButton.pack(fill=X, expand=True)

        self.manipulateButton = Button(self.middleRightFrame, text="Manipulate", command=self.imageManipulation)
        self.manipulateButton.pack(fill=X, expand=True)

        # ***** bottom right frame *****
        self.bottomRightFrame = Frame(self.rightFrame, bg="red")
        self.bottomRightFrame.pack(side=BOTTOM, fill=X)

        self.quitButton = Button(self.bottomRightFrame, text="Quit", command=self.quit)
        self.quitButton.pack(fill=X, expand=True)

        # ***** status bar *****
        self.status = Label(self.root, text="No Image Open", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def openImage(self, event=None):
        self.imageString = self.fileEntry.get()
        if "." not in self.imageString and not self.imageString == "":
            self.imageString += ".jpg"
        if self.imageString == "":
            self.closeImage()
            self.status.configure(text="No Image Open" + self.imageString)
        else:
            try:
                self.status.configure(text="Opening " + self.imageString)
                self.image = Image.open(self.imageString)
                self.photo = ImageTk.PhotoImage(self.image)
                self.imageLabel.configure(image=self.photo)
                self.status.configure(text="Editing " + self.imageString)
            except FileNotFoundError:
                self.closeImage()
                self.status.configure(text="File not found: " + self.imageString)

    def closeImage(self):
        self.status.configure(text="No Image Open")
        self.fileEntry.delete(0, END)
        self.imageLabel.configure(image="")

    def quit(self):
        self.root.quit()

    def undo(self):
        print("undoing your shit")

    def imageManipulation(self):
        self.editedImage = self.image.convert('RGBA')
        self.data = array(self.editedImage)
        [self.redData, self.greenData, self.blueData, self.alphaData] = self.data.T

        self.redMask = self.redSlider.get()
        self.greenMask = self.greenSlider.get()
        self.blueMask = self.blueSlider.get()
        self.alphaMask = self.alphaSlider.get()

        # creates a mask for pixels that fit user defined parameters
        if self.maskBoolean.get():
            mask = (self.redData >= self.redMask) & (self.greenData >= self.greenMask) & (self.blueData >= self.blueMask) & (self.alphaData >= self.alphaMask)
        else:
            mask = (self.redData <= self.redMask) & (self.greenData <= self.greenMask) & (self.blueData <= self.blueMask) & (self.alphaData >= self.alphaMask)

        # alters pixels included in the mask to be transparent
        self.data[mask.T] = (0, 0, 0, 0)

        # converts four interconnected arrays back into image interpretation
        self.editedImage = Image.fromarray(self.data)
        self.photo = ImageTk.PhotoImage(self.editedImage)
        self.imageLabel.configure(image=self.photo)

        # creates a new file name based on the input and saves the edited image under that name
        outputFile = self.imageString[0:len(self.imageString) - 4] + "_edited.png"
        self.editedImage.save(outputFile)
        self.status.configure(text="Image saved as " + outputFile)

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
- path to image
    - open directory to do several images
    - batch image option
"""

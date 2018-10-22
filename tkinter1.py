from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text='Exit', command=self.clickExitButton)

        exitButton.place(x=0, y=0)

    def clickExitButton(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title('Tkinter window')
root.geometry('320x200')
root.mainloop()
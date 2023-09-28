
from tkinter import Tk

class gui:

    def __init__(self):
        self.window=Tk()

    def run(self):
        self.window.mainloop()


if __name__=="__main__":
    v=gui()
    v.run()

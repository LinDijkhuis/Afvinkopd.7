import tkinter
from tkinter import messagebox

class GUI:
    def __init__(self):
        # Creeer de main window
        self.main_window = tkinter.Tk()
        self.main_window.title("GUI")

        # Maak de twee frames voor checkbox en de buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # We maken drie intvar objecten voor checkbuttens
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # Zet de drie intvar objecten naar 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # Checkbuttons aanmaken
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text="Ei met spek",
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text="Cereal",
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text="Toast",
                                       variable=self.cb_var3)

        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text="OK",
                                        command=self.showresults)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="QUIT",
                                          command=self.main_window.destroy)


        # Pack items
        # Frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        # Buttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.ok_button.pack()
        self.quit_button.pack()
        # Geef de main window weer
        tkinter.mainloop()

    def showresults(self):
        self.message = "U wilt graag voor ontbijt: \n"
        if self.cb_var1.get() == 1:
            self.message = self.message + "Ei met spek\n"
        if self.cb_var2.get() == 1:
            self.message = self.message + "Cereal\n"
        if self.cb_var3.get() == 1:
            self.message = self.message + "Toast"
        tkinter.messagebox.showinfo("Ontbijt", self.message)

if __name__ == '__main__':
    gui = GUI()
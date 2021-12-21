# import matplotlib.pyplot as plt
# import tkinter
# from tkinter import messagebox
#
# class GUI:
#     def __init__(self):
#         # Creeer de main window
#         self.main_window = tkinter.Tk()
#         self.main_window.title("GUI")
#
#         # Maak de twee frames voor checkbox en de buttons
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.bottom_frame = tkinter.Frame(self.main_window)
#
#         # We maken drie intvar objecten voor checkbuttens
#         self.cb_var3 = tkinter.IntVar()
#
#         # Zet de drie intvar objecten naar 0
#         self.cb_var3.set(0)
#
#         # Checkbuttons aanmaken
#         self.cb3 = tkinter.Checkbutton(master=self.main_window,
#                                        height=2,
#                                        width=10,
#                                        text="plot")
#
#         self.ok_button = tkinter.Button(self.bottom_frame,
#                                         text="OK",
#                                         command=self.showresults)
#         self.quit_button = tkinter.Button(self.bottom_frame,
#                                           text="QUIT",
#                                           command=self.main_window.destroy)
#
#
#         # Pack items
#         # Frames
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         # Buttons
#         self.cb3.pack()
#         self.ok_button.pack()
#         self.quit_button.pack()
#         # Geef de main window weer
#         tkinter.mainloop()
#
#     # def showresults(self):
#     #     self.message =
#
# if __name__ == '__main__':
#     gui = GUI()
#
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


# plot function is created for
# plotting the graph in
# tkinter window
def plot():
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    # list of squares
    y = [i ** 2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x500")

# button that displays the plot
plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()

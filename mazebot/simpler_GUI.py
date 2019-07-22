from tkinter import *


class UserInterface(Frame):

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.geometry('500x500')

        # Variables that will be needed by the maze
        self.min_value = 0
        self.max_value = 100
        self.paths = []

        # Window Title
        self.master.title('Maze Solver')

        # Minimum size for maze
        self.min_label = Label(master=master, text='Choose the minimum size of the maze')
        self.min_label.pack()

        self.min_slider = Scale(orient='horizontal', from_=0, to=100)
        self.min_slider.pack()

        # Maximum size for maze
        self.max_label = Label(master=master, text='Choose the maximum size of the maze')
        self.max_label.pack()

        self.max_slider = Scale(orient='horizontal', from_=0, to=100)
        self.max_slider.pack()

        # Checkboxes for which paths to show
        self.path_label = Label(master=master, text='Choose which paths you would like to see')
        self.path_label.pack()

        self.condensed_path = Checkbutton(master=master, text='Condensed Path')
        self.condensed_path.pack()

        self.full_path = Checkbutton(master=master, text='Full Path')
        self.full_path.pack()

        # Start button
        self.start = Button(master=master, text='START', command=self.start)
        self.start.pack()

    def start(self):
        """
        Starts maze solver
        :return:
        """
        self.min_value = self.min_slider.get()
        self.max_value = self.max_slider.get()

        self.
        print('button pressed')

from tkinter import *
import tkinter.font as TkFont


class UserInterface(Frame):

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.geometry('500x500')
        #self.master.configure(bg='black')
        self.custom_font = TkFont.Font(family='Helvetica', size=20)
        self.slider_length = 200

        # Variables that will be needed by the maze
        self.min_value = 10
        self.max_value = 100
        self.show_full_path = False
        self.show_condensed_path = False

        # Window Title
        self.master.title('MazeBot Settings')

        # Minimum size for maze
        self.min_label = Label(master=master, text='Choose the minimum size of the maze', font=self.custom_font)
        self.min_label.pack()

        self.min_slider = Scale(orient='horizontal', from_=self.min_value, to=self.max_value, length=self.slider_length)
        self.min_slider.set(10)
        self.min_slider.pack()

        # Maximum size for maze
        self.max_label = Label(master=master, text='Choose the maximum size of the maze', font=self.custom_font)
        self.max_label.pack()

        self.max_slider = Scale(orient='horizontal', from_=self.min_value, to=self.max_value, length=self.slider_length)
        self.max_slider.set(100)
        self.max_slider.pack()

        # Checkboxes for which paths to show
        self.path_label = Label(master=master, text='Choose which paths you would like to see', font=self.custom_font)
        self.path_label.pack()

        self.condensed = IntVar()
        self.condensed.set(1)
        self.condensed_path = Checkbutton(master=master, text='Condensed Path', variable=self.condensed, font=self.custom_font)
        self.condensed_path.pack()

        self.full = IntVar()
        self.full_path = Checkbutton(master=master, text='Full Path', variable=self.full, font=self.custom_font)
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

        if self.condensed.get():
            self.show_condensed_path = True
        if self.full.get():
            self.show_full_path = True

        self.master.destroy()

        print('button pressed')



root = Tk()
ui = UserInterface(root)
root.mainloop()
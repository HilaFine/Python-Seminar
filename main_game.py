import tkinter as tk
from tkinter import messagebox


class ComputerLayer:
    """
    A class use to build the frames and the labels of the computer
    ...
    Methods
    -------
    __init__(self, computer_layer, number)
    computer_header_layer(self, size)
    playing_grid(self)
    """

    """ The function is building ComputerLayer, constructor 
    :parameters: self: the function gets self as a parameter
    computer_layer: the frame of the layer
    number: the id number of the computer
    :returns: the function do not return any value
    """

    def __init__(self, computer_layer, computer_number):
        self.number_label = None
        self.frame = computer_layer
        self.computer_number = computer_number
        self.top_grid = tk.Frame(
            master=self.frame,
            relief=tk.RIDGE,
            borderwidth=2
        )

    """ The function is building the label of the computer layer
    :parameters: self: the function gets self as a parameter
    size: the label size
    :returns: the function do not return any value
    """

    def computer_header_layer(self, size):
        tk.Label(
            master=self.frame,
            text=f"Computer {self.computer_number}",
            justify="center", font=f"BOLD {size}") \
            .pack()

    """ The function is building the ComputerLayer grid 
    :parameters: self: the function gets self as a parameter
    :returns: the function do not return any value
    """

    def playing_grid(self):
        self.number_label = tk.Label(self.top_grid, text=f"The number is:PRESS START", relief=tk.RIDGE)
        b_label = tk.Label(self.top_grid, text="B", relief=tk.RIDGE, width=10)
        h_label = tk.Label(self.top_grid, text="H", relief=tk.RIDGE, width=10)
        self.top_grid.pack(fill=tk.BOTH)
        self.top_grid.columnconfigure(index=[0, 1, 2], weight=1, minsize=5)
        self.number_label.grid(row=0, column=0, sticky="w")
        b_label.grid(row=0, column=1, sticky="e")
        h_label.grid(row=0, column=2, sticky="e")


class InfoLayer:
    """
    A class use to build the frames and the labels of the bottom layer
    ...
    Methods
    -------
    __init__(self, info_layer, text, label)
    def info_grid(self)
    """

    """ The function is building InfoLayer, constructor 
    :parameters: self: the function gets self as a parameter
    info_layer: 
    text:
    label:
    :returns: the function do not return any value
    """

    def __init__(self, info_layer, text, label):
        self.frame = info_layer
        self.text = text
        self.btn = tk.Button(master=self.frame, text="Start")
        self.label_computer = label

    """ The function is building the InfoLayer grid
    :parameters: self: the function gets self as a parameter
    :returns: the function do not return any value
    """

    def info_grid(self):
        self.frame.columnconfigure([0, 1], weight=1, minsize=250)
        self.frame.rowconfigure(0, weight=1, minsize=100)
        self.label_computer = tk.Label(master=self.frame, text=self.text, width=40)
        self.label_computer.grid(row=0, column=0)
        self.btn.grid(row=0, column=1, sticky="news")


class TopLayer:
    """
    A class use to build the frames and the labels of the top window ( the window where the game is representing,
    all the players moves) ... Methods ------- __init__(self, top_frame): add_info(self, guessed_number,
    number_guess, number_bulls, number_hits):
     The function is building TopLayer, constructor
    :parameters: self: the function gets self as a parameter
    top_frame: the top frame
    :returns: the function do not return any value
    """

    def __init__(self, top_frame):
        self.computer_2_layer = ComputerLayer(
            tk.Frame(master=top_frame, width=200, borderwidth="2", relief=tk.RIDGE, height=200), 2)
        self.computer_1_layer = ComputerLayer(
            tk.Frame(master=top_frame, width=200, borderwidth="2", relief=tk.RIDGE, height=200), 1)
        self.top_frame = top_frame

    """ The function is adding information to the frame that show a move in the game (a guess of the player)
    :parameters: self: the function gets self as a parameter
    guessed_number: the number that the player is guessing
    number_guess: number of  guesses the player was trying to guess (including this)
    number_bulls: number of bulls in the guess
    number_hits: number of hits in the guess
    :returns: the function do not return any value
    """

    def add_info(self, layer, guessed_number, table_size, number_guess, number_bulls, number_hits):
        temp_layer = 0
        if layer == 1:
            temp_layer = self.computer_1_layer.frame
        if layer == 2:
            temp_layer = self.computer_2_layer.frame

        new_frame = tk.Frame(
            master=temp_layer,
            relief=tk.RIDGE,
            borderwidth=2,
        )
        label_guess = tk.Label(master=new_frame,
                               text=f"Guess-{number_guess}:Number-{guessed_number}\n[Table Size:{table_size}]",
                               height=4)
        label_bh = tk.Label(master=new_frame, text=f"{number_bulls}", width=5)
        label_bn = tk.Label(master=new_frame, text=f"{number_hits}", justify="center", width=10)
        new_frame.pack(fill=tk.BOTH)
        new_frame.columnconfigure(index=[0, 1, 2], weight=1, minsize=5)
        label_guess.grid(row=0, column=0, sticky="w")
        label_bh.grid(row=0, column=1, sticky="e")
        label_bn.grid(row=0, column=2, sticky="e")


class BottomLayer:
    """
    A class use to build the frames and the labels of the bottom window
    ...
    Methods
    -------
    __init__(self, bottom_frame):
    
    """

    """ The function is building BottomLayer, constructor 
    :parameters: self: the function gets self as a parameter
    top: the top frame
    bottom_frame: the bottom frame 
    :returns: the function do not return any value
    """

    def __init__(self, bottom_frame):
        self.info_layer = InfoLayer(info_layer=bottom_frame, label=None, text="Start the game by pressing START =>")
        self.bottom_frame = bottom_frame


class MainWindow:
    """
    A class use to represent the main window of the game
    ...
    Methods
    -------
    __init__(self, top, bottom)
    top_window(self, number_1)
    bottom_window(self)
    """

    """ The function is building MainWindow, constructor 
    :parameters: self: the function gets self as a parameter
    top: the top frame
    bottom: the bottom frame
    :returns: the function do not return any value
    """

    def __init__(self, top, bottom):
        self.top = TopLayer(top_frame=top)
        self.bottom = BottomLayer(bottom_frame=bottom)
        self.top.top_frame.pack(fill=tk.BOTH, expand=True)
        self.bottom.bottom_frame.pack(fill=tk.BOTH)

    """ The function is building the top window where computer 1 and computer 2 game is displaying,
     where the game is represent, all the players moves  
    :parameters: self: the function gets self as a parameter
    number_1: the random number (4 digits) you need to guess for the game
    :returns: the function do not return any value
    """

    def top_window(self):
        # Computer 1

        self.top.computer_1_layer.guess_number = ""
        self.top.computer_1_layer.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.top.computer_2_layer.guess_number = ""

        self.top.computer_2_layer.frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.top.computer_1_layer.computer_header_layer(25)
        self.top.computer_1_layer.playing_grid()
        # Computer 2
        self.top.computer_2_layer.computer_header_layer(25)
        self.top.computer_2_layer.playing_grid()

    """ The function is building the bottom window of the main window
    :parameters: self: the function gets self as a parameter
    :returns: the function do not return any value
    """

    def bottom_window(self):
        self.bottom.info_layer.info_grid()


def stats_open(data_bases, window):
    if data_bases[0].number_of_games != 0:
        window.destroy()
        stats = StatsWindow()
        for data_base in data_bases:
            stats.create_starts(data_base=data_base)
        stats.window.mainloop()
    else:
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()


class DisplayGame:
    """
    A class use to set up the game display, the windows
    ...
    Attributes
    ----------
    window : create a main window
    
    Methods
    -------
    __init__(self)
    display(self, number_1)
    """

    window = tk.Tk()
    window.title("Game Screen")

    """ The function building DisplayGame, constructor
    :parameters: self: the function gets self as a parameter
    :returns: the function do not return any value
    """

    def __init__(self):
        self.main_window = MainWindow(bottom=tk.Frame(
            master=self.window,
            height=150,
            relief=tk.RIDGE,
            borderwidth=2
        ), top=tk.Frame(
            master=self.window,
            height=100,
            border=1
        ))

    """ The function building the display of the game
    after we press the button of the start menu
    :parameters: self: the function gets self as a parameter
    number_1: the random number (4 digits) you need to guess for the game
    :returns: the function do not return any value
    """

    def display(self):
        self.window.geometry("800x800")
        self.main_window.top_window()
        self.main_window.bottom_window()
        self.window.mainloop()


class StatsWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Stats")
        self.window.geometry("400x400")

        # Average of guess pre game
        # Number of wins
        # Number of draws
        # Number of games
        pass

    def create_starts(self, data_base):
        tk.Label(
            master=self.window,
            text=data_base.player,
            justify="center", font=f"BOLD {25}") \
            .pack()
        label_list = ["Average guess", "Wins", "Draws", "Games"]
        frame = tk.Frame(master=self.window, borderwidth="2", relief=tk.RIDGE)
        frame.columnconfigure([0, 1, 2, 3], weight=1, minsize=100)
        frame.rowconfigure([0, 1], weight=1, minsize=40)
        frame.pack()
        for j in range(4):
            label = tk.Label(master=frame, text=label_list[j], justify="center", relief=tk.RIDGE, width=10)
            label.grid(row=0, column=j)
        if data_base.number_of_games != 0:
            tk.Label(master=frame, text=data_base.average_calculator(), justify="center", width=10).grid(row=1,
                                                                                                         column=0)
            tk.Label(master=frame, text=data_base.number_of_wins, justify="center", width=10).grid(row=1, column=1)
            tk.Label(master=frame, text=data_base.number_of_draws, justify="center", width=10).grid(row=1, column=2)
            tk.Label(master=frame, text=data_base.number_of_games, justify="center", width=10).grid(row=1, column=3)

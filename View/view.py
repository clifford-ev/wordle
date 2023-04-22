# import tkinter as tk
# import tkinter.ttk as ttk
# import tkinter.messagebox
import sv_ttk



class View():
    """Parent for all GUI classes. Provides class attributes for theme, color, etc.
    """
    # Reads file of allowed guesses into guess_list.
    with open("allowed_guesses.txt") as f:
        guess_list = f.read().splitlines()

    # Reference letters for keyboard.
    top_letters = {"Q" : 0, "W" : 1, "E" : 2, "R" : 3, "T" : 4, "Y" : 5, "U" : 6, "I" : 7, "O" : 8, "P" : 9}
    mid_letters = {"A" : 0, "S" : 1, "D" : 2, "F" : 3, "G" : 4, "H" : 5, "J" : 6, "K" : 7, "L" : 8}
    bottom_letters = {"Z" : 0, "X" : 1, "C" : 2, "V" : 3, "B" : 4, "N" : 5, "M" : 6}

    color_dict = {  # Reference for letter colors.
         0: "#797c7e",
         1: "#c5b35d",
         2: "#76a866"
    }
    # Theme defaults to light at startup.
    theme_setting = "light"
    bg_theme = "#ffffff"

    def __init__(self, controller) -> None:
        self.current_guess = ""
        self.controller = controller

    def run(self, window):
        """Starts the event loop for window.

        Args:
            window (Tk): Tk object/window
        """
        window.mainloop()

    def switch_theme(self):
        sv_ttk.set_theme(self.theme_setting)
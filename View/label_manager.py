import tkinter as tk
import tkinter.ttk as ttk
from View.view import View

class LabelManager(View):
    """Creates and updates the labels that display current and previous guesses.
    """
    def __init__(self, controller, main_gui) -> None:
        super().__init__(controller)
        self.main_gui = main_gui

    def guess_labels(self):
        """Generates and displays an array of labels that contain current and previous guesses.
        """
        self.label_list = []

        for i in range(6):  # Loops for each row of labels.
            # Generates a label for each letter slot in a row.
             self.label_list.append([
                ttk.Label(
                 text="", width=3, font=14, background=View.bg_theme, master=self.main_gui.frame, anchor="center")
                for x in range(5)])

             for j in range(5): # Repeats each letter in a row.
                self.label_list[i][j].place(x=(300 + 50*j), y=(100 + 50*i), anchor="center")  # Places labels.

    def update_guess_labels(self, guess_num, guessed_letters):
        """Updates labels after user guesses.

        Args:
            guess_num (int): Represents which row to update
            guessed_letters (list): List of int (0-2) for color of each letter
        """
        j = 0   # Index representing position of letter in word.
        
        for ch in self.main_gui.current_guess:  # Updates each guess with the corresponding letter.
            self.label_list[guess_num-1][j].config(
                text=ch.upper(),
                background=self.color_dict[guessed_letters[j]],
                foreground="white"
            )
            j += 1

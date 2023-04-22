import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk
from View.view import View

class KeyboardManager(View):
    """Creates and updates the keyboard representing guessed letters.
    """
    def __init__(self, controller, main_gui) -> None:
        super().__init__(controller)
        self.main_gui = main_gui

    def start_keyboard(self):
        self.top_labels = [     # List of labels for top row of keyboard.
            ttk.Label(text=ch, width = 2, font=12, background=View.bg_theme,
                    anchor="center", master=self.main_gui.frame, borderwidth=1)
                    for ch in View.top_letters.keys()]
        
        self.mid_labels = [     # List of labels for middle row of keyboard.
            ttk.Label(text=ch, width = 2, font=12, background=View.bg_theme,
                    anchor="center", master=self.main_gui.frame, borderwidth=1)
                    for ch in View.mid_letters.keys()]
        
        self.bottom_labels = [  # List of labels for bottom row of keyboard.
            ttk.Label(text=ch, width = 2, font=12, background=View.bg_theme,
                    anchor="center", master=self.main_gui.frame, borderwidth=1)
                    for ch in View.bottom_letters.keys()]

        for i in range(len(self.top_labels)):   # Places each label in top row.
            self.top_labels[i].place(x=(200 + 45*i), y=(500), anchor="center")

            if i < len(self.mid_labels):        # Places each label in middle row.
                self.mid_labels[i].place(x=(220 + 45*i), y=540, anchor="center")

            if i < len(self.bottom_labels):     # Places each label in bottom row.
                self.bottom_labels[i].place(x=(240 + 45*i), y=580, anchor="center")

    def update_keyboard(self, guessed_letters):
        """Updates keyboard with correct colors after a guess.

        Args:
            guessed_letters (list): List of int (0-2) for color of each letter in guess.
        """
        i = 0   # Index variable for guessed_letters

        for ch in self.main_gui.current_guess:  # Updates keys for each letter in last guess.
            CH = ch.upper()
            if CH in self.bottom_letters.keys():    # Updates top letters.
                self.bottom_labels[self.bottom_letters[CH]].config(
                    text=CH,
                    background=self.color_dict[guessed_letters[i]],
                    foreground="white"
                )

            elif CH in self.mid_letters.keys():     # Updates middle letters.
                self.mid_labels[self.mid_letters[CH]].config(
                    text=CH,
                    background=self.color_dict[guessed_letters[i]],
                    foreground="white"
                )

            else:   # Updates bottom letters.
                self.top_labels[self.top_letters[CH]].config(
                    text=CH,
                    background=self.color_dict[guessed_letters[i]],
                    foreground="white"
                )
            i += 1
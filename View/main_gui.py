import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk
from View.view import View
from View.label_manager import LabelManager
from View.keyboard_manager import KeyboardManager

class MainGUI(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)
        self.label_manager = LabelManager(self.controller, self)
        self.keyboard_manager = KeyboardManager(self.controller, self)

    def start_GUI(self):
        """Generates the GUI at startup. Updates to GUI are handled 
           individually by other methods.
        """
        self.window = tk.Tk()
        sv_ttk.set_theme(View.theme_setting)

        self.frame = tk.Frame(master=self.window, width=800, height=700)
        self.frame.pack()

        self.title = ttk.Label(text="Wordle", font=28, master=self.frame)
        self.title.place(x=400, y=40, anchor="center")

        self.enter_button = ttk.Button(
            text="Enter",
            command=self.enter_guess,
            master=self.frame)
        self.enter_button.place(x=545, y=580, anchor="w")

        self.guess = tk.StringVar(master=self.frame)
        self.guess.trace("w", self.limit_guess_size)
        self.word_input = ttk.Entry(textvariable=self.guess, master=self.frame, font=12)
        self.word_input.place(x=400, y=425, anchor="center")

        self.label_manager.guess_labels()
        self.keyboard_manager.start_keyboard()

    def limit_guess_size(self, *args):
        """Restricts the max chars in the guess entry to 5.
        """
        value = self.guess.get()
        if len(value) > 5: self.guess.set(value[:5])

    def enter_guess(self):
            guess_input = self.word_input.get()
            guess_input = guess_input.lower()

            if guess_input in View.guess_list:    # Guess is only accepted if it is in the wordlist. 
                self.current_guess = self.word_input.get().lower()
                self.word_input.delete(0, len(guess_input)) # Clears entry field for next guess.
                self.controller.control_guess()
            else:
                tkinter.messagebox.showwarning(message="Guess not in word list.")

    def switch_theme(self):
        sv_ttk.set_theme(self.theme_setting)
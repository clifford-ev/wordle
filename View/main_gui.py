import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk
from View.view import View
from View.label_manager import LabelManager
from View.keyboard_manager import KeyboardManager

class MainGUI(View):
    """Generates the UI of the main window and gets guesses from user.

    Args:
        View (_type_): _description_
    """
    def __init__(self, controller) -> None:
        super().__init__(controller)
        self.label_manager = LabelManager(self.controller, self)
        self.keyboard_manager = KeyboardManager(self.controller, self)

    def start_GUI(self):
        """Generates the GUI at startup. Updates to GUI are handled 
           individually by other methods.
        """
        self.window = tk.Tk()   # Main window
        sv_ttk.set_theme(View.theme_setting)

        # Main frame in which all widgets are placed
        self.frame = tk.Frame(master=self.window, width=800, height=700)
        self.frame.pack()

        # Title text
        self.title = ttk.Label(text="Wordle", font=32, master=self.frame)
        self.title.place(x=400, y=40, anchor="center")

        # Enter button to submit guess
        self.enter_button = ttk.Button(
            text="Enter",
            command=self.enter_guess,
            master=self.frame)
        self.enter_button.place(x=545, y=580, anchor="w")

        # Entry box for guess; limit_guess_size is called everytime a char is typed/deleted.
        self.guess = tk.StringVar(master=self.frame)
        self.guess.trace("w", self.limit_guess_size)
        self.word_input = ttk.Entry(textvariable=self.guess, master=self.frame, font=12)
        self.word_input.focus()
        self.word_input.place(x=400, y=425, anchor="center")

        # Word labels and keyboard
        self.label_manager.guess_labels()
        self.keyboard_manager.start_keyboard()

    def limit_guess_size(self, *args):
        """Restricts the max chars in the guess entry to 5 and calls
        update_dynamic_labels().
        """
        value = self.guess.get()    # Texted currently entered in the guess entry.
        self.update_dynamic_labels(value)   # Updates labels.

        if len(value) > 5: # If there are more than 5 chars, delete all but the first 5.
            self.guess.set(value[:5])

    def update_dynamic_labels(self, value):
        """Dynamically updates the word labels with the contents
        of the entry box.

        Args:
            value (str): Contents of guess entry box.
        """
        i = len(value)-1  # Index of the last character.

        try:    # If the entry box is not empty, updates the last character.
            ch = value[-1]
            CH = ch.upper()

            self.label_manager.label_list[self.controller.model.guess_num][i].config(
                text= CH
            )
        except IndexError:
            pass

        for j in range(i+1, 5):  # Clears all deleted letters.
            self.label_manager.label_list[self.controller.model.guess_num][j].config(
                text= ""
            )


    def enter_guess(self):
        """Checks if entered guess is valid and returns it to the controller.
        """
        guess_input = self.word_input.get()
        guess_input = guess_input.lower()

        if guess_input in View.guess_list:    # Guess is only accepted if it is in the wordlist. 
            self.current_guess = self.word_input.get().lower()
            self.word_input.delete(0, len(guess_input)) # Clears entry field for next guess.
            self.controller.control_guess()
        else:
            tkinter.messagebox.showwarning(message="Guess not in word list.")
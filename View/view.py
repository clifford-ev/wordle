import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import threading

class View(threading.Thread):
    # Reads file of allowed guesses into guess_list.
    with open("allowed_guesses.txt") as f:
        guess_list = f.read().splitlines()

    color_dict = {
         0: "#797c7e",
         1: "#c5b35d",
         2: "#76a866"
    }

    def __init__(self) -> None:
        self.current_guess = ""
        self.label_list = []
        threading.Thread.__init__(self=self)


    def start_GUI(self):
        """Generates the GUI at startup. Updates to GUI are handled 
           individually by other methods.
        """
        self.window = tk.Tk()

        self.frame = tk.Frame(master=self.window, width=1000, height=800)
        self.frame.pack()


        self.title = ttk.Label(text="wordle", master=self.frame)
        self.title.place(x=500, y=0)

        self.enter_button = ttk.Button(
            text="Enter",
            # width=10,
            # height=3,
            # bg="white",
            # fg="black",
            command=self.enter_guess)
        self.enter_button.place(x=500, y=600)

        self.guess = tk.StringVar()
        self.guess.trace("w", self.limit_guess_size)
        self.word_input = ttk.Entry(textvariable=self.guess, master=self.frame)
        self.word_input.place(x=500, y=400)

        self.guess_labels()

    def run(self):
        self.window.mainloop()

    def enter_guess(self):
            guess_input = self.word_input.get()
            guess_input.lower()

            if guess_input in View.guess_list:    # Guess is only accepted if it is in the wordlist. 
                self.word_input.delete(0, len(guess_input)) # Clears entry field for next guess.
                guess_input = self.current_guess
                return guess_input
            
            tkinter.messagebox.showwarning(message="Guess not in word list.")


    def limit_guess_size(self, *args):
        """Restricts the max chars in the guess entry to 5.
        """
        value = self.guess.get()
        if len(value) > 5: self.guess.set(value[:5])

    def guess_labels(self):
        """Generates and displays an array of labels that contain current and previous guesses.
        """
        for i in range(6):  # Loops for each row of labels.
            # Generates a label for each letter slot in a row.
             self.label_list.append([ttk.Label(text="", width=5, background="white", master=self.frame) for x in range(5)])

             for j in range(5): # Repeats each letter in a row.
                self.label_list[i][j].place(x=(375 + 50*j), y=(50 + 50*i))  # Places labels.

    def update_guess_labels(self, guess_num, guessed_letters):
        j = 0   # Index representing position of letter in word.
        
        for ch in self.current_guess:
            self.label_list[guess_num-1][j].config(
                text=ch.upper(),
                background=self.color_dict[guessed_letters[ch]],
                foreground="white"
            )
            j += 1
        self.window.mainloop()

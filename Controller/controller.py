from Model.game import Game
# from View.view import View

class Controller:
    def __init__(self) -> None:
        self.model = Game()
        self.view = View(self)
        # self.guess_limit = 6

    def set_guess_limit(self):
        pass

    def control_guess(self):        
        win_state = self.model.guess(self.view.current_guess)
        self.view.update_guess_labels(self.model.guess_num, self.model.guessed_letters)
        self.view.update_keyboard(self.model.guessed_letters)

        if win_state:
            self.view.win_popup()
        elif self.model.guess_num == 6:
            self.view.loss_popup()

    def run_game(self):
        self.model.set_solution()

        self.view.start_GUI()
        self.view.run()

        if self.model.guess(self.view.current_guess):
            self.model.new_game()

        self.view.update_guess_labels(self.model.guess_num, self.model.guessed_letters)

    def restart(self):
        self.model.new_game()   # Resets model variables. 
        self.model.set_solution()   # Generates new solution.

        self.view.guess_labels()    # Resets UI.
        self.view.start_keyboard()
        self.view.switch_theme()
        
        
        try:    # Deletes win/loss popup.
            self.view.win_window.destroy()
        except:
            self.view.loss_window.destroy()
        







import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk

class View():
    # Reads file of allowed guesses into guess_list.
    with open("allowed_guesses.txt") as f:
        guess_list = f.read().splitlines()

    top_letters = {"Q" : 0, "W" : 1, "E" : 2, "R" : 3, "T" : 4, "Y" : 5, "U" : 6, "I" : 7, "O" : 8, "P" : 9}
    mid_letters = {"A" : 0, "S" : 1, "D" : 2, "F" : 3, "G" : 4, "H" : 5, "J" : 6, "K" : 7, "L" : 8}
    bottom_letters = {"Z" : 0, "X" : 1, "C" : 2, "V" : 3, "B" : 4, "N" : 5, "M" : 6}

    color_dict = {
         0: "#797c7e",
         1: "#c5b35d",
         2: "#76a866"
    }

    def __init__(self, controller) -> None:
        self.current_guess = ""
        self.controller = controller
        self.theme_setting = "light"
        self.bg_theme = "#ffffff"


    def start_GUI(self):
        """Generates the GUI at startup. Updates to GUI are handled 
           individually by other methods.
        """
        self.window = tk.Tk()
        sv_ttk.set_theme(self.theme_setting)

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

        self.guess_labels()
        self.start_keyboard()

    def run(self):
        self.window.mainloop()

    def enter_guess(self):
            guess_input = self.word_input.get()
            guess_input = guess_input.lower()

            if guess_input in View.guess_list:    # Guess is only accepted if it is in the wordlist. 
                self.current_guess = self.word_input.get().lower()
                self.word_input.delete(0, len(guess_input)) # Clears entry field for next guess.
                self.controller.control_guess()
            else:
                tkinter.messagebox.showwarning(message="Guess not in word list.")


    def limit_guess_size(self, *args):
        """Restricts the max chars in the guess entry to 5.
        """
        value = self.guess.get()
        if len(value) > 5: self.guess.set(value[:5])

    def guess_labels(self):
        """Generates and displays an array of labels that contain current and previous guesses.
        """
        self.label_list = []

        for i in range(6):  # Loops for each row of labels.
            # Generates a label for each letter slot in a row.
             self.label_list.append([
                ttk.Label(text="", width=3, font=14, background=self.bg_theme, master=self.frame, anchor="center")
                for x in range(5)])

             for j in range(5): # Repeats each letter in a row.
                self.label_list[i][j].place(x=(300 + 50*j), y=(100 + 50*i), anchor="center")  # Places labels.

    def start_keyboard(self):
        self.top_labels = []
        self.mid_labels = []
        self.bottom_labels = []

        self.top_labels = [
            ttk.Label(text=ch, width = 2, font=12, background=self.bg_theme,
                    anchor="center", master=self.frame, borderwidth=1)
                    for ch in View.top_letters.keys()]
        self.mid_labels = [
            ttk.Label(text=ch, width = 2, font=12, background=self.bg_theme,
                    anchor="center", master=self.frame, borderwidth=1)
                    for ch in View.mid_letters.keys()]
        self.bottom_labels = [
            ttk.Label(text=ch, width = 2, font=12, background=self.bg_theme,
                    anchor="center", master=self.frame, borderwidth=1)
                    for ch in View.bottom_letters.keys()]

        for i in range(len(self.top_labels)):
            self.top_labels[i].place(x=(200 + 45*i), y=(500), anchor="center")

            if i < len(self.mid_labels):
                self.mid_labels[i].place(x=(220 + 45*i), y=540, anchor="center")

            if i < len(self.bottom_labels):
                self.bottom_labels[i].place(x=(240 + 45*i), y=580, anchor="center")


    def update_guess_labels(self, guess_num, guessed_letters):
        j = 0   # Index representing position of letter in word.
        
        for ch in self.current_guess:
            self.label_list[guess_num-1][j].config(
                text=ch.upper(),
                background=self.color_dict[guessed_letters[j]],
                foreground="white"
            )
            j += 1
        # self.window.mainloop()

    def update_keyboard(self, guessed_letters):
        i = 0

        for ch in self.current_guess:
            CH = ch.upper()
            if CH in self.bottom_letters.keys():
                self.bottom_labels[self.bottom_letters[CH]].config(
                    text=CH,
                    background=self.color_dict[guessed_letters[i]],
                    foreground="white"
                )

            elif CH in self.mid_letters.keys():
                self.mid_labels[self.mid_letters[CH]].config(
                    text=CH,
                    background=self.color_dict[guessed_letters[i]],
                    foreground="white"
                )

            else:
                self.top_labels[self.top_letters[CH]].config(
                    text=CH,
                    background=self.color_dict[guessed_letters[i]],
                    foreground="white"
                )
            i += 1

    def win_popup(self):
        self.win_window = tk.Tk()
        self.win_window.title("Congratulations!")
        
        self.win_label = ttk.Label(master=self.win_window,
                                   text="You got the word!\nWould you like to play again?",
                                   padding=10)
        
        self.restart_button = ttk.Button(text="Restart",
                                         command=self.controller.restart,
                                         master=self.win_window,
                                         padding=5)
        self.options_button = ttk.Button(text="Options",
                                         command=self.options,
                                         master=self.win_window,
                                         padding=5)
        
        self.win_label.pack(side="top")
        self.restart_button.pack(side="left")
        self.options_button.pack(side="right")

        self.win_window.mainloop()


    def loss_popup(self):
        self.loss_window = tk.Tk()
        self.loss_window.title("Game over!")
        
        self.loss_label = ttk.Label(master=self.loss_window,
                                   text="You ran out of guesses!\nWould you like to play again?",
                                   padding=10)
        
        self.restart_button = ttk.Button(text="Restart",
                                          command=self.controller.restart,
                                          master=self.loss_window,
                                          padding=5)
        self.options_button = ttk.Button(text="Options",
                                          command=self.options,
                                          master=self.loss_window,
                                          padding=5)
        
        self.loss_label.pack(side="top")
        self.restart_button.pack(side="left")
        self.options_button.pack(side="right")

        self.loss_window.mainloop()

    
    def options(self):
        self.options_window = tk.Tk()
        self.options_window.title("Options")
        
        if self.theme_setting == "light":
            self.theme_button = ttk.Button(text="Current Theme: Light",
                                         command=self.switch_dark,
                                         master=self.options_window)

        else:
            self.theme_button = ttk.Button(text="Current Theme: Dark",
                                         command=self.switch_light,
                                         master=self.options_window)
            
        

        self.save_button = ttk.Button(text="Save and Exit",
                                         command=self.exit_options,
                                         master=self.options_window)
        
        self.theme_button.pack()
        self.save_button.pack()

        self.options_window.mainloop()

    def switch_dark(self):
        self.theme_setting = "dark"
        self.bg_theme = "#2f2f2f"
        self.theme_button.config(text="Current Theme: Dark")
        
    def switch_light(self):
        self.theme_setting = "light"
        self.bg_theme = "#ffffff"
        self.theme_button.config(text="Current Theme: Light")
        
    def exit_options(self):
        self.options_window.destroy()

    def switch_theme(self):
        sv_ttk.set_theme(self.theme_setting)
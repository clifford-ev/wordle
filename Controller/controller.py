from Model.game import Game
from View.view import View
# from waiting import wait
import tkinter.ttk as ttk

class Controller:
    def __init__(self) -> None:
        self.model = Game()
        self.view = View()
        # self.guess_limit = 6

    def set_guess_limit(self):
        pass

    def control_guess(self):        
        # Waits until user guesses.
        # wait(lambda self: bool(self.view.current_guess))

        if self.model.guess(self.view.current_guess):
            # victory popup ***
            self.model.new_game()

        self.view.update_guess_labels(self.model.guess_num, self.model.guessed_letters)

    def run_game(self):
        self.enter_button = ttk.Button(
            text="Enter",
            # width=10,
            # height=3,
            # bg="white",
            # fg="black",
            command=self.control_guess)


        self.view.start_GUI(self.enter_button)

        
        # self.view.enter_button.configure(command=self.control_guess)

        self.view.window.mainloop()

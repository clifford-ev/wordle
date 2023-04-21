from Model.game import Game
from View.main_gui import MainGUI
from View.win_gui import WinGUI
from View.loss_gui import LossGUI


class Controller:
    def __init__(self) -> None:
        self.model = Game()
        self.view = MainGUI(self)
        self.win_gui = WinGUI(self)
        self.loss_gui = LossGUI(self)

    def control_guess(self):        
        win_state = self.model.guess(self.view.current_guess)
        self.view.label_manager.update_guess_labels(self.model.guess_num, self.model.guessed_letters)
        self.view.keyboard_manager.update_keyboard(self.model.guessed_letters)

        if win_state:
            self.win_gui.win_popup()
        elif self.model.guess_num == 6:
            self.loss_gui.loss_popup()

    def run_game(self):
        self.model.set_solution()

        self.view.start_GUI()
        self.view.run(self.view.window)

        if self.model.guess(self.view.current_guess):
            self.model.new_game()

        self.view.label_manager.update_guess_labels(self.model.guess_num, self.model.guessed_letters)

    def restart(self):
        self.model.new_game()   # Resets model variables. 
        self.model.set_solution()   # Generates new solution.

        self.view.label_manager.guess_labels()    # Resets UI.
        self.view.keyboard_manager.start_keyboard()
        self.view.switch_theme()
        
        
        try:    # Deletes win/loss popup.
            self.win_gui.delete_window()
        except:
            self.loss_gui.delete_window()
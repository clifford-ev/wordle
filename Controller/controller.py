from Model.game import Game
from View.main_gui import MainGUI
from View.win_gui import WinGUI
from View.loss_gui import LossGUI


class Controller:
    """Receives data from GUI classes and manipulates the model.
    """
    def __init__(self) -> None:
        self.model = Game()
        self.view = MainGUI(self)
        self.win_gui = WinGUI(self)
        self.loss_gui = LossGUI(self)

    def control_guess(self):
        """Receives guess from main_GUI and passes on to model. Then initializes
        win/loss GUI if an end state had been reached.
        """

        win_state = self.model.guess(self.view.current_guess)   # Checks guess
        # Updates guess labels with new guess.
        self.view.label_manager.update_guess_labels(self.model.guess_num, self.model.guessed_letters)
        self.view.keyboard_manager.update_keyboard(self.model.guessed_letters)  # Updates keyboard.

        if win_state:   # If the player has won, triggers win pop-up.
            self.win_gui.win_popup()
        elif self.model.guess_num == 6:  # If the player has lost, triggers loss pop-up.
            self.loss_gui.loss_popup()

    def run_game(self):
        """Initializes GUI and and sets solution.
        """
        self.model.set_solution()

        self.view.start_GUI()
        self.view.run(self.view.window)

    def restart(self):
        """Resets UI and clears variables to allow for a new game.
        """
        self.model.new_game()   # Resets model variables. 
        self.model.set_solution()   # Generates new solution.

        self.view.label_manager.guess_labels()    # Resets UI.
        self.view.keyboard_manager.start_keyboard()
        self.view.switch_theme()
        
        
        try:    # Deletes win/loss popup.
            self.win_gui.delete_window()
        except:
            self.loss_gui.delete_window()
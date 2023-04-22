import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk
from View.view import View
from View.option_gui import OptionGUI

class LossGUI(View):
    """Creates loss pop-up with buttons to restart or open options.

    Args:
        View (_type_): _description_
    """
    def __init__(self, controller) -> None:
        super().__init__(controller)
        self.option_gui = OptionGUI(self.controller)

    def loss_popup(self):
        """Creates loss pop-up window.
        """
        self.loss_window = tk.Toplevel()  # Pop-up window.
        self.loss_window.title("Game over!")
        sv_ttk.set_theme(View.theme_setting)
        
        # Loss message with correct word.
        self.loss_label = ttk.Label(master=self.loss_window,
                                   text= # Sorry for formatting: justify breaks if text is on multiple lines.
f"You ran out of guesses!\nThe correct word was {self.controller.model.solution}.\nWould you like to play again?",
                                   padding=5,
                                   justify="center")
        
        # Restart button
        self.restart_button = ttk.Button(text="Restart",
                                          command=self.controller.restart,
                                          master=self.loss_window,
                                          padding=5)
        # Options button
        self.options_button = ttk.Button(text="Options",
                                          command=self.option_gui.options,
                                          master=self.loss_window,
                                          padding=5)
        
        self.loss_label.pack(side="top")
        self.restart_button.pack(side="left", padx=5, pady=5)
        self.options_button.pack(side="right", padx=5, pady=5)

        self.loss_window.mainloop()

    def delete_window(self):
        """Deletes loss pop-up window.
        """
        self.loss_window.destroy()
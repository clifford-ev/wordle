import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk
from View.view import View
from View.option_gui import OptionGUI

class LossGUI(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)
        self.option_gui = OptionGUI(self.controller)

    def loss_popup(self):
        self.loss_window = tk.Tk()
        self.loss_window.title("Game over!")
        
        self.loss_label = ttk.Label(master=self.loss_window,
                                   text=f"You ran out of guesses!\
                                   \nThe correct word was {self.controller.model.solution}.\
                                   \nWould you like to play again?",
                                   padding=10)
        
        self.restart_button = ttk.Button(text="Restart",
                                          command=self.controller.restart,
                                          master=self.loss_window,
                                          padding=5)
        self.options_button = ttk.Button(text="Options",
                                          command=self.option_gui.options,
                                          master=self.loss_window,
                                          padding=5)
        
        self.loss_label.pack(side="top")
        self.restart_button.pack(side="left")
        self.options_button.pack(side="right")

        self.loss_window.mainloop()

    def delete_window(self):
        self.loss_window.destroy()
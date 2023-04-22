import tkinter as tk
import tkinter.ttk as ttk
from View.view import View
from View.option_gui import OptionGUI

class WinGUI(View):
    """Creates win popup message with buttons to restart or open options.
    """
    def __init__(self, controller) -> None:
        super().__init__(controller)
        self.option_gui = OptionGUI(self.controller)

    def win_popup(self):
        """Generates the popup menu.
        """
        self.win_window = tk.Toplevel() # Win pop-up window
        self.win_window.title("Congratulations!")
        
        # Win pop-up message
        self.win_label = ttk.Label(master=self.win_window,
                                   text="You got the word!\nWould you like to play again?",
                                   padding=5,
                                   justify="center")
        # Restart button
        self.restart_button = ttk.Button(text="Restart",
                                         command=self.controller.restart,
                                         master=self.win_window,
                                         padding=5)
        #Options button
        self.options_button = ttk.Button(text="Options",
                                         command=self.option_gui.options,
                                         master=self.win_window,
                                         padding=7)
        
        self.win_label.pack(side="top")
        self.restart_button.pack(side="left", padx=7, pady=5)
        self.options_button.pack(side="right", padx=7, pady=5)

        self.win_window.mainloop()

    def delete_window(self):
        """Deletes popup after restart is selected.
        """
        self.win_window.destroy()
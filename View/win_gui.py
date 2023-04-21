import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk
from View.view import View
from View.option_gui import OptionGUI

class WinGUI(View):
    def __init__(self, controller) -> None:
        super().__init__(controller)
        self.option_gui = OptionGUI(self.controller)

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
                                         command=self.option_gui.options,
                                         master=self.win_window,
                                         padding=5)
        
        self.win_label.pack(side="top")
        self.restart_button.pack(side="left")
        self.options_button.pack(side="right")

        self.win_window.mainloop()

    def delete_window(self):
        self.win_window.destroy()
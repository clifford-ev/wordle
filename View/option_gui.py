import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sv_ttk
from View.view import View

class OptionGUI(View):
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
        View.theme_setting = "dark"
        View.bg_theme = "#2f2f2f"
        self.theme_button.config(text="Current Theme: Dark")
        
    def switch_light(self):
        View.theme_setting = "light"
        View.bg_theme = "#ffffff"
        self.theme_button.config(text="Current Theme: Light")
        
    def exit_options(self):
        self.options_window.destroy()
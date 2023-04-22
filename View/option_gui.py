import tkinter as tk
import tkinter.ttk as ttk
from View.view import View

class OptionGUI(View):
    """Creates options pop-up window with button to switch themes.
        """
    def options(self):
        """Creates options pop-up window.
        """
        self.options_window = tk.Toplevel() # Options window
        self.options_window.title("Options")
        
        if self.theme_setting == "light":   # If light, uses switch-dark button.
            self.theme_button = ttk.Button(text="Current Theme: Light",
                                         command=self.switch_dark,
                                         master=self.options_window,
                                         width=20)

        else:   # If dark, uses switch-light button.
            self.theme_button = ttk.Button(text="Current Theme: Dark",
                                         command=self.switch_light,
                                         master=self.options_window,
                                         width=20)
            
        
        # Save button that closes window.
        self.save_button = ttk.Button(text="Save and Exit",
                                         command=self.exit_options,
                                         master=self.options_window)
        
        self.theme_button.pack(padx=5, pady=7)
        self.save_button.pack(padx=5, pady=2)

        self.options_window.mainloop()

    def switch_dark(self):
        """Changes theme from light to dark.
        """
        View.theme_setting = "dark"
        View.bg_theme = "#2f2f2f"
        self.theme_button.config(text="Current Theme: Dark")
        self.switch_theme()
        
    def switch_light(self):
        """Changes theme from dark to light.
        """
        View.theme_setting = "light"
        View.bg_theme = "#ffffff"
        self.theme_button.config(text="Current Theme: Light")
        self.switch_theme()
        
    def exit_options(self):
        """Closes options window.
        """
        self.options_window.destroy()
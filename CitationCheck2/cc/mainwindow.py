from customtkinter import CTkFrame
import homeF
import singleF
import checkF
import helpF
import infoF

class MainWindow(CTkFrame):
    f_home = None
    f_single = None
    f_check = None
    f_help = None
    f_info = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color='#101221', corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.f_home = homeF.HOME_FRAME(master=self)
        self.f_single = singleF.SINGLE_FRAME(master=self)
        self.f_check = checkF.CHECK_FRAME(master=self)
        self.f_help = helpF.HELP_FRAME(master=self)
        self.f_info = infoF.INFO_FRAME(master=self)

        self.f_single.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.f_check.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.f_help.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.f_info.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.f_single.grid_remove()
        self.f_check.grid_remove()
        self.f_help.grid_remove()
        self.f_info.grid_remove()
        self.f_home.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def set_window(self, window):
        match window:
            case "HOME":
                self.f_home.grid()
                self.f_single.grid_remove()
                self.f_check.grid_remove()
                self.f_help.grid_remove()
                self.f_info.grid_remove()
            case "SINGLE":
                self.f_single.grid()
                self.f_home.grid_remove()
                self.f_check.grid_remove()
                self.f_help.grid_remove()
                self.f_info.grid_remove()
            case "CHECK":
                self.f_check.grid()
                self.f_home.grid_remove()
                self.f_single.grid_remove()
                self.f_help.grid_remove()
                self.f_info.grid_remove()
            case "HELP":
                self.f_help.grid()
                self.f_home.grid_remove()
                self.f_check.grid_remove()
                self.f_single.grid_remove()
                self.f_info.grid_remove()
            case "INFO":
                self.f_info.grid()
                self.f_home.grid_remove()
                self.f_check.grid_remove()
                self.f_help.grid_remove()
                self.f_single.grid_remove()    
        
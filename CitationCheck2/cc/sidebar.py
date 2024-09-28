from customtkinter import CTkFrame
from customtkinter import CTkButton
from customtkinter import CTkImage
from webbrowser import open_new
from PIL import Image

class Sidebar(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.configure(fg_color='#252730', width=80, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(0, weight=1)

        image_cc_icon = CTkImage(Image.open("assets/logo.png"), size=(40,40))
        self.b_logo = CTkButton(self, fg_color='#252730', text="", hover_color='#252730', image=image_cc_icon, command=self.open_browser)
        self.b_logo.grid(row=0, column=0, padx=5, pady=5)

        fileopen_icon = CTkImage(Image.open("assets/fileopen_icon.png"), size=(30,30))
        self.b_fileopen_icon = CTkButton(self, fg_color='#252730', text="", hover_color='#252730', image=fileopen_icon, command=self.show_home)
        self.b_fileopen_icon.grid(row=2, column=0, padx=5, pady=5)

        looksone_icon = CTkImage(Image.open("assets/looksone_icon.png"), size=(30,30))
        self.b_looksone_icon = CTkButton(self, fg_color='#252730', text="", hover_color='#252730', image=looksone_icon, command=self.show_single)
        self.b_looksone_icon.grid(row=3, column=0, padx=5, pady=5)

        checkbox_icon = CTkImage(Image.open("assets/checkbox_icon.png"), size=(30,30))
        self.b_checkbox_icon = CTkButton(self, fg_color='#252730', text="", hover_color='#252730', image=checkbox_icon, command=self.show_check)
        self.b_checkbox_icon.grid(row=4, column=0, padx=5, pady=5)

        help_icon = CTkImage(Image.open("assets/help_icon.png"), size=(30,30))
        self.b_help_icon = CTkButton(self, fg_color='#252730', text="", hover_color='#252730', image=help_icon, command=self.show_help)
        self.b_help_icon.grid(row=5, column=0, padx=5, pady=5)

        info_icon = CTkImage(Image.open("assets/info_icon.png"), size=(30,30))
        self.b_info_icon = CTkButton(self, fg_color='#252730', text="", hover_color='#252730', image=info_icon, command=self.show_info)
        self.b_info_icon.grid(row=7, column=0, padx=5, pady=5)

    def open_browser(self):
        open_new(r"https://github.com/BenSt099/CitationCheck")

    def show_home(self):
        self.master.update_UI("HOME")

    def show_single(self):
        self.master.update_UI("SINGLE")

    def show_check(self):
        self.master.update_UI("CHECK")

    def show_help(self):
        self.master.update_UI("HELP")

    def show_info(self):
        self.master.update_UI("INFO")
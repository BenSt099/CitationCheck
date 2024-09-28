###############################################################################################
###############################################################################################
#                           /************ CitationCheck ************/                         #
#                                             v2.0                                            #
###############################################################################################
###############################################################################################

from platform import system
from multiprocessing import freeze_support
import sidebar
import mainwindow
from tkinter import PhotoImage
from customtkinter import CTkInputDialog
from customtkinter import CTkFont
from customtkinter import CTk
from customtkinter import set_appearance_mode
from customtkinter import set_default_color_theme
from json import load
from json import dump
from re import search

###############################################################################################
#####################################       MAINAPP       #####################################
###############################################################################################
class App(CTk):
 
    def __init__(self):
        super().__init__()
        set_appearance_mode("System")
        set_default_color_theme("dark-blue")
        self.geometry("1000x600")
        self.title("CitationCheck")
        
        if system() == 'Windows':
            self.iconbitmap('assets/logo.ico')
        else:
            icon_cc = PhotoImage(file='assets/logo.png')
            self.iconphoto(False, icon_cc)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0)
        self.grid_columnconfigure(1, weight=8)
        self.grid_columnconfigure(2, weight=8)

        self.sb = sidebar.Sidebar(master=self)
        self.sb.grid(row=0, column=0, padx=0, pady=0, sticky="news")

        self.sb = mainwindow.MainWindow(master=self)
        self.sb.grid(row=0, column=1, padx=0, pady=0, sticky="news", columnspan=2)



        # content_dict = {}
        # with open('assets/cc_email.json') as email_file:
        #     content_dict = load(email_file)
        # if content_dict == {}:
        #     dialog = CTkInputDialog(text="Please type in your email address:", title="Email address", button_fg_color="#bf0041", button_hover_color="#8d0433", button_text_color="black", font=CTkFont(family='times new roman 16 bold', size=17, weight="bold"))
        #     email = dialog.get_input()
        #     if email == "" or (search(r"^\S+@\S+\.\S+$", email) is None):
        #         email = "citationcheck.application.github@gmail.com"
        #     content_dict = {
        #         'email': email
        #     }
        #     with open("assets/cc_email.json", mode="w", encoding="utf-8") as email_file:
        #         dump(content_dict, email_file)    


    def update_UI(self, window):
        self.sb.set_window(window)

if __name__ == "__main__":
    if system() == 'Windows':
        freeze_support()
    app = App()
    app.mainloop()
###############################################################################################
#####################################       MAINAPP       #####################################
###############################################################################################
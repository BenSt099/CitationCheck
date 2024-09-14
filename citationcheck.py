###############################################################################################
###############################################################################################
#                           /************ CitationCheck ************/                         #
#                                             v1.0                                            #
###############################################################################################
###############################################################################################

import cc_upperframe
import cc_lowerframe
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
        self.geometry("800x600")
        self.title("CheckCitation")
        self.iconbitmap('logo.ico')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.upperframe = cc_upperframe.UpperFrame(master=self)
        self.upperframe.grid(row=0, column=0, padx=0, pady=0, rowspan=4, sticky="news")
        self.lowerframe = cc_lowerframe.LowerFrame(master=self, height=10)
        self.lowerframe.grid(row=4, column=0, padx=0, pady=0, sticky="new")

        content_dict = {}
        with open('cc_email.json') as email_file:
            content_dict = load(email_file)
        if content_dict == {}:
            dialog = CTkInputDialog(text="Please type in your email address:", title="Email address", button_fg_color="#bf0041", button_hover_color="#8d0433", button_text_color="black", font=CTkFont(family='times new roman 16 bold', size=17, weight="bold"))
            email = dialog.get_input()
            if email == "" or (search(r"^\S+@\S+\.\S+$", email) is None):
                email = "citationcheck.github@gmail.com"

            content_dict = {
                'email': email
            }
            with open("cc_email.json", mode="w", encoding="utf-8") as email_file:
                dump(content_dict, email_file)    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()

###############################################################################################
#####################################       MAINAPP       #####################################
###############################################################################################
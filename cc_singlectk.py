from customtkinter import CTkFont
from customtkinter import CTkButton
from customtkinter import CTkEntry
from customtkinter import CTkToplevel
from customtkinter import get_appearance_mode
from platform import system
from tkinter import PhotoImage

###############################################################################################
#####################################      SINGLECTK      #####################################
###############################################################################################
class SingleCTk(CTkToplevel):
    information = []
    closed = False
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x220")

        if system() == 'Windows':
            self.after(201, lambda: self.iconbitmap('assets/logo.ico')) # fix from StackOverflow
            # https://stackoverflow.com/questions/75825190/how-to-put-iconbitmap-on-a-customtkinter-toplevel
        else:
            icon_cc = PhotoImage(file='assets/logo.png')
            self.iconphoto(False, icon_cc)

        self.resizable(False, False)
        self.title("CheckCitation - Input")
        self.grid_rowconfigure(3) 
        self.grid_columnconfigure(2)

        self.protocol("WM_DELETE_WINDOW", self.close)

        if get_appearance_mode() == 'Light':
            textcolor = "black"
            frameColor= "#d9d8d7"
            textbuttoncolor = "white"
        else:
            textbuttoncolor = "black"
            frameColor= "gray13"
            textcolor = "white"    

        self.configure(fg_color=frameColor)    

        ###############################################################################
        ### Title ###
        self.label_title = CTkButton(self, fg_color = "transparent", hover_color=frameColor, text_color=textcolor, text="Title", font=CTkFont(family='times new roman 14 bold', size=17, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=20)

        self.title_input = CTkEntry(self, placeholder_text="Title", width=500, height=35)
        self.title_input.grid(row=0, column=1, padx=20, pady=20)
        ###############################################################################
        ### DOI ###
        self.label_doi = CTkButton(self, fg_color = "transparent", hover_color=frameColor, text_color=textcolor, text="DOI", font=CTkFont(family='times new roman 14 bold', size=17, weight="bold"))
        self.label_doi.grid(row=1, column=0, padx=20, pady=20)

        self.doi_input = CTkEntry(self, placeholder_text="DOI", width=500, height=35)
        self.doi_input.grid(row=1, column=1, padx=20, pady=20)
        ###############################################################################
        ### Buttons ###
        self.button1 = CTkButton(self, text_color=textbuttoncolor, text="Cancel", fg_color="#bf0041", hover_color="#8d0433", font=CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.close)      
        self.button1.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.button2 = CTkButton(self, text_color=textbuttoncolor, text="CHECK", fg_color="#bf0041", hover_color="#8d0433", font=CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.collect)
        self.button2.grid(row=2, column=2, padx=20, pady=20, sticky="ew")
        ###############################################################################

    def close(self):
        self.closed = True
        self.withdraw()

    def destroy_window(self):
        self.destroy()

    def collect(self):
        self.information.append(self.title_input.get())
        self.information.append(self.doi_input.get())
        self.withdraw()
        self.closed = True

    def get_information(self):
        return self.information
    
###############################################################################################
#####################################      SINGLECTK      #####################################
###############################################################################################
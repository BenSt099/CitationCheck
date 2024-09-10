import os
import requests
import customtkinter
from tkinter import filedialog


def contact_crossref_api(email_address, data_dict):

        # api_url = "https://api.labs.crossref.org/works/10.2147/CMAR.S324920?mailto=ginny@crossref.org"
        api_url = "https://api.labs.crossref.org/works/" + data + "mailto=" + email_address
        response = requests.get(api_url)
        return response.json()

class UpperFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color="black")

        self.button1 = customtkinter.CTkButton(self, text="BIB", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.process_bibtex_file)
        self.button1.grid(row=1, column=1, padx=20, pady=20, sticky="ew", columnspan=1)
        self.button2 = customtkinter.CTkButton(self, text="SINGLE", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.openWindow)
        self.button2.grid(row=1, column=2, padx=20, pady=20, sticky="ew", columnspan=2)

        self.toplevel_window = None

    def openFileDialog(event=None):
        filepath = filedialog.askopenfilename()
        return filepath
        
    def process_bibtex_file(self):
        path = self.openFileDialog()

        if os.path.exists(path) and path.lower().endswith(".bib"):
            print("works")
        else:
            if not bool(path.strip()):
                print(path)
            else:
                print("doesn't work")
    
    def openWindow(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SingleCTk(self) 
            self.toplevel_window.attributes('-topmost', 1)
    
            while self.toplevel_window.closed != True:
                 self.update()

            k = self.toplevel_window.get_information()  
            
            self.toplevel_window.close()
            
        else:
            self.toplevel_window.focus()

class SingleCTk(customtkinter.CTkToplevel):
    information = {}
    closed = False
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x220")
        self.iconbitmap('logo.ico')
        self.resizable(False, False)
        self.title("CheckCitation - Input")
        self.grid_rowconfigure(3) 
        self.grid_columnconfigure(2)

        ###############################################################################
        ### Title ###
        self.label_title = customtkinter.CTkLabel(self, text="Title", font=customtkinter.CTkFont(family='times new roman 14 bold', size=17, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=20)

        self.title_input = customtkinter.CTkEntry(self, placeholder_text="Title", width=500, height=35)
        self.title_input.grid(row=0, column=1, padx=20, pady=20)
        ###############################################################################
        ### DOI ###
        self.label_doi = customtkinter.CTkLabel(self, text="DOI", font=customtkinter.CTkFont(family='times new roman 14 bold', size=17, weight="bold"))
        self.label_doi.grid(row=1, column=0, padx=20, pady=20)

        self.doi_input = customtkinter.CTkEntry(self, placeholder_text="DOI", width=500, height=35)
        self.doi_input.grid(row=1, column=1, padx=20, pady=20)
        ###############################################################################
        ### Buttons ###
        self.button1 = customtkinter.CTkButton(self, text="Cancel", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.close)      
        self.button1.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.button2 = customtkinter.CTkButton(self, text="CHECK", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.collect)
        self.button2.grid(row=2, column=2, padx=20, pady=20, sticky="ew")
        ###############################################################################

    def close(self):
        self.destroy()

    def collect(self):
        self.information = {
            "title_info": self.title_input.get(),
            "doi_info": self.doi_input.get()
        }
        self.withdraw()
        self.closed = True
        #self.close()

    def get_information(self):
        return self.information

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("800x600")
        self.title("CheckCitation")
        self.iconbitmap('logo.ico')
        ###self.grid_columnconfigure((2, 1), weight=1)


        self.grid_rowconfigure(2, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.upperframe = UpperFrame(master=self)
        self.upperframe.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        
    
    

app = App()
app.mainloop()
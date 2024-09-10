import os
import requests
import webbrowser
import customtkinter
from tkinter import filedialog
from PIL import Image

def contact_crossref_api(email_address, data_dict):

        # api_url = "https://api.labs.crossref.org/works/10.2147/CMAR.S324920?mailto=ginny@crossref.org"
        api_url = "https://api.labs.crossref.org/works/" + data + "mailto=" + email_address
        response = requests.get(api_url)
        return response.json()

class UpperFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color="black")
        self.toplevel_window = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        infoFrame = customtkinter.CTkFrame(master=self)
        infoFrame.grid(row=1, column=0, rowspan=4, padx=10, pady=10, sticky="ew")
        infoFrame.grid_rowconfigure(0, weight=1)
        infoFrame.grid_rowconfigure(1, weight=1)
        infoFrame.grid_rowconfigure(2, weight=1)
        infoFrame.grid_columnconfigure(0, weight=1)

        ###########################
        image_cc_icon = customtkinter.CTkImage(Image.open("logo.png"), size=(21,21))
        label_title = customtkinter.CTkButton(infoFrame, fg_color = "gray13", hover_color="gray13", text="CitationCheck", image=image_cc_icon, compound="left", font=customtkinter.CTkFont(family='times new roman 14 bold', size=20, weight="bold"))
        label_title.grid(row=0, column=0, padx=10, pady=10)

        middle = customtkinter.CTkFrame(master=infoFrame)
        middle.configure(fg_color="gray13")
        middle.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        middle.grid_rowconfigure(0, weight=1)
        middle.grid_columnconfigure(0, weight=1)
        middle.grid_columnconfigure(1, weight=1)

        leftinfo = customtkinter.CTkLabel(middle, text_color="lime green", text="Passed: -", height=10, font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"))
        leftinfo.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        rightinfo = customtkinter.CTkLabel(middle, text_color="firebrick3", text="Failed: -", height=10, font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"))
        rightinfo.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

        image_pdf = customtkinter.CTkImage(Image.open("filetype-pdf.png"), size=(20,20))
        label_title = customtkinter.CTkButton(infoFrame, fg_color = "#2a51fa", hover_color="#0c38f5", text_color="black", text="PDF", image=image_pdf, compound="right", font=customtkinter.CTkFont(family='times new roman 14 bold', size=17, weight="bold"), command=self.export_to_pdf)
        label_title.grid(row=2, column=0, padx=10, pady=10)
        ###########################

        controlFrame = customtkinter.CTkFrame(master=self)
        controlFrame.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        controlFrame.configure(fg_color="gray13")
        controlFrame.grid_rowconfigure(0, weight=1)
        controlFrame.grid_columnconfigure(0, weight=1)

        buttons = customtkinter.CTkFrame(master=controlFrame)
        buttons.grid(row=0, column=0, padx=100, pady=5, sticky="ew")
        buttons.configure(fg_color="gray13")
        buttons.grid_rowconfigure(0, weight=1)
        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(1, weight=1)

        button1 = customtkinter.CTkButton(buttons, text="BiB", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.process_bibtex_file)
        button1.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        button2 = customtkinter.CTkButton(buttons, text="SINGLE", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.openWindow)
        button2.grid(row=0, column=1, padx=10, pady=10, sticky="news")

    def export_to_pdf(self):
        pass

    def openFileDialog(event=None):
        filepath = filedialog.askopenfilename(filetypes=[("BibTex Files", "*.bib")])
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
            self.toplevel_window.grab_set()
            
            while self.toplevel_window.closed != True:
                self.update()

            k = self.toplevel_window.get_information()  
            
            self.toplevel_window.destroy_all()
            
        else:
            self.toplevel_window.focus()

class SingleCTk(customtkinter.CTkToplevel):
    information = {}
    closed = False
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x220")
        self.after(201, lambda: self.iconbitmap('logo.ico')) # fix from StackOverflow
        # https://stackoverflow.com/questions/75825190/how-to-put-iconbitmap-on-a-customtkinter-toplevel
        self.resizable(False, False)
        self.title("CheckCitation - Input")
        self.grid_rowconfigure(3) 
        self.grid_columnconfigure(2)

        ###############################################################################
        ### Title ###
        image_questionmark = customtkinter.CTkImage(Image.open("icon_questionmark.png"), size=(16,16))
        self.label_title = customtkinter.CTkButton(self, fg_color = "transparent", hover_color="#181818", text="Title", image=image_questionmark, compound="right", font=customtkinter.CTkFont(family='times new roman 14 bold', size=17, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=20)

        self.title_input = customtkinter.CTkEntry(self, placeholder_text="Title", width=500, height=35)
        self.title_input.grid(row=0, column=1, padx=20, pady=20)
        ###############################################################################
        ### DOI ###
        self.label_doi = customtkinter.CTkButton(self, fg_color = "transparent", hover_color="#181818", text="DOI", image=image_questionmark, compound="right", font=customtkinter.CTkFont(family='times new roman 14 bold', size=17, weight="bold"))
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
        self.closed = True
        self.withdraw()

    def destroy_all(self):
        self.destroy()

    def collect(self):
        self.information = {
            "title_info": self.title_input.get(),
            "doi_info": self.doi_input.get()
        }
        self.closed = True
        self.withdraw()

    def get_information(self):
        return self.information

class LowerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        innerFrame = customtkinter.CTkFrame(master=self, height=20)
        innerFrame.grid(row=0, column=0, padx=160, pady=10, sticky="ew")
        innerFrame.grid_rowconfigure(0, weight=1)
        innerFrame.grid_rowconfigure(1, weight=1)
        innerFrame.grid_columnconfigure(0, weight=1)

        upperFrame = customtkinter.CTkFrame(master=innerFrame)
        lowerFrame = customtkinter.CTkFrame(master=innerFrame)
        upperFrame.grid(row=0, column=0, sticky="ew")
        lowerFrame.grid(row=1, column=0, sticky="ew")

        upperFrame.grid_rowconfigure(0, weight=1)
        upperFrame.grid_columnconfigure(0, weight=1)
        lowerFrame.grid_rowconfigure(0, weight=1)
        lowerFrame.grid_columnconfigure(0, weight=1)
        lowerFrame.grid_columnconfigure(1, weight=1)

        label = customtkinter.CTkLabel(upperFrame, text="CitationCheck v1.0", height=10, font=customtkinter.CTkFont(family='times new roman 16 bold', size=16, weight="bold"))
        label.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        image_github = customtkinter.CTkImage(Image.open("logo_github.png"), size=(18,18))
        label_github = customtkinter.CTkButton(lowerFrame, fg_color = "transparent", height=10, hover_color="#181818", text="Homepage", image=image_github, compound="left", font=customtkinter.CTkFont(family='times new roman 14 bold', size=13, weight="bold"), command=self.openGitHub)
        label_github.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        image_issue = customtkinter.CTkImage(Image.open("issue.png"), size=(18,18))
        label_issue = customtkinter.CTkButton(lowerFrame, fg_color = "transparent", height=10, hover_color="#181818", text="Issues", image=image_issue, compound="left", font=customtkinter.CTkFont(family='times new roman 14 bold', size=13, weight="bold"), command=self.openGitHubIssue)
        label_issue.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

    def openGitHub(self):
        webbrowser.open_new(r"https://github.com/BenSt099/CitationCheck")

    def openGitHubIssue(self):
        webbrowser.open_new(r"https://github.com/BenSt099/CitationCheck/issues")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("dark-blue")
        self.geometry("800x600")
        self.title("CheckCitation")
        self.iconbitmap('logo.ico')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.upperframe = UpperFrame(master=self)
        self.upperframe.grid(row=0, column=0, padx=0, pady=0, rowspan=4, sticky="news")
        self.lowerframe = LowerFrame(master=self, height=10)
        self.lowerframe.grid(row=4, column=0, padx=0, pady=0, sticky="new")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
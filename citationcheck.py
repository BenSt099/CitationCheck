##################################################################
##################################################################
#           /************ CitationCheck ************/            #
#                             v1.0                               #
##################################################################
##################################################################

import os
import csv
import json
import requests
import threading
import webbrowser
import customtkinter
from tkinter import filedialog
from tkinter import StringVar
from PIL import Image
from pdf import create_pdf_and_save
from bibtex import process_bibtex_file

global_data = {}

def contact_crossref_api(data_list, email_address):
                         # data_list = ['title','doi']
    
    api_url = "https://api.labs.crossref.org/works/" + data_list[1] + "?mailto=" + email_address
    response = requests.get(api_url)
    return response.json()

def process_response(response_json):
    print(response_json)
    try:
        information = response_json['message']['cr-labs-updates'][0]['reasons']
    except KeyError:
        return -1
    return information
    
class UpperFrame(customtkinter.CTkFrame):
    update_already_in_progress = 0
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
        self.label_title = customtkinter.CTkButton(infoFrame, fg_color = "gray13", hover_color="gray13", text="CitationCheck", image=image_cc_icon, compound="left", font=customtkinter.CTkFont(family='times new roman 14 bold', size=20, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=10, pady=10)

        middle = customtkinter.CTkFrame(master=infoFrame)
        middle.configure(fg_color="gray13")
        middle.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        middle.grid_rowconfigure(0, weight=1)
        middle.grid_columnconfigure(0, weight=1)
        middle.grid_columnconfigure(1, weight=1)

        self.leftinfo = customtkinter.CTkLabel(middle, text_color="lime green", text="Passed: -", height=10, font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"))
        self.leftinfo.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        self.rightinfo = customtkinter.CTkLabel(middle, text_color="firebrick3", text="Failed: -", height=10, font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"))
        self.rightinfo.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

        settingsFrame = customtkinter.CTkFrame(master=infoFrame)
        settingsFrame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        settingsFrame.configure(fg_color="gray13")
        settingsFrame.grid_rowconfigure(0, weight=1)
        settingsFrame.grid_columnconfigure(0, weight=1)
        settingsFrame.grid_columnconfigure(1, weight=1)
        settingsFrame.grid_columnconfigure(2, weight=1)

        radioFrame = customtkinter.CTkFrame(master=settingsFrame)
        radioFrame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        radioFrame.configure(fg_color="gray13")
        radioFrame.grid_rowconfigure(0, weight=1)
        radioFrame.grid_rowconfigure(1, weight=1)
        radioFrame.grid_columnconfigure(0, weight=1)

        radio_var = StringVar(None,"1")
        self.radio_up = customtkinter.CTkRadioButton(radioFrame, text="Local [CSV]", variable=radio_var, value="1")
        self.radio_up.grid(row=0, column=0, padx=5, pady=2)
        self.radio_down = customtkinter.CTkRadioButton(radioFrame, text="Online [API]", variable=radio_var, value="2")
        self.radio_down.grid(row=1, column=0, padx=5, pady=2)

        image_update = customtkinter.CTkImage(Image.open("update.png"), size=(20,20))
        self.btn_text = StringVar()
        self.label_update = customtkinter.CTkButton(settingsFrame, textvariable=self.btn_text, fg_color = "#8a8888", hover_color="#636262", text_color="black", text="UPDATE", image=image_update, compound="right", font=customtkinter.CTkFont(family='times new roman 14 bold', size=17, weight="bold"), command=self.call_update)
        self.label_update.grid(row=0, column=1, padx=10, pady=5)
        self.btn_text.set("UPDATE")

        image_pdf = customtkinter.CTkImage(Image.open("filetype-pdf.png"), size=(20,20))
        label_pdf = customtkinter.CTkButton(settingsFrame, fg_color = "#3d89cc", hover_color="#2a70ad", text_color="black", text="PDF", image=image_pdf, compound="right", font=customtkinter.CTkFont(family='times new roman 14 bold', size=17, weight="bold"), command=self.export_to_pdf)
        label_pdf.grid(row=0, column=2, padx=10, pady=5)
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

        button1 = customtkinter.CTkButton(buttons, text="BiB", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.bibtex)
        button1.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        button2 = customtkinter.CTkButton(buttons, text="SINGLE", fg_color="#bf0041", hover_color="#8d0433", text_color='#000000', font=customtkinter.CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.single)
        button2.grid(row=0, column=1, padx=10, pady=10, sticky="news")

    def call_update(self):
        if self.update_already_in_progress == 0:
            content_dict = {}
            self.update_already_in_progress = 1
            with open('cc_email.json') as email_file:
                content_dict = json.load(email_file)
            
            self.btn_text.set("Working...")
            self.update_and_save(content_dict['email'])
        
    def return_to_normal_state(self):
        self.btn_text.set("UPDATE")
        self.update_already_in_progress = 0

    def update_and_save(self, email_address):
        threading.Thread(target=self.download_csv, args=(email_address,self.return_to_normal_state), daemon=True).start()

    def download_csv(self, email_address, callback_f):
        api_url = r"https://api.labs.crossref.org/data/retractionwatch?" + email_address
        response = requests.get(api_url)
        with open(os.getcwd() + "/CitationCheck_data_CROSSREF_099.csv", 'wb') as f:
            f.write(response.content)
        callback_f()

    def update_info_label(self, info):
        self.label_title.configure(text = info)

    def update_left(self, info):
        self.leftinfo.configure(text = info)

    def update_right(self, info):
        self.rightinfo.configure(text = info)

    ### bibtex
    def openFileDialog(event=None):
        filepath = filedialog.askopenfilename(filetypes=[("BibTex Files", "*.bib")])
        return filepath
        
    def bibtex(self):
        path = self.openFileDialog()

        if os.path.exists(path) and path.lower().endswith(".bib"):
            dict_information = process_bibtex_file(path)

            content_dict = {}
            with open('cc_email.json') as email_file:
                content_dict = json.load(email_file)

        else:
            if not bool(path.strip()):
                pass
            else:
                pass
    ### bibtex
    
    def export_to_pdf(self):
        filename = filedialog.asksaveasfilename(title="Choose location", filetypes=[("PDF Files", "*.pdf")])
        create_pdf_and_save(filename, global_data)
        
    ### single
    def single(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SingleCTk(self) 
            self.toplevel_window.attributes('-topmost', 1)
            self.toplevel_window.grab_set()
            
            while self.toplevel_window.closed != True:
                self.toplevel_window.update()

            k = self.toplevel_window.get_information()
            self.toplevel_window.destroy_all()
            content_dict = {}
            with open('cc_email.json') as email_file:
                content_dict = json.load(email_file)

            if k != [] and k != ['','']:
                response_info = contact_crossref_api(k, content_dict['email'])
                result = process_response(response_info)
                print(result)
            
        else:
            self.toplevel_window.focus()
    ### single

class SingleCTk(customtkinter.CTkToplevel):
    information = []
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
        self.information.append(self.title_input.get())
        self.information.append(self.doi_input.get())
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

        content_dict = {}
        with open('cc_email.json') as email_file:
            content_dict = json.load(email_file)

        if content_dict == {}:
            dialog = customtkinter.CTkInputDialog(text="Please type in your e-mail address:", title="EMail-Address", button_fg_color="#bf0041", button_hover_color="#8d0433", button_text_color="black", font=customtkinter.CTkFont(family='times new roman 16 bold', size=17, weight="bold"))
            email = dialog.get_input()
            content_dict = {
                'email': email
            }
            with open("cc_email.json", mode="w", encoding="utf-8") as email_file:
                json.dump(content_dict, email_file)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
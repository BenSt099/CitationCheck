from os import getcwd
from os.path import exists
from threading import Thread
from multiprocessing import Pool
from difflib import get_close_matches
from pandas import read_csv
from PIL import Image
from re import sub
from requests import get
from json import load
from cc_pdfbuilder import cc_build_and_save_pdf
from cc_process_bibtex import process_bibtex_file
import cc_singlectk
from tkinter import filedialog
from tkinter import IntVar
from tkinter import StringVar
from customtkinter import CTkFont
from customtkinter import CTkButton
from customtkinter import CTkLabel
from customtkinter import CTkFrame
from customtkinter import CTkImage
from customtkinter import CTkRadioButton
from customtkinter import get_appearance_mode

###############################################################################################
#####################################      UPPERFRAME     #####################################
###############################################################################################
class UpperFrame(CTkFrame):
    global_data = {}
    update_already_in_progress = 0
    query_result_csv = []
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ###########################

        if get_appearance_mode() == 'Light':
            textcolor = "black"
            hovercolor = "#d9d8d7"  
            textbuttoncolor = "white"
        else:
            textbuttoncolor = "black"
            textcolor = "white"
            hovercolor = "gray13"

        ###########################
        
        self.configure(fg_color=textbuttoncolor)
        self.toplevel_window = None
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        infoFrame = CTkFrame(master=self, fg_color=hovercolor)
        infoFrame.grid(row=1, column=0, rowspan=4, padx=10, pady=10, sticky="ew")
        infoFrame.grid_rowconfigure(0, weight=1)
        infoFrame.grid_rowconfigure(1, weight=1)
        infoFrame.grid_rowconfigure(2, weight=1)
        infoFrame.grid_columnconfigure(0, weight=1)
        
        image_cc_icon = CTkImage(Image.open("logo.png"), size=(21,21))
        self.label_title = CTkButton(infoFrame, fg_color=hovercolor, hover_color=hovercolor, text_color=textcolor, text="CitationCheck", image=image_cc_icon, compound="left", font=CTkFont(family='times new roman 14 bold', size=20, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=10, pady=10)

        middle = CTkFrame(master=infoFrame)
        middle.configure(fg_color=hovercolor)
        middle.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        middle.grid_rowconfigure(0, weight=1)
        middle.grid_columnconfigure(0, weight=1)
        middle.grid_columnconfigure(1, weight=1)

        self.leftinfo = CTkLabel(middle, text_color="lime green", text="Passed: -", height=10, font=CTkFont(family='times new roman 16 bold', size=20, weight="bold"))
        self.leftinfo.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        self.rightinfo = CTkLabel(middle, text_color="firebrick3", text="Failed: -", height=10, font=CTkFont(family='times new roman 16 bold', size=20, weight="bold"))
        self.rightinfo.grid(row=0, column=1, padx=0, pady=0, sticky="ew")

        settingsFrame = CTkFrame(master=infoFrame)
        settingsFrame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        settingsFrame.configure(fg_color=hovercolor)
        settingsFrame.grid_rowconfigure(0, weight=1)
        settingsFrame.grid_columnconfigure(0, weight=1)
        settingsFrame.grid_columnconfigure(1, weight=1)
        settingsFrame.grid_columnconfigure(2, weight=1)

        radioFrame = CTkFrame(master=settingsFrame)
        radioFrame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        radioFrame.configure(fg_color=hovercolor)
        radioFrame.grid_rowconfigure(0, weight=1)
        radioFrame.grid_rowconfigure(1, weight=1)
        radioFrame.grid_columnconfigure(0, weight=1)

        self.radio_var = IntVar()
        self.radio_var.set(1)
        self.radio_up = CTkRadioButton(radioFrame, text="Local [CSV]", variable=self.radio_var, value=1)
        self.radio_up.grid(row=0, column=0, padx=5, pady=2)
        self.radio_down = CTkRadioButton(radioFrame, text="Online [API]", variable=self.radio_var, value=2)
        self.radio_down.grid(row=1, column=0, padx=5, pady=2)

        image_update = CTkImage(Image.open("update.png"), size=(20,20))
        self.btn_text = StringVar()
        self.label_update = CTkButton(settingsFrame, textvariable=self.btn_text, fg_color = "#8a8888", hover_color="#636262", text_color="black", text="UPDATE", image=image_update, compound="right", font=CTkFont(family='times new roman 14 bold', size=17, weight="bold"), command=self.call_update)
        self.label_update.grid(row=0, column=1, padx=10, pady=5)
        self.btn_text.set("UPDATE")

        image_pdf = CTkImage(Image.open("filetype-pdf.png"), size=(20,20))
        label_pdf = CTkButton(settingsFrame, fg_color = "#3d89cc", hover_color="#2a70ad", text_color="black", text="PDF", image=image_pdf, compound="right", font=CTkFont(family='times new roman 14 bold', size=17, weight="bold"), command=self.export_to_pdf)
        label_pdf.grid(row=0, column=2, padx=10, pady=5)
        ###########################

        controlFrame = CTkFrame(master=self)
        controlFrame.configure(fg_color=hovercolor)
        controlFrame.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        controlFrame.grid_rowconfigure(0, weight=1)
        controlFrame.grid_columnconfigure(0, weight=1)

        buttons = CTkFrame(master=controlFrame)
        buttons.grid(row=0, column=0, padx=100, pady=5, sticky="ew")
        
        buttons.configure(fg_color=hovercolor)
        buttons.grid_rowconfigure(0, weight=1)
        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(1, weight=1)

        button1 = CTkButton(buttons, text="BiB", fg_color="#bf0041", hover_color="#8d0433", text_color=textbuttoncolor, font=CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.process_bibtex_query_master_f)
        button1.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        button2 = CTkButton(buttons, text="SINGLE", fg_color="#bf0041", hover_color="#8d0433", text_color=textbuttoncolor, font=CTkFont(family='times new roman 16 bold', size=20, weight="bold"), command=self.process_single_query_master_f)
        button2.grid(row=0, column=1, padx=10, pady=10, sticky="news")
    
    ###############################################
    ############# UPPERFRAME: methods #############
    ###############################################

    def call_update(self):
        if self.update_already_in_progress == 0:
            content_dict = {}
            self.update_already_in_progress = 1
            with open('cc_email.json') as email_file:
                content_dict = load(email_file)
            
            self.btn_text.set("Working...")
            self.update_and_save(content_dict['email'])
        
    def return_to_normal_state(self):
        self.btn_text.set("UPDATE")
        self.update_already_in_progress = 0

    def update_and_save(self, email_address):
        Thread(target=self.download_csv, args=(email_address,self.return_to_normal_state), daemon=True).start()

    def download_csv(self, email_address, callback_f):
        api_url = r"https://api.labs.crossref.org/data/retractionwatch?" + email_address
        response = get(api_url)
        with open(getcwd() + "/CitationCheck_data_CROSSREF_099.csv", 'wb') as f:
            f.write(response.content)
        callback_f()

    ############################################################################# bibtex
    
    def openFileDialog(event=None):
        filepath = filedialog.askopenfilename(filetypes=[("BibTex Files", "*.bib")])
        return filepath
        
    def process_bibtex_query_master_f(self):
        path = self.openFileDialog()

        if exists(path) and path.lower().endswith(".bib"):
            data = process_bibtex_file(path)
            # ['short title', 'title', 'doi']

            if self.radio_var.get() == 1: # local [csv]
                if data != [] and data != ['','']:
                    self.label_title.configure(text = "Working...")
                    self.process_bibtex_query_call_process_bibtex_csv(data)
            else: # online [api]
                if data != [] and data != ['','']:
                    self.label_title.configure(text = "Working...")
                    self.process_bibtex_query_call_process_bibtex_api(data)
    
    def process_bibtex_query_call_process_bibtex_csv(self, data):
        Thread(target=self.process_bibtex_csv, args=(data,self.process_bibtex_query_update_ui), daemon=True).start()

    def process_bibtex_query_call_process_bibtex_api(self, data):
        Thread(target=self.process_bibtex_api, args=(data,self.process_bibtex_query_update_ui), daemon=True).start()

    def process_bibtex_query_update_ui(self, results):
        self.label_title.configure(text = "CitationCheck")
        passed = 0
        failed = 0
        for result_entry in results:
            if result_entry[0] == False:
                passed = passed + 1    
            else:
                self.query_result_csv.append([result_entry[1], result_entry[2], result_entry[3]])
                failed = failed + 1
        self.leftinfo.configure(text = "Passed: " + str(passed))
        self.rightinfo.configure(text = "Failed: " + str(failed))

    ### bibtex - csv
    def process_bibtex_csv(self, data, callback_f):
        results = []
        with Pool() as pool:
            results = pool.map(search_in_csv, data)
        callback_f(results)

    ### bibtex - api
    def process_bibtex_api(self, data, callback_f):
        results = []
        with Pool() as pool:
            results = pool.map(search_api, data)
        callback_f(results)

    ############################################################################# bibtex

    def is_data_available(self):
        return self.query_result_csv != []
    
    def export_to_pdf(self):
        if self.is_data_available():
            filename = filedialog.asksaveasfilename(title="Choose location", filetypes=[("PDF Files", "*.pdf")])
            cc_build_and_save_pdf(filename, self.query_result_csv)
        
    ############################################################################# single
        
    def process_single_query_master_f(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = cc_singlectk.SingleCTk(self) 
            self.toplevel_window.attributes('-topmost', 1)
            self.toplevel_window.grab_set()
            
            while self.toplevel_window.closed != True:
                self.toplevel_window.update()

            k = self.toplevel_window.get_information()
            self.toplevel_window.destroy_window()
            content_dict = {}
            with open('cc_email.json') as email_file:
                content_dict = load(email_file)

            if self.radio_var.get() == 1: # local [csv]
                if k != [] and k != ['','']:
                    self.label_title.configure(text = "Working...")
                    self.process_single_query_call_process_csv(k)
            else: # online [api]
                if k != [] and k != ['','']:
                    self.label_title.configure(text = "Working...")
                    self.process_single_query_call_process_api(k, content_dict['email'])
        else:
            self.toplevel_window.focus()

    def process_single_query_call_process_csv(self, data):
        Thread(target=self.process_single_query_process_csv, args=(data,self.process_single_query_update_ui), daemon=True).start()

    def process_single_query_process_csv(self, data, callback_f):
        dataset = read_csv('CitationCheck_data_CROSSREF_099.csv', dtype={'OriginalPaperDOI': str, 'Reason': str})
        result_list = []
        if data[1] == '': # use title
            title_set = dataset['Title']
            reason_set = dataset['Reason']
            titlelist = title_set.to_list()
            best_match_title = get_close_matches(data[0], titlelist, n=1, cutoff=0.6)
            if len(best_match_title) == 0 or (len(best_match_title) == 1 and best_match_title[0].strip() == ''):
                result_list.append(False)
            subsettitle = title_set[title_set == best_match_title[0]]
            result_list.append(True)
            result_list.append(data[0])
            result_list.append(best_match_title[0])
            result_list.append(reason_set[subsettitle.index.item()])
        else: # otherwise, use always doi
            originalpaperdoi_set = dataset['OriginalPaperDOI'].astype(str)
            reason_set = dataset['Reason'].astype(str)
            doi_cleaned = data[1]
            
            if "https://doi.org/" in doi_cleaned:
                doi_cleaned = sub("https://doi.org/", "", doi_cleaned)

            subsetdoi = originalpaperdoi_set[originalpaperdoi_set == doi_cleaned]
            setdoilist = subsetdoi.to_list()
            if len(setdoilist) == 0 or (setdoilist[0] == '' and len(setdoilist) == 1):
                result_list.append(False)
            else:
                result_list.append(True)
                result_list.append(data[0])
                result_list.append(setdoilist[0])
                result_list.append(reason_set[subsetdoi.index.item()])
        callback_f(result_list)
    
    def process_single_query_update_ui(self, result_list):
        self.label_title.configure(text = "CitationCheck")
        if result_list[0] == False:
            self.leftinfo.configure(text = "Passed: 1")
            self.rightinfo.configure(text = "Failed: 0")
        else:
            self.leftinfo.configure(text = "Passed: 0")
            self.rightinfo.configure(text = "Failed: 1")
            self.query_result_csv.append([result_list[1], result_list[2], result_list[3]])
        
    def process_single_query_call_process_api(self, data, email_address):
        Thread(target=self.process_single_query_process_api, args=(data, email_address, self.process_single_query_update_ui), daemon=True).start()

    def process_single_query_process_api(self, data, email_address, callback_f):
                                             # data = ['title','doi']
        result_list = []
        api_url = "https://api.labs.crossref.org/works/" + data[1] + "?mailto=" + email_address
        response = get(api_url)
        result_json = response.json()
        try:
            information = result_json['message']['cr-labs-updates'][0]['reasons']
            compressed = ''
            for x in information:
                compressed = compressed + '+' + x + ';'
            result_list.append(True)
            result_list.append(data[0])
            result_list.append(data[1])
            result_list.append(compressed)
        except KeyError:
            result_list.append(False)
        callback_f(result_list)

    ############################################################################# single

###############################################################################################
#####################################      UPPERFRAME     #####################################
###############################################################################################

def search_in_csv(entry):
    data = []
    data.append(entry[1])
    if len(entry) > 2:
        data.append(entry[2])
    else:
        data.append('')
    dataset = read_csv('CitationCheck_data_CROSSREF_099.csv', dtype={'OriginalPaperDOI': str, 'Reason': str})
    result_list = []
    if data[1] == '': # use title
        title_set = dataset['Title']
        reason_set = dataset['Reason']
        titlelist = title_set.to_list()
        best_match_title = get_close_matches(data[0], titlelist, n=1, cutoff=0.6)
        if len(best_match_title) == 0 or (len(best_match_title) == 1 and best_match_title[0].strip() == ''):
            result_list.append(False)
        else:    
            subsettitle = title_set[title_set == best_match_title[0]]
            result_list.append(True)
            result_list.append(data[0] + ' [' +  entry[0] + ']')
            result_list.append(best_match_title[0])
            result_list.append(reason_set[subsettitle.index.item()])
    else: # otherwise, use always doi
        originalpaperdoi_set = dataset['OriginalPaperDOI'].astype(str)
        reason_set = dataset['Reason'].astype(str)
        subsetdoi = originalpaperdoi_set[originalpaperdoi_set == data[1]]
        setdoilist = subsetdoi.to_list()
        if len(setdoilist) == 0 or (setdoilist[0] == '' and len(setdoilist) == 1):
            result_list.append(False)
        else:
            result_list.append(True)
            result_list.append(data[0] + ' [' + entry[0] + ']')
            result_list.append(setdoilist[0])
            result_list.append(reason_set[subsetdoi.index.item()])
    return result_list

def search_api(entry):
    # entry = [name, title, doi]
    data = []
    result_list = []
    data.append(entry[1])
    if len(entry) > 2:
        data.append(entry[2])
    else:
        data.append('')
    with open('cc_email.json') as email_file:
        content_dict = load(email_file)
    
    if data[1] != '':
        api_url = "https://api.labs.crossref.org/works/" + data[1] + "?mailto=" + content_dict['email']
        response = get(api_url)
        result_json = response.json()
        try:
            information = result_json['message']['cr-labs-updates'][0]['reasons']
            compressed = ''
            for x in information:
                compressed = compressed + '+' + x + ';'
            result_list.append(True)
            result_list.append(data[0] + ' [' + entry[0] + ']')
            result_list.append(data[1])
            result_list.append(compressed)
        except KeyError:
            result_list.append(False)
    else:
        result_list.append(False)
    return result_list
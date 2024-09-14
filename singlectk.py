import customtkinter
from PIL import Image

###############################################################################################
#####################################      SINGLECTK      #####################################
###############################################################################################
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

        self.protocol("WM_DELETE_WINDOW", self.close)

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

    def destroy_window(self):
        self.destroy()

    def collect(self):
        self.information.append(self.title_input.get())
        self.information.append(self.doi_input.get())
        self.withdraw()
        self.closed = True

    def get_information(self):
        return self.information
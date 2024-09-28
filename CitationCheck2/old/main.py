import webview

class Api:
    
    def pp(self, input):
        print(input)

if __name__ == '__main__':
    api = Api()
    webview.create_window('CitationCheck', './gui/main.html', js_api=api, text_select=True, width=1000, height=600)
    webview.start()
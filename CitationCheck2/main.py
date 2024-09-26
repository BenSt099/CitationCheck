import webview

class Api:
    pass
    # def addItem(self, title):
    #     print('Added item %s' % title)

    # def removeItem(self, item):
    #     print('Removed item %s' % item)

    # def editItem(self, item):
    #     print('Edited item %s' % item)

    # def toggleItem(self, item):
    #     print('Toggled item %s' % item)

    # def toggleFullscreen(self):
    #     webview.windows[0].toggle_fullscreen()

if __name__ == '__main__':
    api = Api()
    webview.create_window('CitationCheck', './gui/main.html', js_api=api, text_select=True, maximized=True)
    webview.start()
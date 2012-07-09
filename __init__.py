"""

Pterm provides UI elements for building a variety of functional console applications and a keyboard interface thereto.

"""

from Tkinter import *
from root import RootApp

class Pterm(Frame):
    "Python terminal with flexible UI"

    def __init__(self, title, w, h):
        self.master = Tk()
        self.master.title(title)
        self.title = title
        self.width = w
        self.height = h
        self.apps = {}

    def run(self, app, options=None):
        if not self.apps.has_key(app.name):
            self.apps[app.name] = app(self,
                                      Canvas(self.master,
                                             width=self.width,
                                             height=self.height),
                                      options, self.width, self.height)
        self.master.mainloop()

# Start Pterm
pt = Pterm("Pterm", 1024, 768)
pt.run(RootApp)
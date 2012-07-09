"""

Pterm provides UI elements for building a variety of functional console applications and a keyboard interface thereto.

"""

import Tkinter as tk
from lib import *
from root import Root

class Pterm(tk.Frame):
    "Python terminal with flexible UI"

    # Version
    _version = 'Pterm 0.0.001'

    # Default Options
    defaults = {'title': 'Pterm', 'width': 1024, 'height': 768}

    def __init__(self, **options):

        for key, value in self.defaults.items():
            if not options.has_key(key) or options[key] is None:
                options[key] = value
        self.options = options

        # Create graphics
        self.w = tk.Tk()
        self.w.title(options['title'])
        self.width = options['width']
        self.height = options['height']
        self.c = tk.Canvas(self.w,
                             width=self.width,
                             height=self.height)
        self.c.pack()
        self.w.bind_all('<Key>', self.keypress)
        self.app = Root(self)
        self.term = self
        self.update()
        self.w.mainloop()

    def title(self, title):
        self.options['title'] = title
        self.w.title(' - '.join([title, self._version]))

    def update(self):
        pass

    def keypress(self, event):
        method = '_'.join(['key', event.keysym.lower()])
        if hasattr(self.app, method):
            self.react(getattr(self.app, method)(event))

    def exit(self):
        self.w.destroy()

    def react(self, what):
        if isinstance(what, App):
            self.app = what
            self.update()

# Start Pterm
pt = Pterm(title="Pterm Loading...")
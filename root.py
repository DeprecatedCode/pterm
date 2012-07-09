"""

This is the root app that runs when Pterm is run

"""

from lib import *

class Root(BucketApp):
    "Root Pterm Application"

    _name = 'Root'

    def activate(self):
        self.title("Welcome")
        return self

    def title(self, title):
        self.parent.title(title)

    def exit(self):
        "Exit Pterm"
        self.parent.exit()

    def key_escape(self, event):
        print 'Loading exit ConfirmApp'
        self.title('Exit?')
        return ConfirmApp(self, "Are you sure you would like to exit Pterm?", self.exit, self.activate)
import ui

class App:
    "App holds logical functionality"

    def __init__(self, parent):

        self.parent = parent
        self._update = True

        try:
            self.activate()
        except AttributeError:
            pass

    def exit(self):
        return self.parent

    def title(self, title):
        self.parent.title(' - '.join([title, self._name]))

    def update(self):
        pass

class BucketApp(App):
    "BucketApp contains an app and a bucket list of matching commands"

    def __init__(self, parent):
        self.match = []
        App.__init__(self, parent)

    def key_escape(self, event):
        if len(self.match) == 0:
            return self.exit()
        else:
            del self.match[:]
            self._update = True

class ConfirmApp(App):
    "ConfirmApp contains a simple confirmation message and two options"

    def __init__(self, parent, message="Are you sure?", confirm=None, cancel=None):
        self.message = message
        self.confirm = confirm
        self.cancel = cancel
        App.__init__(self, parent)
        print 'ConfirmApp Loaded with message: ' + message

    def key_return(self, event):
        print ' >> Confirmed!'
        if self.confirm is not None:
            return self.confirm()
        return self.exit()

    def key_escape(self, event):
        print ' >> Abandoned!'
        if self.cancel is not None:
            return self.cancel()
        return self.exit()
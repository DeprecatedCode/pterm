class Area:
    "Any UI element should descend from Area"

    pass

class Bucket(Area):
    "UI list with character matching wizardry"

    def __init__(self, items=None):
        if(items is None):
            items = []
        self.items = items
        self.uiText = {}                    # Hold Text objects
        self.uiTextKeys = []
        self.ready = False
        self.visible = False

    def setBounds(self, bounds):
        self.bounds = bounds
        self.visible = True
        self.ready = False                  # Mark for recalc

    def add(self, item):
        self.items.append(item)
        self.ready = False                  # Mark for recalc

    def remove(self, item):
        self.items.remove(item)
        if self.uiText.has_key(item):
            self.uiText.remove(item)
        if self.uiTextKeys.has_key(item):
            self.uiTextKeys.remove(item)
        self.ready = False                  # Mark for recalc

    def prepare(self):
        self.uiTextKeys = []
        for item in self.items:
            if not self.uiText.has_key(item):
                self.uiText[item] = Text(Point(0,0), item)
            self.uiTextKeys.append(item)

            # Calculate position

    def draw(self, window):
        if(self.visible is False):
            return
        for x in self.uiTextKeys:
            self.uiText[x].undraw()
        if(self.ready is False):
            self.prepare()
        for x in self.uiTextKeys:
            self.uiText[x].draw(window)
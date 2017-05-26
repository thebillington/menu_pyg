#Class that implements the most basic menu item
class menuItem(object):

    def __init__(self, text, f):

        #Store the text and function
        self.item_text = text
        self.function = f

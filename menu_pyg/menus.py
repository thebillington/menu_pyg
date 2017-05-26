#Class that implements the most basic menu
class Menu(object):

    def __init__(self, screen):

        #Store the screen
        self.screen = screen

        #Setup a list of menu items
        self.menu_items = []

    def add_item(self, item):

        #Add the item
        self.menu_items.append(item)

    def list_items(self):

        for item in self.menu_items:
            print item.text

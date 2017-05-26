#Class that implements the most basic menu
class Menu(object):

    def __init__(self, screen, x, y, width, height, font, aa, colour):

        #Store the screen
        self.screen = screen

        #Setup a list of menu items
        self.menu_items = []

        #Setup a list to store the renders
        self.item_renders = []

        #Set the position of the menu
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #Store the font and render options
        self.font = font
        self.aa = aa
        self.colour = colour

    #Function to render all of the fonts
    def render_items(self):

        self.item_renders = []

        #For each item, render
        for item in self.menu_items:
            self.item_renders.append(self.font.render(item.text, self.aa, self.colour))

    def add_item(self, item):

        #Add the item
        self.menu_items.append(item)

        #Render the fonts
        self.render_items()

    def list_items(self):

        for item in self.menu_items:
            print item.text

    def render(self):

        #Store how much to move the y by for each item
        y_increment = 0

        for r in self.item_renders:
            self.screen.blit(r, (self.x, self.y + y_increment))
            y_increment = r.get_height()

#Class that implements the most basic menu item
class menuItem(object):

    def __init__(self, text, f):

        print("Menu item created: {}".format(text))
        f()

import kivy
kivy.require('1.10.0') 

from kivy.app import App


class Gui(App):

    def build(self):
        pass

    def button_click(self):
        print("CLICKED")


if __name__ == '__main__':
    Gui().run()
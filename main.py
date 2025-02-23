from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from text import Label_About


class Layout_Menu(BoxLayout):
    pass

class Manager(ScreenManager):
    pass

class Screen_StartGame(Screen):
    pass

class Screen_Home(Screen):
    pass
class Screen_About(Screen):
    pass
    
class Object_Player(Widget):
    def __init__(self, **kwargs):
        super(Object_Player, self).__init__(**kwargs)
        self.size = (100, 150)
        self.pos = (Window.width/2  - self.size[0]/2, 0)

        with self.canvas:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

class MyApp(App):
    def build(self):
        sm = Manager()
        sm.add_widget(Screen_Home(name='home'))
        sm.add_widget(Screen_StartGame(name='startgame'))
        sm.add_widget(Screen_About(name='about'))
        return sm

if __name__ == '__main__':
    
    MyApp().run()

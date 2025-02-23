from kivy.uix.button import Button
from kivy.graphics import Color, Line

class Btn_StartGame(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Nhấn vào tôi!'
        self.font_size = 30
        self.size_hint = (0.5, 0.5)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.9}
        self.background_color = (0, 0, 1, 1)
        
        
        
        self.bind(on_press=self.on_button_press, on_release=self.on_button_release)

    def on_button_press(self, instance):
        self.text = 'Bạn đã nhấn vào tôi!'
    def on_button_release(self, instance):
        self.text = 'Nhấn vào tôi!'

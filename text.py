from kivy.uix.label import Label

class Label_StartGame(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 40
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.text = 'Nhấn Start để bắt đầu trò chơi!'

class Label_About(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 40
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.text = 'Đây là trò chơi về xếp hình!'

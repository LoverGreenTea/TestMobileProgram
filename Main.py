from gettext import install

import kivy
import pip
from kivy.app import *
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager


class FirstScreen():
    def __init__(self, **kw):
        super().__init__(self, **kw)
        btn1 = Button(text="цей текст в перщому вікни")
        btn1.on_press = self.go_to_second

    def go_to_second(self):
        self.manager.current = "second"
class SecondScreen():
    def __init__(self, **kw):
        super().__init__(**kw)
        btn1 = Button(text="screen2")
        btn1.on_press = self.go_to_first

    def go_to_first(self):
        self.manager.current = "first"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        return sm

MyApp().run()

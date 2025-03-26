from gettext import install

import kivy
import pip
from kivy.app import *
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class FirstScreen():
    def __init__(self, **kw):
        super().__init__(self, **kw)
        btn = Button(text="цей текст в перщому вікни")
        btn.on_press = self.go_to_second
        self.add_widget(btn)
    def go_to_second(self):
        self.manager.current = "second"
class SecondScreen():
    def __init__(self, **kw):
        super().__init__(**kw)
        btn = Button(text="screen2")
        btn.on_press = self.go_to_first
        self.add_widget(btn)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        return sm

MyApp().run()

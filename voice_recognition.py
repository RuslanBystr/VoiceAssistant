from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

import pyttsx3
import os


class SpeakEngine:
    def __init__(self, voice, volume=0.5):
        self.voice = voice
        self.volume = volume
        self.conversation_speed = 100
        self.speak_engine = pyttsx3.init()

    def __str__(self):
        return self.voice.name

    def __call__(self, _):
        self.speak_engine.setProperty("voice", self.voice)
        self.speak_engine.setProperty("volume", self.volume)
        self.speak_engine.setProperty("rate", self.conversation_speed)
        self.speak_engine.say(MyApp.text_cmd.text)
        self.speak_engine.runAndWait()
        self.speak_engine.stop()


class TextToSpeechApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bl = BoxLayout(orientation="vertical", padding=20)
        self.gl = GridLayout(cols=3, spacing=3)

        self.text_cmd = TextInput(text="Введіть текст для відтворення", size_hint=(1, .5))

        self.lbl_cmd = Label(text="Enter text for синнтезованим голосом Volodymyr", font_size=20, halign="left", valign="center", size_hint=(1, .5),
                             text_size=(Window.size[0] - 40, Window.size[1] / 20))

        self.speed = speak.conversation_speed
        self.lbl_response = Label(text=f"Швидкість: {self.speed}",
                                  font_size=20,
                                  halign="center",
                                  valign="center",
                                  size_hint=(1, .5),
                                  text_size=(Window.size[0] - 40, Window.size[1] / 20))

        self.lbl = Label(text="add command",
                         font_size=20,
                         halign="left",
                         valign="center",
                         size_hint=(1, .5),
                         text_size=(Window.size[0] - 40, Window.size[1] / 20))

        self.lbl1 = Label(text="Select a table:",
                          font_size=20,
                          halign="left",
                          valign="center",
                          size_hint=(1, .5),
                          text_size=(Window.size[0] - 40, Window.size[1] / 20))

    def build(self):
        self.bl.add_widget(self.lbl_cmd)
        self.bl.add_widget(self.text_cmd)
        self.bl.add_widget(self.lbl)
        self.bl.add_widget(self.lbl1)
        self.gl.add_widget(Button(text="+", on_press=self.speed_up, font_size=32))
        self.gl.add_widget(self.lbl_response)
        self.gl.add_widget(Button(text="-", on_press=self.speed_down, font_size=32))
        self.gl.add_widget(Button(text="V+", on_press=self.speed_up, font_size=32))
        self.gl.add_widget(Button(text="V-", on_press=self.speed_down, font_size=32))
        self.gl.add_widget(Button(text="record", on_press=speak, font_size=32))

        self.bl.add_widget(self.gl)

        return self.bl

    def speed_up(self, _):
        speak.conversation_speed += 10
        self.lbl_response.text = f"speed: {speak.conversation_speed}"

    def speed_down(self, _):
        speak.conversation_speed -= 10
        self.lbl_response.text = f"speed: {speak.conversation_speed}"


if __name__ == '__main__':
    speak = SpeakEngine("HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\TokenEnums\\RHVoice\\Volodymyr")
    MyApp = TextToSpeechApp()
    MyApp.run()

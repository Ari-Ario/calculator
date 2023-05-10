import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        main_layout= BoxLayout(orientation="vertical")

        return main_layout
    
if __name__== "__main__":
    app= CalculatorApp()
    app.run()
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operations = ["+", "-", "*", "/"]
        main_layout = BoxLayout(orientation="vertical")
        self.solution= TextInput(readonly= True, font_size=40)
        main_layout.add_widget(self.solution)

        return main_layout
    
if __name__== "__main__":
    app= CalculatorApp()
    app.run()

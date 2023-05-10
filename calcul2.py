import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        main_layout= BoxLayout(orientation="vertical")
        self.text_box= TextInput(font_size= 30)
        main_layout.add_widget(self.text_box)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "Clear", "+"],
            ]

        for row in buttons:
            y_layout= BoxLayout(spacing=5)
            for i in row:
                butt=Button(text=f"{i}")
                #butt.bind(on_press=self.write)
                y_layout.add_widget(butt)
            main_layout.add_widget(y_layout)
        equal_butt= Button(text= "=")
        #equal_butt.bind(on_press= self.solve)
        main_layout.add_widget(equal_butt)
        
        return main_layout
    
if __name__== "__main__":
    app= CalculatorApp()
    app.run()
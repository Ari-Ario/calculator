import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operations = ["+", "-", "*", "/"]
        main_layout= BoxLayout(orientation="vertical", spacing=3)
        self.text_box= TextInput(font_size= 30)
        main_layout.add_widget(self.text_box)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "Clear", "+"],
            ]

        for row in buttons:
            y_layout= BoxLayout(spacing=3)
            for i in row:
                butt=Button(text=f"{i}")
                butt.bind(on_press=self.write)
                y_layout.add_widget(butt)
            main_layout.add_widget(y_layout)
        equal_butt= Button(text= "=")
        equal_butt.bind(on_press= self.solve)
        main_layout.add_widget(equal_butt)
        
        return main_layout
    
    #Method solve to show the result on the screen
    def solve(self, instance):
        curr = self.text_box.text
        curr_lst= curr.split("=")
        curr_last= curr_lst[-1]
        if curr:
            res = str(eval(curr_last))
            curr += " = " +res
            self.text_box.text= curr

    #Method write to enter the button-text into the textbox/screen
    def write(self, instance):
        input= instance.text
        curr= self.text_box.text
        if curr=="" and input in self.operations:
            self.text_box.text=""
        elif curr!="" and (curr[-1] in self.operations and input in self.operations):
            self.text_box.text = curr
        else:
            self.text_box.text += input
    
if __name__== "__main__":
    app= CalculatorApp()
    app.run()
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
        previous_text= self.text_box.text
        lines= [line for line in self.text_box.text.split("\n")]
        for line in lines:
            curr = line
            curr_list= curr.split("=")
            if not curr_list[-1].isalnum():
                curr_last= curr_list[-1]
        if curr:
            res = str(eval(curr_last))
            if res[-1]== "0" and res[-2]==".":
                res = res[:-2]
            curr = " = " +res
            final_text = previous_text + curr
            self.text_box.text= final_text

    #Method write to enter the button-text into the textbox/screen
    def write(self, instance):
        current= self.text_box.text
        button_text= instance.text
        if button_text=="Clear":
              self.text_box.text = ""
        else:
            if current and (current[-1] in self.operations and button_text in self.operations):
                return
            elif "\n" in current and (button_text in self.operations and current[-1] =="\n"):
                return
            elif current=="" and instance.text in self.operations:
                return
            else:
                new_text= current + button_text
                self.text_box.text= new_text


if __name__== "__main__":
    app= CalculatorApp()
    app.run()
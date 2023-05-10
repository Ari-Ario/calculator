import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operations = ["+", "-", "*", "/"]
        self.last_button= None
        main_layout = BoxLayout(orientation="vertical",  pos_hint={"center_x":0.5, "center_y":0.5})
        self.solution= TextInput(readonly= True, font_size=40, multiline=False)
        main_layout.add_widget(self.solution)
        #the numbers and sign on the layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "Clear", "+"],
            ]
        #loop over the numbers and signs to creat buttons
        for row in buttons:
            y_layout= BoxLayout()
            for sign in row:
                butt= Button(text=sign, pos_hint= {"center_x":0.5, "center_y":0.5})
                butt.bind(on_press= self.butt_press)
                y_layout.add_widget(butt)
            main_layout.add_widget(y_layout)
        equal= Button(text="=", pos_hint= {"center_x":0.5, "center_y":0.5})
        equal.bind(on_press= self.publish_solution)
        main_layout.add_widget(equal)

        return main_layout
    
    #Method to regulate the button-press
    def butt_press(self, instance):
        current= self.solution.text
        button_text= instance.text
        if button_text=="Clear":
              self.solution.text = ""
        else:
              if current and (current[-1] in self.operations and instance.text in self.operations):
                    return
              elif current=="" and instance.text in self.operations:
                    return
              else:
                    new_text= current + button_text
                    self.solution.text= new_text

    #Method to pulish the results on the text-box at the top
    def publish_solution(self, instance):
        text= self.solution.text
        if text[-1] in self.operations:
             return
        if text:
              res = str(eval(text))
              self.solution.text = res
    
if __name__== "__main__":
    app= CalculatorApp()
    app.run()

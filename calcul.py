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
        self.solution= TextInput(readonly= True, font_size=40)
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
        butt_text = instance.text
        pre_text = self.solution.text
        print(butt_text, pre_text)
        #clear the text-box
        if butt_text== "Clear":
            self.solution.text= ""

        #Not allowing tow times a sign and not allowing a sing at the beggining
        else:
            if pre_text and (pre_text[-1] in self.operations and butt_text in self.operations):
                #Not allowing two operation-signs after each other
                return
            elif (pre_text == ""  and butt_text in self.operations):
                #not allowing the first option to be an operation sign
                return
            else:
                text= pre_text + butt_text
                self.solution = text

    #Method to pulish the results on the text-box at the top
    def publish_solution(self, instance):
        equal_sign = instance
        #checks if text-box is empty or if last char is an operation-sign
        if self.solution == "" and self.solution[-1] in self.operations:
            return
        
        else:
            solve = str(eval(self.solution))
            self.solution = solve
    
if __name__== "__main__":
    app= CalculatorApp()
    app.run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
 
class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False)
        main_layout.add_widget(self.solution)
        self.solution2 = TextInput(multiline=False)
        main_layout.add_widget(self.solution2)
        equals_button = Button(text="сложить")
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        self.label = Label()
        main_layout.add_widget(self.label)
        return main_layout
 
    def on_solution(self, instance):
        self.label.text = str(float(self.solution.text)+float(self.solution2.text))
 
if __name__ == "__main__":
    app = MainApp()
    app.run()


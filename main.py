from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


Window.size = (360, 480)




class CalcApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text) == "x":
            self.formula += "*"
        elif str(instance.text) == "AC":
            self.formula = "0"
        else:
            self.formula += instance.text

        self.update_label()

    def result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def build(self):
        self.formula="0"
        bl = BoxLayout(orientation='vertical', padding=5)
        gl = GridLayout(cols=4, spacing=1, size_hint=(1, .6))

        self.lbl = Label(text="0", font_size=60, halign="right", valign="center", size_hint=(1, .25), text_size=(355, 480*0.25))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="1", on_press = self.add_number))
        gl.add_widget(Button(text="2", on_press = self.add_number))
        gl.add_widget(Button(text="3", on_press = self.add_number))
        gl.add_widget(Button(text="+", on_press = self.add_operation))

        gl.add_widget(Button(text="4", on_press = self.add_number))
        gl.add_widget(Button(text="5", on_press = self.add_number))
        gl.add_widget(Button(text="6", on_press = self.add_number))
        gl.add_widget(Button(text="-", on_press = self.add_operation))

        gl.add_widget(Button(text="7", on_press = self.add_number))
        gl.add_widget(Button(text="8", on_press = self.add_number))
        gl.add_widget(Button(text="9", on_press = self.add_number))
        gl.add_widget(Button(text="x", on_press = self.add_operation))

        gl.add_widget(Button(text="0", on_press = self.add_number))
        gl.add_widget(Button(text=".", on_press = self.add_number))
        gl.add_widget(Button(text="AC", on_press = self.add_operation))
        gl.add_widget(Button(text="/", on_press = self.add_operation))

        bl.add_widget(gl)

        al2 = AnchorLayout(size_hint=(1, .15))
        al2.add_widget(Button(text="=", on_press = self.result))

        bl.add_widget(al2)

        return bl


if __name__ == "__main__":
    CalcApp().run()
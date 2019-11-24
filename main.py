from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Preparer(Screen):
    pass

# class OperationScreen():
#     def __init__(self):
#         self.ingnition = ingnition

#     def changeIgnition(self):
#         return !self.ingnition

class MyApp(App): 
    
    def build(self):
        return Manager()

if __name__ == "__main__":
    MyApp().run()
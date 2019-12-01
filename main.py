from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from kivy.modules.console import Console, ConsoleAddon
from kivy.core.window import Window
from kivy.garden.graph import Graph
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from random import randint
import os
import serial
import time
import csv


Window.size = (910, 670)


class Manager(ScreenManager):
    pass

class Menu(Screen):
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmation_exit)

    def confirmation_exit(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical', padding=23, spacing=0)
        buttons = BoxLayout(padding=10, spacing=10)

        pop = Popup(title='Deseja mesmo sair?', content=box, size_hint=(None, None), size=(300,180))

        yes = Button(text='Sim', on_release=App.get_running_app().stop, size_hint_x=None, width=100, size_hint_y=None, height=30)
        no = Button(text='Não', on_release=pop.dismiss, size_hint_x=None, width=100, size_hint_y=None, height=30)

        buttons.add_widget(yes)
        buttons.add_widget(no)

        box.add_widget(buttons)

        pop.open()
        return True


class Preparer(Screen):

    def set_value_weight(self):
        try:
            global value_weight
            value_weight = int(self.ids.value_weight.text)
            print(value_weight)
            return value_weight
        except:
            box = BoxLayout(orientation='vertical', padding=23, spacing=0)
            buttons = BoxLayout(padding=10, spacing=10)

            pop = Popup(title='Valor não adequado', content=box, size_hint=(None, None), size=(300,180))

            ok = Button(text='Ok', on_release=pop.dismiss, size_hint_x=None, width=200, size_hint_y=None, height=30)

            buttons.add_widget(ok)

            box.add_widget(buttons)

            pop.open()

global test
test = []

class PlotGraphs(BoxLayout):
    def __init__(self, **kwargs):
        super(PlotGraphs, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 1)

    def stop(self):
        Clock.unschedule(self.get_value)

    def ignit(self):
        pass

    def get_value(self, dt):

        tests = 0
        for tests in test:
            tests += randint(0,1)
        test.append(tests)

        print(test[-1])
        print(value_weight)
        if(test[-1] >= value_weight):
            box = BoxLayout(orientation='vertical', padding=23, spacing=0)
            buttons = BoxLayout(padding=10, spacing=10)

            pop = Popup(title='Abastecimento finalizado', content=box, size_hint=(None, None), size=(300,180))

            ok = Button(text='Ok', on_release=pop.dismiss, size_hint_x=None, width=200, size_hint_y=None, height=30)

            buttons.add_widget(ok)

            box.add_widget(buttons)

            pop.open()
            self.stop()

        self.plot.points = [(i, j) for i, j in enumerate(test)]
        print(self.plot.points)



class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class PanelTable(TabbedPanel):
    pass

class Dashboard(Screen):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w', newline='') as f:
            fieldnames = ['column 1', 'column 3', 'column 2']
            thewriter = csv.DictWriter(f, fieldnames=fieldnames)

            thewriter.writeheader()


class VegaApp(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    # try:
    #     ser = serial.Serial('/dev/ttyACM0')
    # except:
    #     print ("Failed to connect")    
    #     exit()

    VegaApp().run()

    # ser.close()
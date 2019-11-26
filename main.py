from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from kivy.modules.console import Console, ConsoleAddon
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.popup import Popup
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
import numpy as np


Window.size = (910, 670)


class Manager(ScreenManager):
    pass

class Menu(Screen):
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmation_exit)

    def confirmation_exit(self, *args, **kwargs):
        print('CHAMOU')
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
    pass

class PlotGraphs(BoxLayout):
    def __init__(self, **kwargs):
        super(PlotGraphs, self).__init__()
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    # ysample = random.sample(range(-50, 50), 100)
    
    # xdata = []
    # ydata = []
    
    # axes = plt.gca()
    # axes.set_xlim(0, 100)
    # axes.set_ylim(-50, +50)
    # # line, = axes.plot(xdata, ydata, 'r-')
    
    # for i in range(100):
    #     xdata.append(i)
    #     ydata.append(ysample[i])
    #     line.set_xdata(xdata)
    #     line.set_ydata(ydata)
    #     plt.pause(1e-17)
    #     plt.plot()
    #     time.sleep(0.1)
    plt.xlabel('Tempo')
    plt.ylabel('Volume')
    plt.plot([0,0,2,8])


class PanelTable(TabbedPanel):
    pass

class Dashboard(Screen):
    pass

class VegaApp(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    VegaApp().run()
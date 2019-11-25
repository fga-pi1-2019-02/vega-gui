from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from kivy.modules.console import Console, ConsoleAddon
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.clock import Clock
import matplotlib
import matplotlib.pyplot as plt
from random import randint


Window.size = (910, 670)



class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Preparer(Screen):
    pass

class PlotGraphs(BoxLayout):
    def __init__(self, **kwargs):
        super(PlotGraphs, self).__init__()
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    # Clock.schedule_interval(self.get_value, 0.001)
    plt.ylabel('Volume')
    plt.xlabel('Tempo')
    # plt.plot([randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9)])
    plt.plot([0, 0, 2, 8])
    # self.i = 0
    # self.j = 0

    # def update(self):
    #     plt.plot([self.i, self.j])
    #     self.i += 1
    #     j += 1

    # Clock.schedule_interval(update(i, j), 1)



# class PanelTable(TabbedPanel):
#     pass

class Dashboard(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(Dashboard, self).__init__()
    #     self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    # def start(self):
    #     self.ids.graph.add_plot(self.plot)
    #     Clock.schedule_interval(self.get_value, 0.001)

    # def get_value(self):
    #     self.plot.point = randint(0, 9)

class VegaApp(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    VegaApp().run()
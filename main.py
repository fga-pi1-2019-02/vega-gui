from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.garden.graph import MeshLinePlot
from kivy.modules.console import Console, ConsoleAddon


class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Preparer(Screen):
    pass

class PanelTable(TabbedPanel):
    pass
    # def __init__(self, **kwargs):
    #     super(PanelTable, self).__init__()
    #     self.plot = MeshLinePlot(color=[1, 0, 10, 1])

class Dashboard(Screen):
    pass

class VegaApp(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    VegaApp().run()
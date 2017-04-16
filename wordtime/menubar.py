import rumps, time, threading
import wordTime

class MenuBar(rumps.App):
    def __init__(self):
        super(MenuBar, self).__init__("Word Time", "The time in words")
        refresh(self)

def refresh(self):
    threading.Timer(10, refresh, [self, ]).start()
    self.title = wordTime.fuzzyTime()

def main():
    MenuBar().run()

from os.path import dirname
from os.path import join
from os.path import realpath

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from plyer import notification
from plyer.utils import platform
from plyer.compat import PY2

import cherrypy
from multiprocessing import Process
import time

class NotificationDemo(BoxLayout):

    def do_notify(self, mode='normal'):
        title = self.ids.notification_title.text
        message = self.ids.notification_text.text
        ticker = self.ids.ticker_text.text
        if PY2:
            title = title.decode('utf8')
            message = message.decode('utf8')
        kwargs = {'title': title, 'message': message, 'ticker': ticker}

        if mode == 'fancy':
            kwargs['app_name'] = "Plyer Notification Example"
            if platform == "win":
                kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'plyer-icon.ico')
                kwargs['timeout'] = 4
            else:
                kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'plyer-icon.png')
        notification.notify(**kwargs)

from cherrypy.process.plugins import Daemonizer
class NotificationDemoApp(App):
    def build(self):
        #cherrypy.quickstart(HelloWorld())
        #d = Daemonizer(cherrypy.engine)
        #d.subscribe()
        return NotificationDemo()

    def on_pause(self):
        return True


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        notification.notify("abc", "abc")
        return "Hello World!"

def webserver():
    cherrypy.quickstart(HelloWorld())
    time.sleep(3)

def gui():
    NotificationDemoApp().run()
    time.sleep(3)


if __name__ == '__main__':
    #cherrypy.quickstart(HelloWorld())
    #a = Process(target=webserver, name='webserver')
    #b = Process(target=gui, name='gui')
    #a.start()
    #b.start()
    gui()




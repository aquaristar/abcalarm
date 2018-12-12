import cherrypy
from plyer import notification


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        notification.notify("abc", "abc")
        return "Hello World!"


cherrypy.quickstart(HelloWorld())

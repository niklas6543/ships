#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import os
from tornado import template, ioloop, web, httpserver

class WebManager:
    def __init__(self):
        self.loader = loader = template.Loader('./templates')
        self.templates = {
            'default': 'default.html',
            'home': 'home.html'
        }

class MainHandler(web.RequestHandler):
    def get(self):
        #loader = template.Loader('./templates')
        #self.write(loader.load('home.html').generate(myvalue='hallo welt',))
        self.render('home.html', myvalue="Hello, world!")


if __name__ == "__main__":
    app = web.Application( handlers=[
        (r'/', MainHandler)],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8888)
    ioloop.IOLoop.instance().start()
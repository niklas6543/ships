#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5


from tornado import template, ioloop, web

class WebManager:
    def __init__(self):
        self.loader = loader = template.Loader('./templates')
        self.templates = {
            'default': 'default.html',
            'home': 'home.html'
        }

class MainHandler(web.RequestHandler):
    def get(self):
        loader = template.Loader('./templates')
        self.write(loader.load('home.html').generate(myvalue='hallo welt'))


if __name__ == "__main__":
    application = web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    ioloop.IOLoop.current().start()

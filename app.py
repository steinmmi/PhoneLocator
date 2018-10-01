import tornado.ioloop
import tornado.web

longitude = 0
latitude = 0

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        if(len(self.request.arguments) == 2):
            global longitude
            global latitude
            longitude = self.get_arguments('lo')[0]
            latitude = self.get_arguments('la')[0]
        else:
            self.render("index.html",longitude=longitude,latitude=latitude)

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
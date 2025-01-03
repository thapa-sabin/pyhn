import tornado.web
import tornado.ioloop # Thread that is continuously waiting for result
import json

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        f = open("list.txt", "r")
        fruits = f.read().splitlines()
        f.close()
        self.write(json.dumps(fruits))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/list", listRequestHandler)
    ]) # Array of tuples of endpoints that will request handlers

    port = 8888
    app.listen(port)
    print(f"Application is ready and listening on port {port}.")

    tornado.ioloop.IOLoop.current().start()
    # The loop in the Upper block of code will keep on executing as long as the application is running

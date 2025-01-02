import tornado.web
import tornado.ioloop # Thread that is continuously waiting for result

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World! This is a Python code executed from the backend.")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html") # The render method should be used to "render" a file to show the client

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseID):
        self.write(f"Welcome {studentName}, the course you are viewing is {courseID}")

if __name__ == "__main__": # This code should execute only once
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", listRequestHandler),
        (r"/isEven", queryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler) # Hardcoded requirement for a-z upto infinity and 0-9 upto infinity
    ]) # Array of tuples of endpoints that will request handlers

    port = 8888
    app.listen(port)
    print(f"Application is ready and listening on port {port}.")

    tornado.ioloop.IOLoop.current().start()
    # The loop in the Upper block of code will keep on executing as long as the application is running

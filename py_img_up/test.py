import tornado.web
import tornado.ioloop
import json

class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))
    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))
    
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", mainRequestHandler),
        (r"/list", listRequestHandler)
    ])

    app.listen(8882)
    print(f"Listening on port 8882.") 
    app.listen(8883)
    print(f"Listening on port 8883.") 
    app.listen(8884)
    print(f"Listening on port 8884.") 
    tornado.ioloop.IOLoop.instance().start()
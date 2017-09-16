#!/usr/bin/python2
import tornado.web
import tornado.websocket
import tornado.ioloop

from tornado.options import define, options, parse_command_line
define("port", default=8887, help="run on the given port", type=int) 

chatTexto = "Chat Server Prj BDD"
connections = set()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("chat.html")
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		global connections
		connections.add(self)
		self.write_message(chatTexto)
	
	def on_message(self, message):
		global chatTexto
		global connections
		chatTexto += "<br>" 
		chatTexto += message
		print chatTexto
		for con in connections:
			con.write_message(chatTexto)
			
	def on_close(self):
		global connections
		connections.remove(self)
		
app = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/websocket", WebSocketHandler),
])
 
if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

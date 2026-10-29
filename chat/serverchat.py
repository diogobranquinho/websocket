#Servidor de chat com WebSocket
import json
import tornado.escape
import tornado.web
import tornado.websocket
import tornado.ioloop

from tornado.options import define, options, parse_command_line
# Porta que o Servidor vai escutar
define("port", default=8887, help="run on the given port", type=int)

# Mensagens ja enviadas, para quem entrar no chat depois
historico = []
# Navegadores conectados
connections = set()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("chat.html")

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        connections.add(self)
        # Envia as mensagens anteriores para quem acabou de entrar
        for msg in historico:
            self.write_message(msg)

    def on_message(self, message):
        # O navegador envia [nome, mensagem, hora] no formato JSON
        userName, mensagem, hora = json.loads(message)

        # xhtml_escape impede que HTML ou script digitado por um usuario
        # seja executado no navegador dos outros
        msg = "<div class='msgBody'>"
        msg += "<p class='username'>" + tornado.escape.xhtml_escape(userName) + " diz: </p>"
        msg += "<p class='message'>" + tornado.escape.xhtml_escape(mensagem)
        msg += "<span class='time'>" + tornado.escape.xhtml_escape(hora) + "</span>"
        msg += "</p>"
        msg += "</div>"
        print(userName, "diz:", mensagem)

        historico.append(msg)
        # Envia apenas a nova mensagem para todos os navegadores conectados
        for con in connections:
            con.write_message(msg)

    def on_close(self):
        connections.remove(self)

app = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/websocket", WebSocketHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

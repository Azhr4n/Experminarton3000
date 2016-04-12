from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

def callMagic():
	print 'called !'

clients = []
class SimpleServer(WebSocket):

	def handleMessage(self):

		if self.data == '/Magic':
			callMagic()

		for client in clients:
			if client != self:
				client.sendMessage(self.address[0] + u' - ' + self.data)

	def handleConnected(self):
		for client in clients:
			client.sendMessage(self.address[0] + u' - connected.')
		clients.append(self)
		print self.address, 'connected'

	def handleClose(self):
		print self.address, 'closed'


server = SimpleWebSocketServer('', 5000, SimpleServer)
server.serveforever()
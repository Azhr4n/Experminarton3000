from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleServer(WebSocket):

	def handleMessage(self):
		# echo message back to client
		self.sendMessage(self.data)

	def handleConnected(self):
		for client in clients:
			client.sendMessage(self.address[0] + u' - connected.')
		clients.append(self)
		print self.address, 'connected'

	def handleClose(self):
		print self.address, 'closed'

server = SimpleWebSocketServer('', 5000, SimpleServer)
server.serveforever()
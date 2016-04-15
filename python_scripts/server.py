from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json

def getData():
	return json.dumps({
	"val1": {
		"date": "156322",
		"temp": "37"
	},
	"val2": {
		"date": "156390",
		"temp": "37.6"
	},
	"val3": {
		"date": "157110",
		"temp": "36.2"
	}
})

clients = []
class SimpleChat(WebSocket):

	def handleMessage(self):
		if self.data == '/getData':
			self.sendMessage(u'' + getData())

	def handleConnected(self):
		clients.append(self)

	def handleClose(self):
		clients.remove(self)

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
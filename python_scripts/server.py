from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import base64, json

def getTemp():
	return json.dumps({
		"type_of_data": "temp",
		"data": [{
			"date": "156322",
			"temp": "37"
		}, {
			"date": "156390",
			"temp": "37.6"
		}, {
			"date": "157110",
			"temp": "36.2"
		}]
	})

def getImage():
	f = open('sample/vortex.jpg', 'r')
	image = base64.b64encode(f.read())
	f.close()
	return json.dumps({
		"type_of_data": "image",
		"data": image
		})

clients = []
class SimpleChat(WebSocket):

	def handleMessage(self):
		if self.data == '/getTemp':
			self.sendMessage(u'' + getTemp())
		elif self.data == '/getImage':
			self.sendMessage(u'' + getImage())

	def handleConnected(self):
		clients.append(self)

	def handleClose(self):
		clients.remove(self)

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
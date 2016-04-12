from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import RPi.GPIO as GPIO

def LEDOn():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(8, GPIO.HIGH)

def LEDOff():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(8, GPIO.LOW)

clients = []
class SimpleServer(WebSocket):

	def handleMessage(self):

		if self.data == '/LedOn':
			LEDOn()
		elif self.data == '/LedOff':
			LEDOff()

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
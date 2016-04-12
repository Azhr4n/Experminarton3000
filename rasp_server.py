from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import RPi.GPIO as GPIO

clients = []
class RaspServer(WebSocket):

	def handleMessage(self):
		if self.data == '/LedOn':
			LEDOn()
		elif self.data == '/LedOff':
			LEDOff()
		else:
			sendToOthers(self)

	def handleConnected(self):
		for client in clients:
			client.sendMessage(self.address[0] + u' - connected.')
		clients.append(self)
		print self.address, 'connected'

	def handleClose(self):
		print self.address, 'closed'

	def sendToOthers(self):
		for client in clients:
			if client != self:
				client.sendMessage(self.address[0] + u' - ' + self.data)

def rasp_init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

def LEDOn():
	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, GPIO.HIGH)

def LEDOff():
	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, GPIO.LOW)

server = SimpleWebSocketServer('', 5000, RaspServer)
server.serveforever()
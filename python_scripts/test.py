import base64, json

f = open('sample/vortex.jpg', 'r')
image = base64.b64encode(f.read())
f.close()
json = json.dumps({
	"type_of_data": "image",
	"data": image
	})

print json

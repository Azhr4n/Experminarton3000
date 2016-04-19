
var addr = 'localhost';
var port = '8000';

var socket = new WebSocket('ws://' + addr + ':' + port);

socket.onopen = function(event) {onOpenEvent(event)};
socket.onmessage = function(event) {onMessageEvent(event)};
socket.onclose = function(event) {onCloseEvent(event)};
socket.onerror = function(event) {onErrorEvent(event)};

function onOpenEvent(event) {
	updateData();
	setInterval(updateData, 15000);
};

function onMessageEvent(event) {
	if (isJsonString(event.data)) {
		var node;
		var obj = JSON.parse(event.data);

		if (('type_of_data' && 'data') in obj) {
			data = obj.data;
			if (obj.type_of_data == 'temp') {
				node = document.getElementById('list_temp');
				clearNode(node);
				node.appendChild(createListFromJson(data));
			}
			else if (obj.type_of_data == 'image') {
				node = document.getElementById('rasp_image');
				clearNode(node);
				node.src = 'data:image/jpg;base64,' + data;
			}
		}
	}
};

function onCloseEvent(event) {
	clearInterval();
};

function onErrorEvent(event) {
	console.log('Error : ' + event.data);
	socket.close();
};

function updateData() {
	console.log('Refresh !');
	sendText('/getTemp');
	sendText('/getImage');
};

function sendText(str) {
	socket.send(str);
};

function clearNode(node) {
	while (node.firstChild) {
		node.removeChild(node.firstChild);
	}
};

function isJsonString(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
};

function createListFromJson(json_data) {
	var i, inc, item;
	var list = document.createElement('ul'); 

	for (data in json_data) {
		inc = 0;
		item = document.createElement('li');
		for (value in json_data[data]) {
			if (inc == 0) {
				item.appendChild(document.createTextNode(value + ':' + json_data[data][value]));
			}
			else {
				item.appendChild(document.createTextNode(', ' + value + ':' + json_data[data][value]));
			}
			inc++;
		}
		list.appendChild(item);
	}
	return list;
};

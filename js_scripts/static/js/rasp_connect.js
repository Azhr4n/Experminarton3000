var socket = new WebSocket('ws://localhost:8000');

socket.onopen = function(event) {onOpenEvent(event)};
socket.onmessage = function(event) {onMessageEvent(event)};
socket.onclose = function(event) {onCloseEvent(event)};
socket.onerror = function(event) {onErrorEvent(event)};

function onOpenEvent(event) {
	socket.send('/getData');
};

function onMessageEvent(event) {
	document.getElementById('print_data').appendChild(createListValue(event.data));
};

function onCloseEvent(event) {

};

function onErrorEvent(event) {
	console.log('Error : ' + event.data);
	socket.close();
};

function createListValue(json_data) {
	values = json_data.split('},');

	for (var i = 0; i < values.length; i++) {
		values[i] = values[i].replace(/[{"}]/g, '');
		values[i] = values[i].replace(/,/g, ' ');
	}

	var list = document.createElement('ul');

	for (i = 0; i < values.length; i++) {
		var item = document.createElement('li');

		item.appendChild(document.createTextNode(values[i]));
		list.appendChild(item);
	}
	return list;
};
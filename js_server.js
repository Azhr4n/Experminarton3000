var WebSocket = require('ws');
var express = require('express');

var app = express();

var socket = null;

app.get('/', function(req, res) {
	res.render('Index.ejs', {});
});

app.get('/Bonjour', function(req, res) {
	if (socket == null) {
		socket = new WebSocket('ws://localhost:8000');
	}
	res.end();
});

app.listen(8080);

/*
var socket = new WebSocket('ws://localhost:8000');
socket.onopen = function(event) {onOpenEvent(event)};
socket.onmessage = function(event) {onMessageEvent(event)};
socket.onclose = function(event) {onCloseEvent(event)};
socket.onerror = function(event) {onErrorEvent(event)};

function onOpenEvent(event) {

};

function onMessageEvent(event) {

};

function onCloseEvent(event) {

};

function onErrorEvent(event) {

};
*/
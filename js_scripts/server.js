

var express = require('express');
var app = express();

app.use(express.static('static'));

app.get('/', function(req, res) {
	res.render('index.twig');
});

app.get('/get_data', function(req, res) {
	res.render('get_data.twig');
});

app.listen(8080);

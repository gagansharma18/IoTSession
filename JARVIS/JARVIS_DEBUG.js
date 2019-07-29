const path = require("path");
const port = process.env.PORT || 8080;
const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer( app );
server.listen( port, () => {
    console.log( 'JARVIS server listening on port ' + server.address().port );
} );
var io = require('socket.io')(server); //require socket.io module and pass the http object (server)
io.sockets.on('connection', function (socket) {// Web Socket Connection
    socket.on('command', function(data) { //get payload from client
        console.log(data);
    });
});
app.use(express.static(path.join(__dirname, "./public")));
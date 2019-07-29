const pins = [5,6,13,19,26,16,20,21];

const fs = require('fs');
const path = require("path");
const port = process.env.PORT || 8080;
const express = require('express');
const app = express();

/* HTTPS */
const https = require('https');
const options = {
    key: fs.readFileSync(path.join(__dirname,'localhostkeys/localhost.key'), 'utf8' ),
    cert: fs.readFileSync(path.join(__dirname,'localhostkeys/localhost.cert'), 'utf8' ),
    requestCert: false,
    rejectUnauthorized: false
};
const server = https.createServer( options, app );
/* HTTPS ENDS*/

/* HTTP */
//const http = require('http');
//const server = http.createServer( app );
/* HTTP END */

server.listen( port, () => {
    console.log( 'JARVIS server listening on port ' + server.address().port );
} );
var io = require('socket.io')(server); //require socket.io module and pass the http object (server)

var Gpio = require('pigpio').Gpio; //include pigpio to interact with the GPIO

var Relays = [];
pins.forEach((pin) => {
    Relays.push(new Gpio(pin, {mode: Gpio.OUTPUT}));
});
   
//RESET ALL DEVICES
Relays.forEach((relay) => {
    relay.digitalWrite(0); 
});

io.sockets.on('connection', function (socket) {// Web Socket Connection
    socket.on('command', function(data) { //get payload from client
        console.log(data);
        Relays[data.device].digitalWrite(1);
    });
});

process.on('SIGINT', function () { //on ctrl+c
    //RESET ALL DEVICES
    Relays.forEach((relay) => {
        relay.digitalWrite(0); 
    });
    process.exit(); //exit completely
});
app.use(express.static(path.join(__dirname, "./public")));
var config = {
    "devices":["light","tv","ac","fan","lamp","heater","room light","kitchen light"],
    "onCommands":["turn on *","turn on the *","* on"],
    "offCommands":["turn off *","turn off the *","* off"]
}
var socket = io();
var JARVIS = new Artyom();
window.onload = function(){
    JARVIS.initialize({
        // Run "forever"
        continuous: true,
        lang:"en-GB",
        debug:true,
        mode:"normal",
        soundex:false,
        listen: true,
        //name:"jarvis",
        //executionKeyword:"and do it now",
    }).then(res=>{
            console.log("JARVIS A.I. LOADED");
            window.loadJarvis = function loadJarvis() {
                    JARVIS.say("Hi I am JARVIS.");
                    JARVIS.say("What can I do for you?");
            }
    });
    
    JARVIS.addCommands({
        //The smart property of the command needs to be true
        smart:true,
        indexes: config.offCommands.concat(config.onCommands),
        action: function(i, wildcard){
            var payload={
                "state":undefined,
                "device":undefined
            }
            if(config.devices.indexOf(wildcard.trim()) != -1){
                payload.device = config.devices.indexOf(wildcard.trim());
                payload.state = (i >= 0 && i < config.onCommands.length) ? 0 : 1 ;
                socket.emit("command", payload); //send payload to JARVIS SERVER via WebSocket
                JARVIS.say("Done!");
            }else{
                JARVIS.say("I don't know what is " + wildcard);
            }
        }
    });

    JARVIS.redirectRecognizedTextOutput((recognized,isFinal) => {
        if(isFinal){
            document.getElementById("recognise").innerHTML = recognized;
            //console.log("REC",recognized);
        }
    });
};
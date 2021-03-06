var socket = io();
var JARVIS = new Artyom();
window.onload = function(){
    JARVIS.initialize({
        // Run "forever"
        continuous: true,
        lang:"en-GB",
        debug:config.debug,
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
                if(config.debug){
                    console.log("payload",payload,"Device",config.devices[payload.device]);
                }
                socket.emit("command", payload); //send payload to JARVIS SERVER via WebSocket

                let device_switch = $(`ons-switch:eq( ${payload.device} )`).get(0);
                let device_state = (payload.state)?"on":"off";
                if(device_switch.checked != payload.state){ //Checking if device is already on
                    device_switch.checked = payload.state;
                    JARVIS.say("Done!");
                }else{
                    JARVIS.say(wildcard + " is alrady " +device_state);
                }
                
            }else{
                JARVIS.say("I don't know what is " + wildcard);
            }
        }
    });

    JARVIS.redirectRecognizedTextOutput((recognized,isFinal) => {
        document.getElementById("recognise").innerHTML = recognized;
        // if(isFinal){
        //     document.getElementById("recognise").innerHTML = recognized;
        // }
    });
};
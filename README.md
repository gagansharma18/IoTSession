# IoTSession


## PINOUT
https://pinout.xyz/pinout/pin12_gpio18

## GPIO

gpio.py python file is used for control relay 8 channel with Raspberry Pi

pinList is array of GPIO order from 1 to 8
```
$ python gpio.py 1 on

$ python gpio.py 1 off

$ python gpio.py closeall

$ python gpio.py openall

$ python gpio.py get (to info all of channel turn on or off)
```

#  SENSOR

## RELAY
```
python relayTest.py
```

## SWITCH
```
pyhon switch.py
```

## PIR Passive IR SENSON (Motion sensor)
```
python priMotion.py
```

## Blynk mobile app

### Raspberry Pi
1. Connect your Raspberry Pi to the Internet and open it’s console.
2. Run this command (it updates your OS package repository to include the required packages):
```
 curl -sL "https://deb.nodesource.com/setup_6.x" | sudo -E bash -
 ```
3. Download and build Blynk JS library using npm:
    ```
    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install build-essential
    sudo apt-get install -g npm 
    sudo npm install -g onoff
    sudo npm install -g blynk-library
    ```
4. Run Blynk test script (put your auth token):
    ```
    blynk-client 715f8cafe95f4a91bae319d0376caa8c
    ```
5. You can write our own script based on examples

6. To enable Blynk auto restart for Pi, find /etc/rc.local file and add there:

 node full_path_to_your_script.js <Auth Token>


# JARVIS

Before start you have to create key and cert file for local https connection from the device you're running the server
```
cd IoTSession/JARVIS/localhostkeys
openssl genrsa -out localhost.key 2048
openssl req -new -x509 -key localhost.key -out localhost.cert -days 3650 -subj /CN=localhost
```
```
npm install
npm start
```

# NODE RED

1. Fix conflicts with audio playback

```
sudo nano /boot/config.txt
```
and add these lines

```
hdmi_force_hotplug = 1
hdmi_force_edid_audio = 1
```

2. Install node-red-dashboard

```
cd ~/.node-red
npm install node-red-dashboard
```
3. install the neopixel Node-RED node

```
curl -sS get.pimoroni.com/unicornhat | bash
```
```
node-red-stop
cd ~/.node-red
npm install node-red-node-pi-neopixel
node-red-start
```
# IoTSession

# gpio.py

this python file is used for control relay 8 channel with Raspberry Pi

pinList is array of GPIO order from 1 to 8

$ python3 gpio.py 1 on

$ python3 gpio.py 1 off

$ python3 gpio.py closeall

$ python3 gpio.py openall

$ python3 gpio.py get (to info all of channel turn on or off)


# Blynk mobile app

Raspberry Pi
1.Connect your Raspberry Pi to the Internet and open it’s console.
2.Run this command (it updates your OS package repository to include the required packages):

 curl -sL "https://deb.nodesource.com/setup_6.x" | sudo -E bash -
3.Download and build Blynk JS library using npm:

 sudo apt-get update && sudo apt-get upgrade
 sudo apt-get install build-essential
 sudo apt-get install -g npm 
 sudo npm install -g onoff
 sudo npm install -g blynk-library
4.Run Blynk test script (put your auth token):

 blynk-client 715f8cafe95f4a91bae319d0376caa8c
5.You can write our own script based on examples

6.To enable Blynk auto restart for Pi, find /etc/rc.local file and add there:

 node full_path_to_your_script.js <Auth Token>


# JARVIS
```
openssl genrsa -out localhost.key 2048
openssl req -new -x509 -key localhost.key -out localhost.cert -days 3650 -subj /CN=localhost
```
```
npm install
npm start
```

#NODE RED
```
node-red-start
node-red-stop
```
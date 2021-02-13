 #! /bin/sh
if  [ -z "$1" ]
then
   python feeder.py
else
   python feeder.py $1
fi

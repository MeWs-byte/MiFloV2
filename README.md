# MiFloV2
a KISS implementation of the MiFlo Smart Clock

### Software
#### Calendar

grab quickstart.py from here
https://developers.google.com/calendar/quickstart/python

current setup 

##### On Desktop

- get credentials 

https://developers.google.com/workspace/guides/create-project

- download .json creds as described and rename credentials.json

- run quickstart.py 

- copy token.json to project folder on Pi 

##### On Pi

- sudo pip3 install -r requirements.txt
- sudo python3 threadMachine.py


### Hardware
current setup and connections:

I used BCM pin numbering instead of BOARD pins


Peripherals -> Rasberry Pi

LED matrix -> Pi

- 5v -> 5v
- GND -> GND
- DIN -> 18

Push button -> Pi

- Leg1 -> - 3.3V
- Leg2 -> - 15
       <br />_____-> - 10k resistor -> GND







----
notes : 


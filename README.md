# MiFloV2
a KISS implementation of the MiFlo Smart Clock

## Setup instructions

### Fresh raspberry pi:

#### Setup raspberry pi boot volume

* Get Lite OS from https://www.raspberrypi.org/software/operating-systems/
* Flash on SD card
* On `/boot` volume on SD card:
* Touch an empty `ssh` file so SSH will be enabled on boot
* Create `wpa_supplicant.conf` with contents (update `SSID` and `PASSWORD`):

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=BE
network={
 ssid="SSID"
 psk="PASSWORD"
}
```

* Boot the raspberry pi, find the pi on the network, ssh to it
* `ssh pi@RASPPBERYIPADDRESS` and use the default `raspberry` password
* Change the default password with `passwd`

#### Essentials

* `sudo apt-get update`
* `sudo apt-get install git python3-pip libopenjp2-7-dev libtiff5`
* Set the correct timezone with `sudo raspi-config`

#### Git repo

Set up github access

* `ssh-keygen -t rsa -C "EMAIL@ADDRESS"`
* `cat /home/pi/.ssh/id_rsa.pub`
* Add this key to https://github.com/settings/keys

Clone the repo

* `git clone git@github.com:MeWs-byte/MiFloV2.git`
* `cd MiFloV2`
* `pip3 install -r requirements.txt`
* `pip3 uninstall board`
* Make sure `.local/bin` is in your path by reloading your profile, with `source ~/.profile`

### Google calendar access

#### Quickstart.py

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
       <br />leg2-> - 10k resistor -> GND

## Run


When running, go to `localhost:5000/timer` to set the timer, `/alarm` to set the alarm, `/events` for incoming events, `/home` to enter todos. Press the submit button or input 1 to go back to clockstate.

In alarm mode, press the pushbutton to return back to clockstate.

### Extras

Run `renderip.py` to render the ip


### Troubleshooting 

#### Google Api 

Token revoked error: go to https://console.cloud.google.com/ , click on the hamburger menu ( left) , choose Api & Services -> Credentials tab -> choose the client you were using and click on "reset secret". Download the JSON again and rename it credentials.json. 
When you run quickstart.py again (on your desktop) you should be able to receive a new token. Copy said token to the project folder on the Pi

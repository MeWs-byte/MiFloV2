# MiFloV2
a KISS implementation of the MiFlo Smart Clock

With the MiFlo parents can set alerts, alarms and visual timers in google calendar to plan tasks and create a dedicated point of attention.
For each completed task point are earned and random encouragements are displayed.

Build your own connected clock for kids with ADHD and ASD or anybody else for that matter.


[Hardware Components, Schematics, Lasercut SVG's ](/hardware)

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
* * `sudo apt-get upgrade`
* `sudo apt-get install git python3-pip libopenjp2-7-dev libtiff5`
* Set the correct timezone with `sudo raspi-config`
* Enable I2C with `sudo raspi-config` -> interface options -> enable i2C
#### Git repo

Set up github access

* `ssh-keygen -t rsa -C "EMAIL@ADDRESS"`
* `cat /home/pi/.ssh/id_rsa.pub`
* Add this key to https://github.com/settings/keys

Clone the repo

* `git clone git@github.com:MeWs-byte/MiFloV2.git`
* `cd MiFloV2`

Requirements
* `sudo pip3 install -r requirements.txt`
* `pip3 uninstall board`
* Make sure `.local/bin` is in your path by reloading your profile, with `source ~/.profile`
* if board error keeps persisting :`sudo pip3 install --force-reinstall adafruit-blinka`

### Google calendar access



##### On Desktop

- get credentials from google developer cloud, follow the tutorial below:

https://developers.google.com/workspace/guides/create-project

- download .json creds as described and rename credentials.json

- copy the scripts cal_setup.py and list_events.py to your local computer.  (they are in the calendarSetup folder)
    put the credentials.json in the same folder
    run list_events.py `sudo python3 list_events.py`
- if everything went right you should have received a file called token.pickle in the same folder

- copy token.pickle to project folder on Pi 

##### On Pi

- `sudo pip3 install -r requirements.txt`
- to test : `sudo python3 main.py` 





## External Soundcard 

https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/updating-alsa-config

### Extras

- Run `renderip.py` to render the ip
- If you have a dht sensor , use dht.py as a starting point 
- If you have a HC-SR04 ultrasonic sensor , use ultrasonic.py as a starting point (for example to use it to turn off the alarm)





### Troubleshooting 
disable wifi power save mode 

`sudo nano /etc/rc.local`


add this line before "exit 0"
`/sbin/iwconfig wlan0 power off`

#### Google Api 

Token revoked error: go to https://console.cloud.google.com/ , click on the hamburger menu ( left) , choose Api & Services -> Credentials tab -> choose the client you were using and click on "reset secret". Download the JSON again and rename it credentials.json. 
When you run quickstart.py again (on your desktop) you should be able to receive a new token. Copy said token to the project folder on the Pi

### systemd service
save configuration as 
`sudo nano /lib/systemd/system/miflo.service`

contents of file:
```
[Unit]
Description=MiFlo
After=network.target

[Service]
ExecStart=/usr/bin/python3 main.py
WorkingDirectory=/home/pi/MiFloV2
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```


`sudo chmod 777 /lib/systemd/system/miflo.service`
`sudo systemctl daemon-reload`
`sudo systemctl enable miflo.service`

Because everything starts up kinda slowly , here's another service that starts up 30 seconds faster:

sudo nano /etc/systemd/system/bootAnimation.service 
 

```[Unit]
Description=bootAnimation
Before=local-fs.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 booty.py
WorkingDirectory=/home/pi/MiFloV2
StandardOutput=inherit
StandardError=inherit

User=root

[Install]
WantedBy=multi-user.target
```


###User instructions:
Op http://<IP>:5000 kan je de webapp terugvinden. Deze is intussen quasi overbodig geworden en is gestripped van de features die er initieel aanwezig waren.
Wat wel leuk kan zijn is de naam van de user invoeren onder de tab "userinfo". Het is aan te raden om dit eerst te doen voor je events inplanned .

Om op je telefoon de google calendar app te gebruiken kan je best even deze testaccount toevoegen. 
Vanuit google app op android kan je geen nieuwe account toevoegen.
Op android moet je even naar de settings van je telefoon en onder ''accounts'' deze google account toevoegen. 
Daarna kan je in de calendar app wel de account selecteren. Let op dat events kunnen blenden met je huidige kalender. Dit kan voor verwarring zorgen dus het kan ook een aanrader te zijn om de filte rin te stellen zodat enkel de juiste kalender zichtbaar is in de app.


-google calendar heeft events, tasks en reminders. Kies de optie 'event' om een timer in te plannen. De starttijd en eindtijd bepalen de duur van de timer. 

-Geef de events altijd een titel, het zou kunnen dat er een error optreedt als je geen titel hebt ingevoerd. (work in progress) 

-Om een alarm in te plannen maak je een nieuw evenement aan met als titel 'alarm' (geen hoofletters) 

-Om een reminder in te plannen maak je een nieuw evenement aan met de titel van je reminder. onder "description" moet je "remind" ingeven. Dit zal een alert op de MifLo aanmaken zonder timer 

De arcade button licht op als er een actie vereist is. (er zou af en toe nog een kleine lag kunnen opzitten, wacht een secondje of 2 en de timer zal wel opstarten).
Op google calendar kan je zien aan de kleuren van de events of ze afgewerkt zijn of niet .

Blauw = onafgewerkt
Geel = processing in event queue of onderbroken voor de timer is beeindigd.
Groen = Timer volledig afgewerkt.


Als het licht van de leds te sterk is voor de kamer is het aan te raden om de SLEEP MODE in te schakelen . Hou de knop een tweetal seconden in en laat los. Na enkele seconden zou het scherm uit moeten gaan. Weer aanzetten gebeurd  op dezelfde wijze. 
Als het alarm in de ochtend geactiveerd word zal de SLEEP MODE automatisch uitgezet worden.


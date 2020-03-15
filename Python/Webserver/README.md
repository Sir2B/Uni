# Temperature-Webserver

## Dependencies

```batch
sudo apt install python3-pip librrd-dev libpython3-dev rrdtool
sudo pip3 install rrdtool Adafruit_DHT
```

## Setup

```batch
sudo raspi-config
```

- change hostname, password
- enable ssh, vnc, 1-wire

```batch
rrdtool create values.rrd --step 300 DS:temp0:GAUGE:600:-40:100 DS:temp1:GAUGE:600:-40:100 DS:temp2:GAUGE:600:-40:100 DS:humidity0:GAUGE:600:-1:101 RRA:AVERAGE:0.5:1:576 RRA:AVERAGE:0.5:12:336 RRA:AVERAGE:0.5:288:365 RRA:AVERAGE:0.5:8640:600
```

## Autostart

### Temperature in Cronjob

```batch
crontab -e
```

```text
  */10 * * * * sudo python3 /home/pi/temperature-webserver/gettemp.py >> /home/pi/gettemp.log 2>&1
```

### Webserver as a Service

- https://www.thomaschristlieb.de/ein-python-script-mit-systemd-als-daemon-systemd-tut-garnicht-weh/

```batch
chmod 777 temperature-webserver/temperature_webserver.py
sudo nano /etc/systemd/system/pyserver.service
```

```editor-config
[Unit]
Description=My Python Server
After=syslog.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/pi/temperature-webserver
ExecStart=/home/pi/temperature-webserver/temperature_webserver.py
SyslogIdentifier=pyserver
StandardOutput=syslog
StandardError=syslog
Restart=always
RestartSec=300

[Install]
WantedBy=multi-user.target
```

```batch
sudo systemctl enable pyserver
sudo systemctl start pyserver
journalctl -n 50
```


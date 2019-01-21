sudo apt install librrd-dev libpython3-dev rrdtool
sudo pip3 install rrdtool

sudo raspi-config
# change hostname, password
# enable ssh, vnc, 1-wire

rrdtool create values.rrd --step 300 DS:temp0:GAUGE:600:-40:100 DS:temp1:GAUGE:600:-40:100 DS:temp2:GAUGE:600:-40:100 DS:humidity0:GAUGE:600:-1:101 RRA:AVERAGE:0.5:1:576 RRA:AVERAGE:0.5:12:336 RRA:AVERAGE:0.5:288:365 RRA:AVERAGE:0.5:8640:600

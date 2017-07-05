#!/bin/bash

scrps_path=/root

info_web="= Web-server =
----------------------
$(service apache2 status | egrep -i 'active|tasks|memory')

"

info_cpu="= CPU =
----------------------
$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1" of 100 percents"}')

"

info_ram="= RAM =
----------------------
free: $(free -m | grep Mem | awk '{print $4}') MB of $(free -m | grep Mem | awk '{print $2}') MB total

"

info_space="= HDD =
----------------------
$(df -h --output=source,size,used,avail | grep dev)

"

text=$(printf "$info_web$info_cpu$info_ram$info_space")
printf '%s\n' "$text" > ${scrps_path}/status.txt

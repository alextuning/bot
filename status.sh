#!/bin/bash

scrps_path=/tmp

info_web="*Services*
----------------------
*Apache2:*
$(systemctl status apache2 | egrep -i 'active|tasks|memory' | awk '{print$1,$2,$9,$10}')
*Asterisk:*
$(systemctl status asterisk | egrep -i 'active|tasks|memory' | awk '{print$1,$2,$9,$10}')

"

info_cpu="*CPU*
----------------------
$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1" of 100 percents"}')

"

info_ram="*RAM*
----------------------
free: $(free -m | grep Mem | awk '{print $4}') MB of $(free -m | grep Mem | awk '{print $2}') MB total

"

info_space="*HDD*
----------------------
$(df -h --output=source,size,used,avail | grep dev)

"

text=$(printf "$info_web$info_cpu$info_ram$info_space")
printf '%s\n' "$text" > ${scrps_path}/status.txt

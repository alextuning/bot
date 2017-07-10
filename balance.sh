#!/bin/bash
scrps_path=/root
asterisk -rx 'dongle ussd dongle0 *105#'
sleep 3
balance="*Balance:*
----------------------
$(tail -n1 /var/log/asterisk/ussd)
"
text=$(printf "$balance")
printf '%s\n' "$text" > ${scrps_path}/balance.txt

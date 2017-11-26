#!/bin/bash
curl -d "username=$1&password=$2&action=login&view=console" -c cookies.txt  http://silitus.ru/zm/index.php > /dev/null 2>&1
curl -b cookies.txt -XPOST http://silitus.ru/zm/api/monitors/1.json -d "Monitor[Enabled]=0" > /dev/null 2>&1
curl -b cookies.txt -XPOST http://silitus.ru/zm/api/monitors/2.json -d "Monitor[Enabled]=0" > /dev/null 2>&1

#!/bin/bash
curl -d "username=$1&password=$2&action=login&view=console" -c cookies.txt  https://silitus.ru/zm/index.php > /dev/null 2>&1
curl -b cookies.txt -XPOST https://silitus.ru/zm/api/monitors/1.json -d "Monitor[Enabled]=1" > /dev/null 2>&1
curl -b cookies.txt -XPOST https://silitus.ru/zm/api/monitors/2.json -d "Monitor[Enabled]=1" > /dev/null 2>&1

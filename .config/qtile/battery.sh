#!/bin/bash

#################################################################
## ___  ____ _         _       _  ______ _      _   _          ##
## |  \/  (_) |       | |     (_) | ___ (_)    | | | |         ##
## | .  . |_| | _____ | | __ _ _  | |_/ /_  ___| |_| | ____ _  ##
## | |\/| | | |/ / _ \| |/ _` | | |  __/| |/ _ \ __| |/ / _` | ##
## | |  | | |   < (_) | | (_| | | | |   | |  __/ |_|   < (_| | ##
## \_|  |_/_|_|\_\___/|_|\__,_| | \_|   |_|\___|\__|_|\_\__,_| ##
##                           _/ |                              ##
##                          |__/                               ##
#################################################################

# Small battery management script to notify when battery is below 15 and 5%
# I made it because notifications send by Qtile has timeout and can be missed 
# It doesn't require any additional dependencies

NOT15=0
NOT5=0

function main () {
    let FULL=$(cat /sys/class/power_supply/BAT1/energy_full)
    let NOW=$(cat /sys/class/power_supply/BAT1/energy_now)
    let PART=$NOW*100/$FULL

    STATE=$(cat /sys/class/power_supply/BAT1/status)

    if [ $NOT15 -eq 1 ] && [ $STATE != "Discharging" ] ; then
            NOT15=0
            NOT5=0
    fi

    if [ $PART -lt 5 ] && [ $STATE = "Discharging" ] && [ $NOT5 -eq 0 ]; then
            notify-send -u critical "BATTERY IS ALMOST DEAD!" "Battery level below 5%, connect power supply"
            NOT5=1
            NOT15=1
    fi

    if [ $PART -lt 15 ] && [ $STATE = "Discharging" ] && [ $NOT15 -eq 0 ]; then
            notify-send -u critical "Low battery level!" "Battery level below 15%, connect power supply"
            NOT15=1
    fi

    sleep 5
    main
}
main
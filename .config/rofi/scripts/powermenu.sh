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

# Created by Mikolaj Pietka

declare -a managers=(
    "qtile"
)

declare -a options=(
    "Power off"
    "Suspend"
    "Lock"
    "Logout"
    "Reboot"
)

rofi="rofi -dmenu -i -l 5 -no-show-icons"

screenlock="slock"

choice=$(printf '%s\n' "${options[@]}" | $rofi -p "Powermenu")

case $choice in
    "Power off")
        shutdown now
    ;;
    "Suspend")
        $screenlock & systemctl suspend
    ;;
    "Lock")
        $screenlock
    ;;
    "Logout")
        for manager in ${managers[@]}
            do killall $manager
        done
    ;;
    "Reboot")
        reboot
    ;;
    *)
    exit 0
    ;;
esac

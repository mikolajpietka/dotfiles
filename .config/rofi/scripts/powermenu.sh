#!/usr/bin/bash

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
    "Shutdown"
    "Logout"
    "Reboot"
    "Quit"
)

rofi="rofi -dmenu -i -l 4 -no-show-icons"

choice=$(printf '%s\n' ${options[@]} | $rofi -p "Powermenu")

case $choice in
    "Shutdown")
        if [[ $(echo -e "Yes\nNo" | $rofi -p "Sure?") == "Yes" ]]
        then shutdown now
        else exit 0
        fi
    ;;
    "Logout")
        if [[ $(echo -e "Yes\nNo" | $rofi -p "Sure?") == "Yes" ]]
        then 
            for manager in ${managers[@]}
                do killall $manager
            done
        else exit 0
        fi
    ;;
    "Reboot")
        if [[ $(echo -e "Yes\nNo" | $rofi -p "Sure?") == "Yes" ]]
        then reboot
        else exit 0
        fi
    ;;
    "Quit")
        exit 0
    ;;
esac
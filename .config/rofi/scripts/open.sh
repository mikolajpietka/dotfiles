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

# Script to quickly open files and other options

DMENU="rofi -dmenu -i -p "
TERMINAL="alacritty"
CONFIGFILE="/home/mikolaj/.config/rofi/scripts/open.conf"

SECTION=$(grep "section:" "$CONFIGFILE" | awk -F : '{print $2}' | $DMENU)
if [ "$SECTION" ]; then
    OPTION=$(grep "$SECTION:" "$CONFIGFILE" | awk -F : '{print $2}' | $DMENU)

    if [ "$OPTION" ]; then
        LINE=$(grep "$SECTION:$OPTION:" "$CONFIGFILE")

        COMMAND=$(echo "$LINE" | awk -F : '{print $3}')

        CHTERM=$(echo "$LINE" | awk -F : '{print $4}')
        if [ "$CHTERM" = "term" ]; then
            $TERMINAL -e $COMMAND
        else
            bash -c "$COMMAND"
        fi

    fi
fi

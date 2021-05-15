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

DMENU="rofi -dmenu -i"

declare -a OPTIONS=(
    "Toggle WIFI"
    "List of known connections"
    "Connect to wifi"
)

declare -a CONOPT=(
    "Connect to"
    "Info"
    "Edit"
    "Delete"
)

declare -a EDIOPT=(
    "Name"
    "Autoconnect"
)

CONNECTION=$(nmcli -o | grep "connected to" | awk -F : '{print $2}' | sed 's/ connected to //')
WIFISTATUS=$(nmcli -g WIFI general)
if [ "$CONNECTION" ]; then
    STATUS="Connected to: $CONNECTION"
elif [ "$WIFISTATUS" == "disabled" ]; then
    STATUS="WIFI disabled"
else
    STATUS="Disconnected"
fi

CHOICE=$(printf "%s\n" "${OPTIONS[@]}" | $DMENU -p "What to do?" -mesg "$STATUS")

case $CHOICE in 
${OPTIONS[0]})
    
    if [ $(nmcli -g WIFI general) == "enabled" ]; then
        nmcli radio wifi off
    else 
        nmcli radio wifi on
    fi

;;
${OPTIONS[1]})
    
    CHCON=$(nmcli -g NAME connection | $DMENU -p "List of connections")
    if [ "$CHCON" ]; then
        WTODO=$(printf "%s\n" "${CONOPT[@]}" | $DMENU -p "What to do with $CHCON")  
    fi
    case $WTODO in
    ${CONOPT[0]}) # Connect to
        nmcli connection up "$CHCON"
    ;;
    ${CONOPT[1]}) # Info
        notify-send -u low "Comming soon" "Not added yet"
    ;;
    ${CONOPT[2]}) # Edit
        CHEDI=$(printf "%s\n" "${EDIOPT[@]}" | $DMENU -p "What to change?")
        case $CHEDI in
            ${EDIOPT[0]}) # Name
                EDICONNAME=$($DMENU -l 0 -p "New name for '$CHCON'")
                nmcli connection modify "$CHCON" connection.id "$EDICONNAME"
            ;;
            ${EDIOPT[1]}) # Autoconnect
                CURST=$(nmcli connection show "$CHCON" | grep "connection.autoconnect:" | awk '{print $2}')
                EDITCONAUCO=$(printf "yes\nno" | $DMENU -p "Autoconnect to '$CHCON'?" -mesg "Current state: $CURST")
                nmcli connection modify "$CHCON" connection.autoconnect $EDITCONAUCO
            ;;
            *)
                exit 0
            ;;
        esac

    ;;
    ${CONOPT[3]}) # Delete
        nmcli connection delete "$CHCON"
    ;;
    *)
        exit 0
    ;;
    esac

;;
${OPTIONS[2]})
    
    notify-send -u low "Scanning..."
    CHWIFI=$(nmcli -g SSID device wifi list | $DMENU -p "Choose wifi to connect")
    if [ "$CHWIFI" ]; then
        PASS=$($DMENU -l 0 -password -p "Password for $CHWIFI")
        if [ "$PASS" ]; then
            nmcli device wifi connect "$CHWIFI" password "$PASS"
        fi
    fi

;;
*)
    exit 0
;;
esac
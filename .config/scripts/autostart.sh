#!/usr/bin/env bash

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

### AUTOSTART ###

function run {
    if ! pgrep -f $1;
    then 
        $@&
    fi
}

run picom 
run feh --bg-fill --no-fehbg --randomize $HOME/wallpapers/ 
# run $HOME/.config/scripts/wallpaper.sh
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 
run timedatectl set-timezone Europe/Warsaw 
run dunst 
run key-mapper-control --command autoload 
run $HOME/.config/scripts/battery.sh 
run numlockx on 
run conky 
xset s off
# xset -dpms

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

### AUTOSTART FOR QTILE ###

picom &
feh --bg-fill --no-fehbg --randomize ~/wallpapers/minimal/ &
numlockx on &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
timedatectl set-timezone Europe/Warsaw &
dunst &
key-mapper-control --command autoload &

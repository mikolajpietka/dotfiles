#!/usr/bin/bash

# Autostart for Qtile

picom &
feh --bg-scale $HOME/wallpapers/$(ls -I "README.md" $HOME/wallpapers/ | shuf -n1) &
nm-applet &
numlockx on &
volumeicon &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

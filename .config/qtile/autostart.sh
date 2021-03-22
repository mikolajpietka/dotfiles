#!/bin/sh

# Autostart for Qtile

picom &
feh --bg-scale $HOME/Wallpapers/$(ls $HOME/Wallpapers/ | shuf -n1) &
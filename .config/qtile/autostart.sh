#!/bin/sh

# Autostart for Qtile
function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

picom &
feh --bg-scale $HOME/wallpapers/$(ls $HOME/wallpapers/ | shuf -n1) &

run nm-applet &
numlockx on &
run volumeicon &
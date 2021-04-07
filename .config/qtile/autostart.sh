#!/bin/sh

# Autostart for Qtile
function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

picom &
feh --bg-scale $HOME/wallpapers/$(ls -I "README.md" $HOME/wallpapers/ | shuf -n1) &

run nm-applet &
numlockx on &
run volumeicon &

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

declare -a OPEN=(
    "Configfiles"
    "Workspaces"
    "Wallpaper"
)

declare -a CONFIGFILES=(
    "Qtile"
    "Alacritty"
    "Starship"
    "Rofi"
    "Dunst"
    "Bashrc"
)

declare -a WORKSPACES=(
    "Dotfiles"
    "Notes"
)

declare -a WALLPAPERS=(
    "Earth"
    "Minimal"
)

DMENU="rofi -dmenu -i -l 5 -no-custom -no-show-icons"

TERMINAL="alacritty"

EDITOR="vim"

SETWALL="feh --bg-fill --no-fehbg --randomize"

CHOICE=$(printf '%s\n' ${OPEN[@]} | $DMENU -p "OPEN")
case $CHOICE in
${OPEN[0]})
    CHOICE=$(printf '%s\n' ${CONFIGFILES[@]} | $DMENU -p "Configfiles")
    case $CHOICE in
    ${CONFIGFILES[0]})
        $TERMINAL -e $EDITOR ~/.config/qtile/config.py
    ;;
    ${CONFIGFILES[1]})
        $TERMINAL -e $EDITOR ~/.config/alacritty/alacritty.yml
    ;;
    ${CONFIGFILES[2]})
        $TERMINAL -e $EDITOR ~/.config/starship.toml
    ;;
    ${CONFIGFILES[3]})
        $TERMINAL -e $EDITOR ~/.config/rofi/config.rasi
    ;;
    ${CONFIGFILES[4]})
        $TERMINAL -e $EDITOR ~/.config/dunst/dunstrc
    ;;
    ${CONFIGFILES[5]})
        $TERMINAL -e $EDITOR ~/.bashrc
    ;;
    *)
        exit 0
    ;;
    esac
;;
${OPEN[1]})
    CHOICE=$(printf '%s\n' ${WORKSPACES[@]} | $DMENU -p "Workspaces")
    case $CHOICE in
    ${WORKSPACES[0]})
        code ~/code/Dotfiles.code-workspace
    ;;
    ${WORKSPACES[1]})
        code ~/code/notes.code-workspace
    ;;
    *)
        exit 0
    ;;
    esac
;;
${OPEN[2]})
    CHOICE=$(printf '%s\n' ${WALLPAPERS[@]} | $DMENU -p "Wallpapers")
    case $CHOICE in
    ${WALLPAPERS[0]})
        $SETWALL ~/wallpapers/
    ;;
    ${WALLPAPERS[1]})
        $SETWALL ~/wallpapers/minimal
    ;;
    *)
        exit 0
    ;;
    esac
;;
*)
    exit 0
;;
esac
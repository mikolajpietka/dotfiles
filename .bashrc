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

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export HISTCONTROL=ignoreboth:erasedups

PS1='[\u@\h \W]\$ '

if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

# Ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

# List files
alias ls='exa -l'
alias ll='exa -la'
alias lt='exa -Tl'
alias lta='exa -Tla'
alias l='exa -l'
alias tree='exa -Tl'

# Progress monitor
alias prog='progress -m'

# Pacman
alias pacman='pacman --color auto'

# GRUB
alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'

# Errors from journalctl
alias jctl='journalctl -p 3 -xb'

# Loaded at start
neofetch

# Starship
eval "$(starship init bash)"
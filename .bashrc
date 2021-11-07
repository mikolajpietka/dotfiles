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

# Bashrc configuration

# PATH
if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

# Set editor to vim 
export EDITOR="nvim"

# Alias for nvim
alias vim="nvim"

# Set manpager to bat
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# Ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

# List files
alias ls="exa -l"
alias ll="exa -la"
alias lt="exa -Tl"
alias lta="exa -Tla"
alias l="exa -l"
alias tree="exa -Tl"

# Bat as cat
alias cat="bat"
export BAT_PAGER="less -RF"

# Progress monitor
alias prog="progress -m"

# Clear screen faster
alias cl="clear && neofetch"

# Pacman
alias pacman="pacman --color auto"
alias unlock="sudo rm /var/lib/pacman/db.lck"
alias update="sudo pacman -Syu --noconfirm && paru -Sua --noconfirm"
alias upshut="yes | sudo pacman -Syu && yes | paru -Sua && shutdown now"
alias cleanup="sudo pacman -Rns $(pacman -Qdtq)"
alias reflect="sudo reflector --sort rate -l 5 --save /etc/pacman.d/mirrorlist"

# Update group
alias update-grub="sudo grub-mkconfig -o /boot/grub/grub.cfg"
alias update-initcpio="sudo mkinitcpio -P"

# Edit group
alias edit-initcpio="sudo $EDITOR /etc/mkinitcpio.conf"
alias edit-grub="sudo $EDITOR /etc/default/grub"

# Errors from journalctl
alias jctl="journalctl -p 3 -xb"

# Power aliases
alias sdn="shutdown now"

# Loaded at start
neofetch

# The fuck command
eval "$(thefuck --alias)"

# Starship
eval "$(starship init bash)"

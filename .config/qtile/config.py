# Qtile config

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

# Imports
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy 
# For autostart.sh
import os
import subprocess

# Variables
mod = "mod4" # Windows key
terminal = "alacritty"
rofi = "rofi -show "
autostart = os.path.expanduser("~/.config/qtile/autostart.sh")
powermenu = os.path.expanduser("~/.config/rofi/scripts/powermenu.sh")
filemanager = "nautilus"
lockscreen = "physlock -mp 'Session locked'"
screenshot = "scrot '%Y%m%d_%H%M%S_screenshot.png' -e 'mv $f ~/Pictures/Screenshots/'"
screenshot_int = "scrot -sf '%Y%m%d_%H%M%S_screenshot.png' -e 'mv $f ~/Pictures/Screenshots/'"

##### KEY COMBINATIONS #####
keys = [
    # Special keys
    Key(
        [], "XF86AudioRaiseVolume", 
        lazy.spawn("amixer -q set Master 5%+ unmute"), 
        desc="Volume up"
    ),
    Key(
        [], "XF86AudioLowerVolume", 
        lazy.spawn("amixer -q set Master 5%- unmute"), 
        desc="Volume down"
    ),
    Key(
        [], "XF86AudioMute", 
        lazy.spawn("amixer -q set Master toggle"), 
        desc="Mute"
    ),
    Key(
        [], "XF86MonBrightnessUp",
        lazy.spawn("xbacklight + 10"),
        desc="Decrease brightness"
    ),
    Key(
        [], "XF86MonBrightnessDown",
        lazy.spawn("xbacklight - 10"),
        desc="Increase brightness"
    ),
    Key(
        [], "Print",
        lazy.spawn(screenshot),
        desc="Take screenshot"
    ),
    Key(
        ["control"], "Print",
        lazy.spawn(screenshot_int),
        desc="Take screenshot of chosen space"
    ),
    # Rofi
    Key(
        [mod], "r", 
        lazy.spawn(rofi + 'drun'), 
        desc="Spawn an app using a prompt"
    ),
    Key(
        [mod], "Tab", 
        lazy.spawn(rofi + 'window'), 
        desc="All windows in groups"
    ),
    Key(
        ["mod4", "mod1"], "r",
        lazy.spawn(rofi + 'run'),
        desc="Spawn a command using prompt"
    ),
    Key(
        [mod], "Escape",
        lazy.spawn(powermenu),
        desc="Powermenu"
    ),
    Key(
        [mod], "o",
        lazy.spawn(os.path.expanduser("~/.config/rofi/scripts/open.sh")),
        desc="Open script"
    ),
    # Terminal and files
    Key(
        [mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),
    Key(
        [mod], "e",
        lazy.spawn(filemanager),
        desc="Launch file manager"
    ),
    # Layouts & windows
    Key(
        [mod], "f", 
        lazy.window.toggle_floating(), 
        desc="Switch floating mode"
    ),
    Key(
        ["mod1"], "Tab", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
    ),
    Key(
        [mod], "equal", 
        lazy.layout.grow(),
        desc="Grow window"
    ),
    Key(
        [mod], "minus", 
        lazy.layout.shrink(),
        desc="Shrink window"
    ),
    Key(
        [mod], "space",
        lazy.screen.toggle_group(), 
        desc="Last group"
    ),
    Key(
        [mod], "q", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),
    # Qtile
    Key(
        [mod, "control"], "r", 
        lazy.restart(), 
        desc="Restart Qtile"
    ),
    # Lock screen
    Key(
        [mod], "l",
        lazy.spawn(lockscreen),
        desc="Lock system"
    ),
    # Calculator
    Key(
        [mod], "k",
        lazy.spawn('gnome-calculator')
    ),
]

##### GROUPS #####

# Name of groups
group_names = [
    "Web    ", #0
    "System ", #1
    "Code   ", #2
    "File   ", #3
    "Image  ", #4
    "Docs   ", #5
    "Fun    ", #6
]

group_prop = [
    (group_names[0], {'label': "爵", 'layout': 'max'}),
    (group_names[1], {'label': "", 'layout': 'monadtall'}),
    (group_names[2], {'label': "", 'layout': 'max'}),
    (group_names[3], {'label': "", 'layout': 'monadtall'}),
    (group_names[4], {'label': "", 'layout': 'max'}),
    (group_names[5], {'label': "", 'layout': 'max'}),
    (group_names[6], {'label': "", 'layout': 'max'}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_prop]

for i, (name, kwargs) in enumerate(group_prop, 1):
    keys.append(
        Key(
            [mod], str(i), 
            lazy.group[name].toscreen()
        ))
    keys.append(
        Key(
            [mod, "control"], str(i),
            lazy.window.togroup(name, switch_group=True) 
        ))


##### LAYOUTS #####

# Layouts
layout_theme = {
    "margin": 15, 
    "border_focus": "#8ecae6", 
    "border_normal": "#023047", 
    "border_width": 2, 
}

layouts = [
    layout.Max(
        **layout_theme,
    ),
    layout.MonadTall(
        **layout_theme,
        ratio=0.5
    ),
    layout.Floating(
        **layout_theme,
    ),
    layout.Bsp(
        **layout_theme,
        fair=False
    )
]

widget_defaults = dict(
    font='Ubuntu Bold',
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()


##### BAR/PANEL ######
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="UbuntuMono Nerd Font Bold",
                    fontsize=28,
                    padding=3,
                    highlight_method="line",
                    this_current_screen_border="#FFFFFF",
                    disable_drag=True,
                    inactive="999999",
                    highlight_color=['#ffffff50'] 
                ),
                widget.Spacer(
                    width=20
                ),
                widget.WindowName(
                    font="UbuntuMono Bold",
                    fontsize=14,
                    format="{name}",
                    max_chars=80
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/icon-clock.png",
                    margin_y=6,
                    margin_x=3
                ),
                widget.Clock(
                    format='%H:%M %a, %d.%m',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("gsimplecal")},
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/icon-wifi.png",
                    margin_y=6,
                    margin_x=3
                ),
                widget.Wlan(
                    interface="wlp9s0",
                    format="{essid} {percent:1.0%}",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("nm-connection-editor")},
                    foreground="#9EC1CF"
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/icon-sound.png",
                    margin_y=6,
                    margin_x=3
                ),
                widget.Volume(
                    device=None,
                    step=5,
                    foreground="#ff6663"
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/icon-brightness.png",
                    margin_y=6,
                    margin_x=3
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    update_interval=0.5,
                    step=5,
                    foreground="#FEB144",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("xbacklight -set 100")}
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/icon-battery.png",
                    margin_y=6,
                    margin_x=3
                ),
                widget.Battery(
                    charge_char='+',
                    discharge_char='',
                    full_char='+',
                    format='{char}{percent:1.0%}',
                    show_short_text=False,
                    update_interval=1,
                    foreground="#9EE09E",
                    notify_below=15
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons/")],
                    scale=0.5,
                    margin=0,
                    padding=0
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/button-power.png",
                    margin_y=6,
                    margin_x=5,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(powermenu)}
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 4
                ),
            ],
            28, # Height
            opacity=0.9,
            # margin = [5, 5, 5, 5] # Margin [N E S W]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1", 
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod], "Button3", 
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click(
        [mod], "Button2", 
        lazy.window.toggle_floating(),
    )
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='gnome-calculator'),
    ],
    border_focus='#8ecae6',
    border_normal='#023047',
    border_width=0,
    rounded=True
)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### APPS TO GROUP #####
@hook.subscribe.client_new
def to_group(client):
    g={}
    g[group_names[0]] = ["qutebrowser", "firefox", "microsoft teams - preview"]
    g[group_names[1]] = ["Alacritty"]
    g[group_names[2]] = ["code-oss", "code"]
    g[group_names[3]] = ["org.gnome.Nautilus"]
    g[group_names[4]] = ["gimp-2.10", "gimp", "feh", "eog"]
    g[group_names[5]] = ["evince", "libreoffice", "soffice", "gedit"]
    g[group_names[6]] = ["spotify", "vlc", "Popcorn-Time", "transmission-gtk"]

    wm_class = client.window.get_wm_class()[0]
    for i in range(len(g)):
        if wm_class in list(g.values())[i]:
            group = list(g.keys())[i]
            client.togroup(group, switch_group=True)

##### AUTOSTART #####
@hook.subscribe.startup_once
def startup_once():
    subprocess.call([autostart])

# Weird line but... If it's here I will leave it
wmname = "Qtile"
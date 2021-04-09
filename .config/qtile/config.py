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
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy 
# For autostart.sh
import os
import subprocess

# Variables
mod = "mod4" # Windows key
terminal = "alacritty"
rofi = "rofi -show "
autostart = os.path.expanduser("~/.config/qtile/autostart.sh")
filemanager = "nautilus"
wallpaper_folder = "~/wallpapers/minimal"

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
    # Rofi
    Key(
        [mod], "r", 
        lazy.spawn(rofi + 'drun'), 
        desc="Spawn a command using a prompt widget"
    ),
    Key(
        [mod], "Tab", 
        lazy.spawn(rofi + 'window'), 
        desc="All windows in groups"
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
        [mod], "Up", 
        lazy.layout.grow(),
        desc="Grow window"
    ),
    Key(
        [mod], "Down", 
        lazy.layout.shrink(),
        desc="Shrink window"
    ),
    Key(
        [mod], "space",
        lazy.screen.next_group(), 
        desc="Next group"
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

    # Key chords
    KeyChord(
        [mod], "w", [
            Key(
                [], "m", 
                lazy.window.toggle_floating(), 
                desc="Toggle floating"
            ),
            Key(
                [], "f", 
                lazy.window.toggle_fullscreen(),
                desc="Fullscreen"
            ),
            Key(
                [], "Left", 
                lazy.layout.shuffle_left(), 
                desc="Move window to the left"
            ),
            Key(
                [], "Right", 
                lazy.layout.shuffle_right(), 
                desc="Move window to the right"
            ),
            Key(
                [], "Down", 
                lazy.layout.shuffle_down(), 
                desc="Move window down"
            ),
            Key(
                [], "Up", 
                lazy.layout.shuffle_up(), 
                desc="Move window up"
            ),
            Key(
                [], "Tab", 
                lazy.layout.next(),
                desc="Next window"
            ),
        ],
        mode="Window"
    ),
]

##### GROUPS #####

# Name groups
groups_names = [
    ("WWW", {'label': "", 'layout': 'max'}),
    ("SYS", {'label': "", 'layout': 'monadtall'}),
    ("DEV", {'label': "", 'layout': 'max'}),
    ("FIL", {'label': "", 'layout': 'monadtall'}),
    ("IMG", {'label': "", 'layout': 'max'})
]

groups = [Group(name, **kwargs) for name, kwargs in groups_names]

for i, (name, kwargs) in enumerate(groups_names, 1):
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
    "margin": 10, 
    "border_focus": "#8ecae6", 
    "border_normal": "#023047", 
    "border_width": 2, 
    "ratio": 0.5
}

layouts = [
    layout.Max(
        **layout_theme,
    ),
    layout.MonadTall(
        **layout_theme,
    ),
    layout.Floating(
        **layout_theme,
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
                widget.Image(
                    filename="~/.config/qtile/icons/arcolinux.png",
                    margin_y=4,
                    margin_x=6
                ),
                widget.GroupBox(
                    font="FontAwesome Bold",
                    fontsize=15,
                    padding=3,
                    highlight_method="line",
                    this_current_screen_border="#FFFFFF",
                    disable_drag=True,
                    inactive="999999",
                    highlight_color=['#ffffff50'] 
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/separator.png",
                    margin_y=6,
                    margin_x=10
                ),
                widget.WindowName(
                    format="{name}"
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper()
                ),
                widget.Notify(
                    default_timeout=10,
                    fmt="{}"
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/icon-clock.png",
                    margin_y=6,
                    margin_x=3
                ),
                widget.Clock(
                    format='%H:%M %a, %d.%m',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("gnome-calendar")},
                ),
                widget.Image(
                    filename="~/.config/qtile/icons/icon-wifi.png",
                    margin_y=6,
                    margin_x=3
                ),
                widget.Wlan(
                    interface="wlp9s0",
                    format="{essid} {percent:2.0%}",
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
                    foreground="#FEB144"
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
                    foreground="#9EE09E"
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons/")],
                    scale=0.5,
                    margin=0,
                    padding=0
                ),
                widget.WidgetBox(
                    widgets=[
                        widget.Image(
                            filename="~/.config/qtile/icons/separator.png",
                            margin_y=6,
                            margin_x=10
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/icon-update.png",
                            margin_y=6,
                            margin_x=3
                        ),
                        widget.CheckUpdates(
                            display_format="{updates}",
                            colour_have_updates="#9EC1CF",
                            colour_no_updates="#9EC1CF",
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                            no_update_string="0"
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/icon-folder.png",
                            margin_y=6,
                            margin_x=3
                        ),
                        widget.DF(
                            visible_on_warn=False,
                            format="{uf}{m}",
                            foreground="#FCD462"
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/icon-wallpaper.png",
                            margin_y=6,
                            margin_x=3
                        ),
                        widget.Wallpaper(
                            directory=wallpaper_folder,
                            fmt="",
                            font="FontAwesome",
                            fontsize=14,
                            random_selection=True,
                            foreground="#4CAF50"
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/separator.png",
                            margin_y=6,
                            margin_x=10
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/button-power.png",
                            margin_y=6,
                            margin_x=5,
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("shutdown now")}
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/button-reboot.png",
                            margin_y=6,
                            margin_x=5,
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("reboot")}
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/button-logout.png",
                            margin_y=6,
                            margin_x=5,
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_shutdown()}
                        ),
                    ],
                    font='FontAwesome',
                    text_closed="  ",
                    text_open="  ",
                    close_button_location="right",
		            fontsize=14,
		            padding=0
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 4
                ),
            ],
            28, # Height
            opacity=0.9,
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
main = None  # WARNING: this is deprecated and will be removed soon
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
    ],
    border_focus='#8ecae6',
    border_normal='#023047',
    border_width=3,
    rounded=True
)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### AUTOSTART #####
@hook.subscribe.startup_once
def startup_once():
    subprocess.call([autostart])

# Weird line but... If it's here I will leave it
wmname = "Qtile"

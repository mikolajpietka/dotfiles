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
lockscreen = "gnome-screensaver-command -l"

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
        lazy.spawn("gnome-screenshot"),
        desc="Take screenshot"
    ),
    Key(
        ["control"], "Print",
        lazy.spawn("gnome-screenshot -i"),
        desc="Screenshot settings"
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
group_names = [
    "Web", #0
    "System", #1
    "Code", #2
    "File", #3
    "Image", #4
    "Document", #5
    "Fun", #6
]
group_prop = [
    (group_names[0], {'label': "", 'layout': 'max'}),
    (group_names[1], {'label': "", 'layout': 'monadtall'}),
    (group_names[2], {'label': "", 'layout': 'max'}),
    (group_names[3], {'label': "", 'layout': 'monadtall'}),
    (group_names[4], {'label': "", 'layout': 'max'}),
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
                # widget.Image(
                #     filename="~/.config/qtile/icons/arcolinux.png",
                #     margin_y=4,
                #     margin_x=6
                # ),
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
                    font="UbuntuMono Bold",
                    fontsize=14,
                    format="{name}"
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper()
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
                            filename="~/.config/qtile/icons/button-logout.png",
                            margin_y=6,
                            margin_x=5,
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_shutdown()}
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/button-reboot.png",
                            margin_y=6,
                            margin_x=5,
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("reboot")}
                        ),
                        widget.Image(
                            filename="~/.config/qtile/icons/button-power.png",
                            margin_y=6,
                            margin_x=5,
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("shutdown now")}
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

##### WINDOW TO GROUP #####
@hook.subscribe.client_new
def to_group(client):
    g={}
    g[group_names[0]] = ["Navigator", "firefox", "vivaldi-stable"]
    g[group_names[1]] = ["Alacritty"]
    g[group_names[2]] = ["code-oss"]
    g[group_names[3]] = ["org.gnome.Nautilus"]
    g[group_names[4]] = ["gimp-2.10", "gimp", "feh", "eog"]
    g[group_names[5]] = ["evince", "libreoffice", "soffice"]
    g[group_names[6]] = ["spotify", "vlc"]

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

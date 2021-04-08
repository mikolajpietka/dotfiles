# Qtile config by Mikolaj Pietka

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
rofi = "rofi -show drun"
autostart_path = "~/.config/qtile/autostart.sh"

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
    # Rofi drun
    Key(
        [mod], "r", 
        lazy.spawn(rofi), 
        desc="Spawn a command using a prompt widget"
    ),
    # Terminal
    Key(
        [mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
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
        [mod], "Tab", 
        lazy.screen.next_group(), 
        desc="Jumo between groups"
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
    ("WWW", {'layout': 'max'}),
    ("SYS", {'layout': 'monadtall'}),
    ("DEV", {'layout': 'max'}),
    ("FLT", {'layout': 'floating'}),
    ("BCK", {'layout': 'monadtall'})
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

# Number groups
# groups = [Group(i) for i in "12345"]
# for i in groups:
#     keys.extend([
#         Key(
#             [mod], i.name, 
#             lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)
#         ),
#         Key(
#             [mod, "shift"], i.name, 
#             lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)
#         ),
#     ])

##### LAYOUTS #####

# Layouts
layout_theme = {
    "margin": 8, 
    "border_focus": "#8ecae6", 
    "border_normal": "#023047", 
    "border_width": 3, 
    "ratio": 0.5
}

layouts = [
    layout.Max(
        **layout_theme,
        name=""
    ),
    layout.MonadTall(
        **layout_theme,
        name=""
    ),
    layout.Floating(
        **layout_theme,
        name=""
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
                    padding=3,
                    highlight_method="line",
                    this_current_screen_border="#0183daa8",
                    disable_drag=True,
                    inactive="999999",
                    highlight_color=['0183daa8'] 
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
                    fmt=" {}"
                ),
                widget.CurrentLayout(
                    font="FontAwesome",
                    fontsize=14
                ),
                widget.Sep(
                    linewidth=2,
                    padding=6,
                    size_percent=65
                ),
                widget.Clock(
                    format='%H:%M %a, %d.%m',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("gnome-calendar")},
                ),
                widget.Sep(
                    linewidth=2,
                    padding=6,
                    size_percent=65
                ),
                widget.TextBox(
                    text="",
                    fontsize=14,
                    font="FontAwesome"
                ),
                widget.Wlan(
                    interface="wlp9s0",
                    format="{essid} {percent:2.0%}",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("nm-connection-editor")},
                ),
                widget.TextBox(
                    text="",
                    fontsize=14,
                    font="FontAwesome"
                ),
                widget.Volume(
                    device=None,
                    step=5,
                ),
                widget.TextBox(
                    text="",
                    fontsize=14,
                    font="font-awesome"
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    update_interval=0.5,
                    step=5,
                ),
                widget.TextBox(
                    text="",
                    fontsize=14,
                    font="FontAwesome"
                ),
                widget.Battery(
                    charge_char='+',
                    discharge_char='',
                    full_char='+',
                    format='{char}{percent:1.0%}',
                    show_short_text=False,
                    update_interval=1
                ),
                widget.Sep(
                    linewidth=2,
                    padding=6,
                    size_percent=65
                ),
                widget.WidgetBox(
                    widgets=[
                        widget.DF(
                            visible_on_warn=False,
                            format=" {uf}{m}"
                        ),
                        widget.Wallpaper(
                            directory="~/wallpapers/",
                            fmt="",
                            font="FontAwesome",
                            fontsize=14,
                            random_selection=True
                        ),
                        widget.Sep(
                            linewidth=2,
                            padding=6,
                            size_percent=65
                        ),
                        widget.TextBox(
                            font='FontAwesome',
                            fontsize=14,
                            text="",
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("shutdown now")}
                        ),
                        widget.TextBox(
                            font='FontAwesome',
                            fontsize=14,
                            text="",
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("reboot")}
                        ),
                        widget.TextBox(
                            font='FontAwesome',
                            fontsize=14,
                            text="",
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
    autostart = os.path.expanduser(autostart_path)
    subprocess.call([autostart])

# Weird line but... If it's here I will leave it
wmname = "Qtile"

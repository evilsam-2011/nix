import os
import subprocess
from collections.abc import Callable

import libqtile.resources
from libqtile import bar, layout, qtile

try:
    from qtile_extras import widget
    from qtile_extras.widget.decorations import BorderDecoration

    _has_decorations = True
except ImportError:
    from libqtile import widget

    _has_decorations = False

from libqtile.config import Click, Drag, Group, Key, Match, Output, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook



mod = "mod4"
terminal = "foot"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "v", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    KeyChord([mod], "w", [
        Key([], "w", lazy.spawn("fuzzel")),
        Key([], "p", lazy.spawn("waypaper")),
    ], name="launch"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=["#7aa2f7", "#3d59a1"],
        border_normal="#3b4261",
        border_width=4,
        border_on_single=True,
        margin = 5,
        margin_on_single = 5,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        border_focus=["#7aa2f7", "#3d59a1"],
        border_normal="#3b4261",
        border_width=4,
        border_on_single=True,
        margin = 5,
        margin_on_single = 5,
    ),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(
        border_focus=["#7aa2f7", "#3d59a1"],
        border_normal="#3b4261",
        border_width=4,
        margin = 5,
        margin_on_single = 5,
    ),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# --- Tokyo Night palette ---
bg      = "#1a1b26"
bg_dark = "#16161e"
fg      = "#c0caf5"
fg_dim  = "#565f89"
blue    = "#7aa2f7"
cyan    = "#7dcfff"
magenta = "#bb9af7"
green   = "#9ece6a"
yellow  = "#e0af68"
orange  = "#ff9e64"
red     = "#f7768e"
brblk   = "#444b6a"


def module(colour):
    """Waybar-style module: coloured text on the bar background, with a
    matching 4px line drawn along the bottom edge."""
    cfg = {"foreground": colour, "background": bg}
    if _has_decorations:
        cfg["decorations"] = [
            BorderDecoration(border_width=[0, 0, 4, 0], colour=colour)
        ]
    return cfg


def sep():
    """Thin '|' separator between modules."""
    return widget.TextBox(
        text="|",
        font="JetBrainsMono Nerd Font",
        fontsize=13,
        padding=4,
        foreground=brblk,
        background=bg,
    )


widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=13,
    padding=6,
    foreground=fg,
)
extension_defaults = widget_defaults.copy()

logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(**module(blue)),
                sep(),
                widget.GroupBox(
                    highlight_method="block",
                    active=fg,
                    inactive=fg_dim,
                    this_current_screen_border=blue,
                    urgent_text=red,
                    urgent_border=red,
                    borderwidth=3,
                    disable_drag=True,
                    background=bg,
                ),
                widget.Prompt(background=bg),
                widget.Chord(
                    chords_colors={"launch": (bg, blue)},
                    name_transform=lambda name: name.upper(),
                    background=bg,
                ),
                widget.Spacer(background=bg),
                widget.CPU(
                    format=" \uf2db {load_percent:2.0f}%",
                    update_interval=2,
                    **module(cyan),
                ),
                sep(),
                widget.Memory(
                    format=" \U000F035B {MemPercent:2.0f}%",
                    update_interval=2,
                    **module(green),
                ),
                sep(),
                widget.Battery(
                    format=" \uf240 {percent:2.0%}",
                    low_percentage=0.20,
                    low_foreground=red,
                    update_interval=10,
                    **module(yellow),
                ),
                sep(),
                widget.PulseVolume(
                    mute_format=" \uf026 {volume}%",
                    unmute_format=" \uf028 {volume}%",
                    **module(magenta),
                ),
                sep(),
                widget.Wlan(
                    interface="wlp3s0",
                    format=" \uf1eb {essid} {percent:2.0%}",
                    disconnected_message=" \uf1eb off",
                    update_interval=5,
                    **module(blue),
                ),
                sep(),
                widget.Clock(
                    format=" \uf017 %a %H:%M",
                    **module(orange),
                ),
                sep(),
                widget.StatusNotifier(background=bg),
            ],
            30,
            background=bg,
        ),
        wallpaper=logo,
        wallpaper_mode="center",
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Instead of screens, you can define a function here to specify which Screen
# should correspond to which Output.
fake_screens: list[Screen] | None = None

# Instead of screens or fake screens, you can define a function here that
# returns a list of Screen objects based on the list of Outputs; that way you
# can decide based on e.g. the number of screens, or which ports are plugged
# in exactly what do render in each bar for each screen.
generate_screens: Callable[[list[Output]], list[Screen]] | None = None

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# How long (in seconds) to wait after a screen change event before firing the
# screen_change hook, coalescing bursts of events into a single one.
screen_change_debounce_timeout = 1

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

idle_timers = []  # type: list
idle_inhibitors = []  # type: list

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

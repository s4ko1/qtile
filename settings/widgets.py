from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=2)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="󰽣", # Icon: nf-oct-triangle_left
        fontsize=40,
        padding=-5
    )

def powerlineInv(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="󰽡", # Icon: nf-oct-triangle_left
        fontsize=40,
        padding=-5
    )



def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='FiraCode Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['morado'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=13, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),


    powerline(fg="morado"),
    icon(bg="morado", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['morado'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
        padding=0,
    ),

    powerlineInv(fg='morado'),
    separator(),

    powerline(fg="color3"),
    widget.Net(**base(bg='color3'), interface='wlp0s20f0u1', format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}'),
    powerlineInv(fg='color3'),
    separator(),

    powerline(fg="color2"),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    powerlineInv(fg='color2'),
    separator(),
    # widget.CurrentLayout(**base(bg='color2'), padding=5),


    # icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    powerline(fg="color1"),
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    powerlineInv(fg='color1'),

    separator(),
    powerline(fg="negro_icons"),
    widget.Systray(background=colors['negro_icons'], padding=5),
    powerlineInv(fg='negro_icons'),
]

secondary_widgets = [
    *workspaces(),

    separator(),


    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    # widget.CurrentLayout(**base(bg='color1'), padding=5),


    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),


]

widget_defaults = {
    'font': 'FiraCode Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

# MACROPAD Hotkeys: Slack (and Discord) for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Slack/Discord',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        # Mark all channels read
        (0x004000, 'All Read', [Keycode.SHIFT, Keycode.ESCAPE]),
        (0x000000, '', []),
        (0x303000, 'Status', [Keycode.COMMAND,
                              Keycode.SHIFT, 'y']),  # Set a status
        # 2nd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000040, 'Channels', [Keycode.COMMAND,
                                Keycode.SHIFT, 'l']),  # Channel Browser
        (0x000000, '', []),
        (0x000040, 'Jump to', [Keycode.COMMAND, 'k']),  # open channel / chat
        # 4th row ----------
        (0xffa500, 'DND-30', ['/d', 0.5, 'nd 30 min\n\n\n']),  # DND 30 min
        (0x000000, '', []),
        # set away and DND until tomorrow
        (0x400000, 'EOD', ['/', 'a', 0.5, 'way\n\n\n', 0.5,
                           '/', 'd', 0.5, 'nd tomorrow\n\n\n']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}

# MACROPAD Hotkeys: Zoom for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "Zoom",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        # audio toggle
        (0x400000, "Mic", [Keycode.SHIFT, Keycode.COMMAND, "a"]),
        (0x000000, "", []),
        (0x004000, "Camera", [Keycode.SHIFT, Keycode.COMMAND, "v"]),  # video toggle
        # 2nd row ----------
        (0x000000, "", []),
        (0x000000, "", []),
        (0x000000, "", []),
        # 3rd row ----------
        # view toggle (gallery/speaker)
        (0x000040, "View", [Keycode.SHIFT, Keycode.COMMAND, "w"]),
        (0x000000, "", []),
        (0x000040, "Users", [Keycode.COMMAND, "u"]),  # participants toggle
        # 4th row ----------
        (0x000000, "", []),
        (0x202000, "Hand", [Keycode.ALT, "y"]),  # raise/lower hand
        (0x000000, "", []),
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # close window
    ],
}

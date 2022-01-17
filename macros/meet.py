# MACROPAD Hotkeys: Google Meet for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "Meet",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, "Mic", [Keycode.COMMAND, "d"]),  # audio toggle
        (0x000000, "", []),
        (0x004000, "Camera", [Keycode.COMMAND, "e"]),  # video toggle
        # 2nd row ----------
        (0x000000, "", []),
        (0x000000, "", []),
        (0x000000, "", []),
        # 3rd row ----------
        (
            0x000040,
            "View",
            [Keycode.CONTROL, Keycode.COMMAND, "p"],
        ),  # view toggle (gallery/speaker)
        (0x000000, "", []),
        (0x000040, "Chat", [Keycode.CONTROL, Keycode.COMMAND, "c"]),  # chat toggle
        # 4th row ----------
        (0x000000, "", []),
        (0x202000, "Hand", [Keycode.CONTROL, Keycode.COMMAND, "h"]),  # raise/lower hand
        (0x000000, "", []),
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, "w"]),  # close window
    ],
}

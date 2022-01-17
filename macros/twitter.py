# MACROPAD Hotkeys: Twitter for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "Twitter",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x024E9A, "Tweet", [Keycode.COMMAND, "n"]),  # new Tweet
        (0x024E9A, "DMs", [Keycode.COMMAND, "4"]),  # direct messages
        (
            0x024E9A,
            "Refresh",
            [Keycode.SHIFT, Keycode.COMMAND, "r"],
        ),  # refresh timeline
        # 2nd row ----------
        (0x000000, "", []),
        (0x024E9A, "Profile", [Keycode.COMMAND, "7"]),  # show user profile
        (0x000000, "", []),
        # 3rd row ----------
        (0x024E9A, "Home", [Keycode.COMMAND, "1"]),  # home timeline
        (0x024E9A, "[@]", [Keycode.COMMAND, "3"]),  # notifications / mentions
        (0x024E9A, "Explore", [Keycode.COMMAND, "2"]),  # explore / search
        # 4th row ----------
        (
            0x024E9A,
            "< Prev",
            [Keycode.SHIFT, Keycode.COMMAND, "["],
        ),  # previous pinned list / tab
        (0x000000, "", []),
        (
            0x024E9A,
            "Next >",
            [Keycode.SHIFT, Keycode.COMMAND, "]"],
        ),  # next pinned list / tab
        # Encoder button ---
        (0x000000, "", [Keycode.COMMAND, Keycode.CONTROL, "]"]),  # next account
    ],
}

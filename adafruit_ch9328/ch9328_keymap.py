# SPDX-FileCopyrightText: Copyright (c) 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_ch9328.ch9328_keymap`
================================================================================

CircuitPython driver for the CH9328 UART to HID keyboard breakout


* Author(s): Liz Clark

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""


# pylint: disable=too-few-public-methods, invalid-name
class Keymap:
    """Keymap for the Adafruit CH9328 UART to HID keyboard driver"""

    # Modifier keys
    LEFT_CTRL = 0x01
    LEFT_SHIFT = 0x02
    LEFT_ALT = 0x04
    LEFT_GUI = 0x08
    RIGHT_CTRL = 0x10
    RIGHT_SHIFT = 0x20
    RIGHT_ALT = 0x40
    RIGHT_GUI = 0x80

    # Keycodes
    A = 0x04
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0A
    H = 0x0B
    I = 0x0C
    J = 0x0D
    K = 0x0E
    L = 0x0F
    M = 0x10
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x14
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1A
    X = 0x1B
    Y = 0x1C
    Z = 0x1D

    ONE = 0x1E
    TWO = 0x1F
    THREE = 0x20
    FOUR = 0x21
    FIVE = 0x22
    SIX = 0x23
    SEVEN = 0x24
    EIGHT = 0x25
    NINE = 0x26
    ZERO = 0x27

    ENTER = 0x28
    ESC = 0x29
    BACKSPACE = 0x2A
    TAB = 0x2B
    SPACE = 0x2C
    MINUS = 0x2D
    EQUAL = 0x2E
    LEFT_BRACE = 0x2F
    RIGHT_BRACE = 0x30
    BACKSLASH = 0x31
    SEMICOLON = 0x33
    QUOTE = 0x34
    TILDE = 0x35
    COMMA = 0x36
    PERIOD = 0x37
    SLASH = 0x38
    CAPS_LOCK = 0x39

    F1 = 0x3A
    F2 = 0x3B
    F3 = 0x3C
    F4 = 0x3D
    F5 = 0x3E
    F6 = 0x3F
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45

    PRINTSCREEN = 0x46
    SCROLL_LOCK = 0x47
    PAUSE = 0x48
    INSERT = 0x49
    HOME = 0x4A
    PAGE_UP = 0x4B
    DELETE = 0x4C
    END = 0x4D
    PAGE_DOWN = 0x4E
    RIGHT = 0x4F
    LEFT = 0x50
    DOWN = 0x51
    UP = 0x52

    NUM_LOCK = 0x53
    NUMPAD_SLASH = 0x54
    NUMPAD_ASTERISK = 0x55
    NUMPAD_MINUS = 0x56
    NUMPAD_PLUS = 0x57
    NUMPAD_ENTER = 0x58
    NUMPAD_1 = 0x59
    NUMPAD_2 = 0x5A
    NUMPAD_3 = 0x5B
    NUMPAD_4 = 0x5C
    NUMPAD_5 = 0x5D
    NUMPAD_6 = 0x5E
    NUMPAD_7 = 0x5F
    NUMPAD_8 = 0x60
    NUMPAD_9 = 0x61
    NUMPAD_0 = 0x62
    NUMPAD_PERIOD = 0x63

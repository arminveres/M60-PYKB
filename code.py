# ruff: noqa: F405

# use this for the frozen library
# from PYKB import *

# to use this, copy over keyboard folder to 'lib'
from lib.keyboard import *


keyboard = Keyboard()
# General keyboard settings
keyboard.matrix.debounce_time = 8  # miliseconds
keyboard.tap_delay = 200
keyboard.fast_type_thresh = 100
# keyboard.backlight.on()

___ = TRANSPARENT  # takes the underlying keybind
BOOT = BOOTLOADER
L1 = LAYER_TAP(1)
L2F = LAYER_TAP(2, F)
L3B = LAYER_TAP(3, B)
LSFT4 = LAYER_MODS(4, MODS(LSHIFT))
RSFT4 = LAYER_MODS(4, MODS(RSHIFT))
L5S = LAYER_TAP(5, S)

# Semicolon & Ctrl
SCC = MODS_TAP(MODS(RCTRL), ";")
SINS = MODS_KEY(MODS(SHIFT), INSERT)
# When tapping, use as ESC, when holding, as LCTRL
ESCTL = MODS_TAP(MODS(LCTRL), ESC)

# Display related renames
DBU = DISPLAY_BRIGHTNESS_UP
DBD = DISPLAY_BRIGHTNESS_DOWN
PPT = TRANSPORT_PREV_TRACK
PNT = TRANSPORT_NEXT_TRACK
PPP = TRANSPORT_PLAY_PAUSE

# fmt: off
keyboard.keymap = (
    # layer 0
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        LCTRL,  A,   S,   D, L2F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
        LSFT4, Z,   X,   C,   V, L3B,   N,   M, ',', '.', '/',         RSFT4,
        CAPS, LALT, LGUI,          SPACE,            RALT, RGUI,  L1, RCTRL
    ),

    # layer 1
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___,  UP, ___, ___, ___, ___, ___, ___, ___,SUSPEND,___,___,___,
        ___,LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___,BOOT, ___, ___, ___, ___, ___,       ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 2
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___, ___, ___, ___, ___,HOME,PGUP, ___, ___,SINS,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, ___, ___, ___, ___, ___,LEFT,DOWN, UP,RIGHT, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___,PGDN,END, PPT, PNT, PPP,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3
    # NOTE: currently I don't need any bluetooth related features
    # (
    #     BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, ___, ___, ___,
    #     RGB_MOD, ___, ___, ___, ___, ___,___,USB_TOGGLE,___,___,___,___,___, ___,
    #     RGB_TOGGLE,HUE_RGB,RGB_HUE,SAT_RGB,RGB_SAT,___,___,___,___,___,___,___,      ___,
    #     ___, ___, ___, ___, ___, ___, ___, ___,VAL_RGB,RGB_VAL, ___,           ___,
    #     ___, ___, ___,                ___,               ___, ___, ___,  ___
    # ),
    (
        RGB_TOGGLE, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, DBD, DBU, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),


    # layer 4
    (
        '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___,   D, ___, ___, ___, ___, ___, ___, ';', ___,      ___,
        ___, ___, ___, ___, ___,   B, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 5
    (
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___,MS_W_UP,MS_UL,MS_UP,MS_UR, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___,MS_BTN1,MS_LT,MS_DN,MS_RT,MS_BTN2, ___,      ___,
        ___, ___, ___, ___, ___, ___,MS_W_DN,MS_DL,MS_DN,MS_DR, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),
)

# Use different keymaps on different connections
# Valid keys are "USB" and "BT0"-"BT9"
# Connection not in this map will use default keymap defined above.
keyboard.profiles = {
    # For example, BT8 is connected to a Mac
    "BT8": (
        # layer 0
        (
            ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
            TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
            CAPS,  A,   S,   D,   F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
            LSHIFT,Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',        RSHIFT,
            LCTRL, LALT, LGUI,          SPACE,            MENU, RALT,  L1, RCTRL
        ),

        # layer 1
        (
            '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
            ___, ___,  UP, ___, ___, ___, ___, ___, ___, ___,SUSPEND,___,___,___,
            ___,LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___,      ___,
            ___, ___, ___, ___, ___,BOOT, ___,MACRO(1), ___, ___, ___,       ___,
            ___, ___, ___,                ___,               ___, ___, ___,  ___
        ),
    )
}
# fmt: on


def macro_handler(dev: Device, n: int, is_down: bool):
    # dev.backlight.set_brightness(255)
    if is_down:
        # dev.send_text("You pressed macro #{}\n".format(n))
        print("You pressed macro #{}\n".format(n))
        # dev.backlight.pixel(54, 0xFF, 0, 0)
    else:
        # dev.send_text("You released macro #{}\n".format(n))
        print("You released macro #{}\n".format(n))
        # dev.backlight.pixel(54, 0, 0xFF, 0)
    # dev.backlight.update()


def pairs_handler(dev: Device, n: int):
    pass
    # dev.send_text("You just triggered pair keys #{}\n".format(n))


# ESC(0)    1(1)   2(2)   3(3)   4(4)   5(5)   6(6)   7(7)   8(8)   9(9)   0(10)  -(11)  =(12)  BACKSPACE(13)
# TAB(27)   Q(26)  W(25)  E(24)  R(23)  T(22)  Y(21)  U(20)  I(19)  O(18)  P(17)  [(16)  ](15)   \(14)
# CAPS(28)  A(29)  S(30)  D(31)  F(32)  G(33)  H(34)  J(35)  K(36)  L(37)  ;(38)  "(39)      ENTER(40)
# LSHIFT(52) Z(51)  X(50)  C(49)  V(48)  B(47)  N(46)  M(45)  ,(44)  .(43)  /(42)            RSHIFT(41)
# LCTRL(53)  LGUI(54)  LALT(55)               SPACE(56)          RALT(57)  MENU(58)  Fn(59)  RCTRL(60)

keyboard.macro_handler = macro_handler
keyboard.pairs_handler = pairs_handler
# Pairs: J & K, U & I
# keyboard.pairs = [{35, 36}, {20, 19}]
keyboard.verbose = False

keyboard.run()

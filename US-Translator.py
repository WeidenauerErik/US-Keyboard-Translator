import time

import keyboard
import pyperclip


def print_ae():
    pyperclip.copy('ä')


def print_AE():
    pyperclip.copy('Ä')


def print_ue():
    pyperclip.copy('ü')


def print_UE():
    pyperclip.copy('Ü')


def print_oe():
    pyperclip.copy('ö')


def print_OE():
    pyperclip.copy('Ö')


keyboard.add_hotkey('ctrl+alt+a', print_ae)
keyboard.add_hotkey('ctrl+alt+shift+a', print_AE)
keyboard.add_hotkey('ctrl+alt+u', print_ue)
keyboard.add_hotkey('ctrl+alt+shift+u', print_UE)
keyboard.add_hotkey('ctrl+alt+o', print_oe)
keyboard.add_hotkey('ctrl+alt+shift+o', print_OE)
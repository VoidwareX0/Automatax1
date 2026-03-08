"""Core module tests"""
import pytest
from automatax1.core import Device, Touch, Keyboard

def test_device_creation():
    device = Device()
    assert device is not None

def test_touch_click():
    device = Device()
    touch = Touch(device)
    assert touch.click(100, 200) == True

def test_keyboard_type():
    device = Device()
    kb = Keyboard(device)
    assert kb.type("Hello") == True
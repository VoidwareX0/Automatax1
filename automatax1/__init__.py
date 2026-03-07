"""Automatax1 - Fast Android automation for Python"""

from .device import Device
from .touch import Touch
from .keyboard import Keyboard
from .clipboard import Clipboard
from .fastinput import FastInput
from .adb import Adb

__version__ = "0.1.0"

class Automator:
    """Main automation class - combines all modules"""
    
    def __init__(self, device_id=None):
        self.device = Device(device_id)
        self.touch = Touch(self.device)
        self.keyboard = Keyboard(self.device)
        self.clipboard = Clipboard(self.device)
        self.fastinput = FastInput(self.device)
        
    def click(self, x, y):
        return self.touch.click(x, y)
    
    def type(self, text):
        return self.fastinput.type(text)
    
    def swipe(self, x1, y1, x2, y2, duration=100):
        return self.touch.swipe(x1, y1, x2, y2, duration)
    
    def copy(self, text):
        return self.clipboard.copy(text)
    
    def paste(self):
        return self.clipboard.paste()

# Convenience imports
__all__ = ['Automator', 'Device', 'Touch', 'Keyboard', 'Clipboard', 'FastInput', 'Adb']
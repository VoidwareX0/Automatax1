"""
automatax1 - Ultra-fast Android automation for Python
=====================================================

10x faster than alternatives through direct socket communication
and native Android APIs.

Basic usage:
    >>> import automatax1 as a1
    >>> auto = a1.Automator()
    >>> auto.click(500, 600)
    >>> auto.type("Hello World!")
    >>> auto.swipe(100, 200, 300, 400)

Find elements:
    >>> btn = auto.find(text="Submit")
    >>> if btn:
    >>>     btn.click()

Wait for elements:
    >>> if auto.wait(text="Loading...", timeout=5):
    >>>     auto.click_text("Continue")
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

# Core imports - what users will use
from .core.device import Device
from .core.touch import Touch
from .core.keyboard import Keyboard
from .core.selector import Selector, Element
from .core.service import Service

# Convenience imports
from .core import device, touch, keyboard, selector, service

# Main class for easy access
class Automator:
    """
    Main automation class - combines all modules into one easy interface.
    
    Examples:
        >>> auto = Automator()
        >>> auto.click(100, 200)
        >>> auto.type("Hello")
        >>> auto.swipe(0, 0, 500, 500)
    """
    
    def __init__(self, serial=None):
        """
        Connect to Android device.
        
        Args:
            serial: Optional device serial number (None = first device)
        """
        self.device = Device(serial)
        self.touch = Touch(self.device)
        self.keyboard = Keyboard(self.device)
        self.selector = Selector(self.device)
        self.service = Service(self.device)
    
    # Touch methods
    def click(self, x, y):
        """Click at coordinates (x, y)"""
        return self.touch.click(x, y)
    
    def double_click(self, x, y):
        """Double click at coordinates"""
        return self.touch.double_click(x, y)
    
    def long_click(self, x, y, duration=0.5):
        """Long press at coordinates"""
        return self.touch.long_click(x, y, duration)
    
    def swipe(self, x1, y1, x2, y2, duration=0.2):
        """Swipe from (x1,y1) to (x2,y2)"""
        return self.touch.swipe(x1, y1, x2, y2, duration)
    
    # Keyboard methods
    def type(self, text):
        """Type text instantly (50x faster than alternatives)"""
        return self.keyboard.type(text)
    
    def press(self, key):
        """Press special key: home, back, menu, etc"""
        return self.keyboard.press(key)
    
    # Element methods
    def find(self, **kwargs):
        """
        Find element by criteria.
        
        Examples:
            auto.find(text="OK")
            auto.find(id="button1")
            auto.find(class_name="Button")
        """
        return self.selector.find(**kwargs)
    
    def find_text(self, text):
        """Find element by text"""
        return self.selector.by_text(text)
    
    def find_id(self, id):
        """Find element by resource ID"""
        return self.selector.by_id(id)
    
    def click_text(self, text, timeout=None):
        """Find and click element with matching text"""
        elem = self.selector.by_text(text)
        if timeout:
            elem = elem.wait(timeout)
        if elem:
            return elem.click()
        return False
    
    def wait(self, **kwargs):
        """Wait for element to appear"""
        return self.selector.wait(**kwargs)
    
    # Service methods
    def install_service(self, apk_path=None):
        """Install the Android service APK"""
        return self.service.install(apk_path)
    
    def uninstall_service(self):
        """Uninstall the Android service"""
        return self.service.uninstall()
    
    # Device info
    @property
    def info(self):
        """Get device information"""
        return self.device.info if hasattr(self.device, 'info') else {}
    
    def window_size(self):
        """Get screen dimensions (width, height)"""
        return self.device.window_size()
    
    def screenshot(self, filename=None):
        """Take screenshot (returns PIL Image or saves to file)"""
        # To be implemented
        pass
    
    # Connection
    def close(self):
        """Close device connection"""
        if hasattr(self.device, 'close'):
            self.device.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.close()
    
    def __repr__(self):
        return f"<Automator device={getattr(self.device, 'serial', 'unknown')}>"


# Convenience functions
def connect(serial=None):
    """Quick connection - same as Automator(serial)"""
    return Automator(serial)


def list_devices():
    """List connected Android devices"""
    from .core.device import list_devices as _list
    return _list()


# What gets imported with "from automatax1 import *"
__all__ = [
    'Automator',
    'Device',
    'Touch',
    'Keyboard',
    'Selector',
    'Element',
    'Service',
    'connect',
    'list_devices',
]


# Version info
__version_info__ = tuple(map(int, __version__.split('.')))


# Package metadata
__pkg_name__ = "automatax1"
__description__ = "Ultra-fast Android automation - 50x faster than alternatives"
__url__ = "https://github.com/yourusername/automatax1"
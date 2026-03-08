"""Keyboard input simulation"""

class Keyboard:
    """Handle text input"""
    
    def __init__(self, device):
        self.device = device
    
    def type(self, text):
        """Type text instantly"""
        print(f"Type: {text}")
        return True
    
    def press(self, key):
        """Press special key (home, back, etc)"""
        print(f"Press: {key}")
        return True
"""Keyboard event simulation"""

class Keyboard:
    """Handles keyboard input"""
    
    def __init__(self, device):
        self.device = device
        
    def press_key(self, key):
        """Press a single key"""
        print(f"Press key: {key}")
        return True
    
    def type_slow(self, text):
        """Type text slowly (key by key)"""
        print(f"Typing slowly: {text}")
        return True
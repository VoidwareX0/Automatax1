"""Clipboard management"""

class Clipboard:
    """Handle copy/paste operations"""
    
    def __init__(self, device):
        self.device = device
        self._content = ""
        
    def copy(self, text):
        """Copy text to clipboard"""
        self._content = text
        print(f"Copied to clipboard: {text[:30]}...")
        return True
    
    def paste(self):
        """Paste from clipboard"""
        print(f"Pasted: {self._content[:30]}...")
        return self._content
    
    def clear(self):
        """Clear clipboard"""
        self._content = ""
        return True
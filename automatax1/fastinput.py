"""Ultra-fast text input engine"""

class FastInput:
    """Direct text injection for instant typing"""
    
    def __init__(self, device):
        self.device = device
        
    def type(self, text):
        """Type text INSTANTLY (not simulated)"""
        print(f"⚡ Fast typing: {text}")
        # This will eventually use direct AccessibilityService injection
        return True
    
    def type_secret(self, text):
        """Type without logging (for passwords)"""
        print("⚡ Typing [hidden]")
        return True
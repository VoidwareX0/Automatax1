"""Touch and gesture simulation"""

class Touch:
    """Handle touch interactions"""
    
    def __init__(self, device):
        self.device = device
    
    def click(self, x, y):
        """Click at coordinates"""
        print(f"Click at ({x}, {y})")
        return True
    
    def double_click(self, x, y):
        """Double click at coordinates"""
        self.click(x, y)
        self.click(x, y)
        return True
    
    def long_click(self, x, y, duration=0.5):
        """Long press at coordinates"""
        print(f"Long click at ({x}, {y}) for {duration}s")
        return True
    
    def swipe(self, x1, y1, x2, y2, duration=0.2):
        """Swipe gesture"""
        print(f"Swipe from ({x1},{y1}) to ({x2},{y2})")
        return True
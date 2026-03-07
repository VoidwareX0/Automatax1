"""Touch and gesture simulation"""

class Touch:
    """Handles all touch interactions"""
    
    def __init__(self, device):
        self.device = device
        
    def click(self, x, y):
        """Click at coordinates"""
        print(f"Click at ({x}, {y})")
        return True
    
    def double_click(self, x, y):
        """Double click"""
        return self.click(x, y) and self.click(x, y)
    
    def swipe(self, x1, y1, x2, y2, duration=100):
        """Swipe gesture"""
        print(f"Swipe from ({x1},{y1}) to ({x2},{y2})")
        return True
    
    def long_press(self, x, y, duration=500):
        """Long press"""
        print(f"Long press at ({x},{y}) for {duration}ms")
        return True
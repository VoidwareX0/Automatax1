"""Element selection and finding"""

class Element:
    """UI Element with actions"""
    
    def __init__(self, device, selector):
        self.device = device
        self.selector = selector
        self._exists = False
    
    @property
    def exists(self):
        """Check if element exists"""
        return self._exists
    
    def click(self):
        """Click the element"""
        if self.exists:
            print(f"Click element: {self.selector}")
            return True
        return False
    
    def text(self):
        """Get element text"""
        return None
    
    def wait(self, timeout=10.0):
        """Wait for element to appear"""
        import time
        deadline = time.time() + timeout
        while time.time() < deadline:
            if self.exists:
                return self
            time.sleep(0.1)
        return None

class Selector:
    """Find UI elements"""
    
    def __init__(self, device):
        self.device = device
    
    def by_text(self, text):
        """Find element by text"""
        return Element(self.device, {'text': text})
    
    def by_id(self, id):
        """Find element by resource ID"""
        return Element(self.device, {'resource-id': id})
    
    def by_class(self, class_name):
        """Find element by class name"""
        return Element(self.device, {'class': class_name})
    
    def find(self, **kwargs):
        """Find element by criteria"""
        if 'text' in kwargs:
            return self.by_text(kwargs['text'])
        if 'id' in kwargs:
            return self.by_id(kwargs['id'])
        if 'class_name' in kwargs:
            return self.by_class(kwargs['class_name'])
        return None
    
    def wait(self, **kwargs):
        """Wait for element to appear"""
        elem = self.find(**kwargs)
        if elem:
            return elem.wait(kwargs.get('timeout', 10))
        return None
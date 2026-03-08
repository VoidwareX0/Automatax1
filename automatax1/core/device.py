"""Device connection and management"""
import socket
import subprocess
from typing import Optional, Tuple

class Device:
    """Android device connection"""
    
    def __init__(self, serial: Optional[str] = None):
        self.serial = serial
        self.sock: Optional[socket.socket] = None
        self._connect()
    
    def _connect(self) -> bool:
        """Establish connection to device"""
        try:
            # ADB forward
            cmd = ['adb', 'forward', 'tcp:17384', 'localabstract:automatax1']
            if self.serial:
                cmd = ['adb', '-s', self.serial, 'forward', 'tcp:17384', 'localabstract:automatax1']
            subprocess.run(cmd, check=True)
            
            # Connect socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('127.0.0.1', 17384))
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def window_size(self) -> Tuple[int, int]:
        """Get screen dimensions"""
        # To be implemented
        return (1080, 2400)
    
    def close(self):
        """Close connection"""
        if self.sock:
            self.sock.close()
            self.sock = None
"""Android service management"""
import subprocess
from pathlib import Path
from typing import Optional

class Service:
    """Manage automatax1 Android service"""
    
    def __init__(self, device):
        self.device = device
    
    def install(self, apk_path: Optional[Path] = None):
        """Install the Android service APK"""
        if not apk_path:
            # Get from package resources
            import pkg_resources
            apk_path = Path(pkg_resources.resource_filename('automatax1', 'assets/automatax1.apk'))
        
        cmd = ['adb', 'install', '-r', str(apk_path)]
        if self.device.serial:
            cmd = ['adb', '-s', self.device.serial, 'install', '-r', str(apk_path)]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Install failed: {result.stderr}")
        
        print(f"✅ Service installed: {apk_path}")
    
    def uninstall(self):
        """Remove the Android service"""
        cmd = ['adb', 'uninstall', 'com.automatax1']
        if self.device.serial:
            cmd = ['adb', '-s', self.device.serial, 'uninstall', 'com.automatax1']
        
        subprocess.run(cmd, capture_output=True)
        print("✅ Service uninstalled")
    
    def is_running(self) -> bool:
        """Check if service is running"""
        # To be implemented
        return True
    
    def start(self):
        """Start the service"""
        # To be implemented
        pass
    
    def stop(self):
        """Stop the service"""
        # To be implemented
        pass
"""ADB communication layer"""

import subprocess

class Adb:
    """Handle ADB commands"""
    
    def __init__(self, device_id=None):
        self.device_id = device_id
        
    def _cmd(self, *args):
        """Execute ADB command"""
        cmd = ['adb']
        if self.device_id:
            cmd.extend(['-s', self.device_id])
        cmd.extend(args)
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()
    
    def forward(self, local, remote):
        """Forward port"""
        return self._cmd('forward', local, remote)
    
    def shell(self, command):
        """Execute shell command"""
        return self._cmd('shell', command)
    
    def devices(self):
        """List connected devices"""
        output = self._cmd('devices')
        return [line.split()[0] for line in output.split('\n')[1:] if 'device' in line]
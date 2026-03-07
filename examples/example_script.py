#!/usr/bin/env python3
"""Example usage of automatax1"""

import automatax1 as a1

def main():
    # Initialize
    auto = a1.Automator()
    
    # Get device info
    print(f"Device: {auto.device}")
    
    # Perform actions
    auto.click(500, 600)
    auto.type("Hello from automatax1!")
    auto.swipe(100, 200, 300, 400)
    
    # Copy/paste
    auto.copy("Secret text")
    pasted = auto.paste()
    print(f"Pasted: {pasted}")

if __name__ == "__main__":
    main()
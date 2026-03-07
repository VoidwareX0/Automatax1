"""Basic tests for automatax1"""

import automatax1 as a1

def test_import():
    """Test package imports"""
    assert hasattr(a1, 'Automator')
    assert hasattr(a1, 'Device')
    assert hasattr(a1, 'Touch')
    print("✅ Import test passed")

def test_automator():
    """Test Automator class"""
    auto = a1.Automator()
    assert auto.click(100, 200) == True
    assert auto.type("test") == True
    print("✅ Automator test passed")

if __name__ == "__main__":
    test_import()
    test_automator()
    print("\n✅ All tests passed!")
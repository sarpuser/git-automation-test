# test_hello.py
from pkg.module import helloWorld

def testHelloWorld():
    """Test that helloWorld returns the correct string."""
    expected = "hello world"
    actual = helloWorld()
    assert actual == expected

def testHelloWorldType():
    """Test that helloWorld returns a string."""
    result = helloWorld()
    assert isinstance(result, str)
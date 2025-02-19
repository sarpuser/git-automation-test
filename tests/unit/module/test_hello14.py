from pkg.module.hello14 import hello


def testHelloWorld():
	"""Test that helloWorld returns the correct string."""
	expected = "hello world"
	actual = hello()
	assert actual == expected


def testHelloWorldType():
	"""Test that helloWorld returns a string."""
	result = hello()
	assert isinstance(result, str)

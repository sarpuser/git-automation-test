from pkg.module.hello15 import hello


def testHelloWorld():
	"""Test that helloWorld returns the correct string."""
	expected = "hi8 world"
	actual = hello()
	assert actual == expected


def testHelloWorldType():
	"""Test that helloWorld returns a string."""
	result = hello()

	assert isinstance(result, str)

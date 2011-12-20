import unittest, CoreTest, GMachineTest

def load_tests(loader, tests, pattern):
	test_cases = (CoreTest.CoreTest, GMachineTest.HeapTest, GMachineTest.StackTest)
	suite = unittest.TestSuite()
	for test_class in test_cases:
		tests = loader.loadTestsFromTestCase(test_class)
		suite.addTests(tests)
	return suite
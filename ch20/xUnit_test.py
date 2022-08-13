from xUnit import TestCase
from xUnit import WasRun

class TestCaseTest(TestCase):
  def setUp(self):
    self.test = WasRun("testMethod")
    
  def testTemplateMethod(self):
    test = WasRun("testMethod")
    test.run()
    assert("setUp testMethod tearDown " == test.log)
    
TestCaseTest("testTemplateMethod").run()
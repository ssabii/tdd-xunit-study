class TestCase:
  def __init__(self, name):
    self.name = name
  
  def setUp(self):
    pass
    
  def run(self):
    result = TestResult()
    result.testStarted()
    self.setUp()
    try:
      method = getattr(self, self.name)
      method()
    except:
      result.testFailed()
    self.tearDown()
    return result
    
  def tearDown(self):
    pass
  
class TestResult:
  def __init__(self):
    self.runCount = 0
    self.failureCount = 0
  
  def testStarted(self):
    self.runCount = self.runCount + 1
    
  def testFailed(self):
    self.failureCount = self.failureCount + 1
    
  def summary(self):
    return "%d run, %d failed" % (self.runCount, self.failureCount)
  
class WasRun(TestCase):
  def __init__(self, name):
    TestCase.__init__(self, name)
    
  def setUp(self):
    self.log = "setUp "
    
  def testMethod(self):
    self.log = self.log + "testMethod "
  
  def tearDown(self):
    self.log = self.log + "tearDown "
    
  def testBrokenMethod(self):
    raise Exception

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import core as coreApi

ec2_id='i-019ebfaf92631c228'
serviceName='nodejs-restart'

class ec2Tests(unittest.TestCase):

  def testkillServiceOrProcess(self):
    item = {
      'id': ec2_id,
      'serviceName': serviceName
    }
    
    print item
    coreApi.killServiceOrProcess(item)
    
def main():
  unittest.main()

if __name__ == '__main__':
  main()

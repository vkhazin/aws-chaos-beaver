import unittest
import sys
import os
from time import sleep
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chalicelib import utils
from chalicelib import core as coreApi
import lambdaHandler

nodeJsInstanceId='i-0b314f9c31a99621c'
serviceName='nodejs-restart'
processName='node'
nodeJsPortNumber=3000

class ec2Tests(unittest.TestCase):

  def testRemovePort(self):
    payload = {
      'method': 'delete',
      'path': '/port',
      'body': {
        'instanceId': nodeJsInstanceId,
        'osType': 'Linux',
        'portNumber': nodeJsPortNumber
      }
    }
    result = lambdaHandler.handler(payload)
    print(json.dumps(result, default=utils.jsonSerializer))

def main():
  unittest.main()

if __name__ == '__main__':
  main()

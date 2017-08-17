import unittest
from lib import utils
import json
from time import sleep
from lib import core as coreApi
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
    result = lambdaHandler.handler(payload, None)

def main():
  unittest.main()

if __name__ == '__main__':
  main()

import unittest
import json
from time import sleep
import sys
import os
from time import sleep
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib import utils
from lib import core as coreApi
import lambdaHandler

nodeJsInstanceId='i-0b314f9c31a99621c'
nodeJsServiceName='nodejs-restart'
processName='node'
nodeJsPortNumber=3000

class ec2Tests(unittest.TestCase):

  def testDescribeInstance(self):
    payload = {
      'method': 'GET',
      'path': '/instance/' + nodeJsInstanceId + ',' + nodeJsInstanceId
    }
    result = lambdaHandler.handler(payload, None)

  def testStopService(self):
    payload = {
      'method': 'delete',
      'path': '/service',
      'body': {
        'instanceId': nodeJsInstanceId,
        'osType': 'Linux',
        'serviceName': nodeJsServiceName
      }
    }
    result = lambdaHandler.handler(payload, None)

  def testKillProcessByName(self):
    payload = {
      'method': 'delete',
      'path': '/process',
      'body': {
        'instanceId': nodeJsInstanceId,
        'osType': 'Linux',
        'processName': processName
      }
    }
    result = lambdaHandler.handler(payload, None)

  def testKillProcessByPortNumber(self):
    payload = {
      'method': 'delete',
      'path': '/process',
      'body': {
        'instanceId': nodeJsInstanceId,
        'osType': 'Linux',
        'portNumber': nodeJsPortNumber
      }
    }
    result = lambdaHandler.handler(payload, None)

  def testKillProcessByNameAndPortNumber(self):
    payload = {
      'method': 'delete',
      'path': '/process',
      'body': {
        'instanceId': nodeJsInstanceId,
        'osType': 'Linux',
        'processName': processName,
        'portNumber': nodeJsPortNumber
      }
    }
    result = lambdaHandler.handler(payload, None)
    
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

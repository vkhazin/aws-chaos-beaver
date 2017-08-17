import unittest
import sys
import os
from time import sleep
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib import utils
from lib import core as coreApi

nodeJsInstanceId='i-0b314f9c31a99621c'
serviceName='nodejs-restart'
processName='node'
nodeJsPortNumber=3000

redisOnLinuxInstanceId='i-0c7ac0aa037e4aa82'
redisOnLinuxServiceName='nodejs-restart'

class ec2Tests(unittest.TestCase):

#   def testSsmDescribeInstances(self):
#     print (coreApi.ssmDescribeInstances([redisOnLinuxInstanceId]))
        
#   def testStopService(self):
#     item = {
#       'id': nodeJsInstanceId,
#       'serviceName': serviceName
#     }
#     coreApi.killServiceOrProcess(item)

#   def testKillProcessByName(self):
#     ssmApi.restartService([nodeJsInstanceId], serviceName)
#     sleep(.5)
#     item = {
#       'id': nodeJsInstanceId,
#       'processName': processName
#     }
#     coreApi.killServiceOrProcess(item)

#   def testKillProcessByPortNumber(self):
#     ssmApi.restartService([nodeJsInstanceId], serviceName)
#     sleep(.5)
#     item = {
#       'id': nodeJsInstanceId,
#       'portNumber': portNumber
#     }
#     coreApi.killServiceOrProcess(item)

#   def testKillProcessByNameAndPortNumber(self):
#     ssmApi.restartService([nodeJsInstanceId], serviceName)
#     sleep(.5)
#     item = {
#       'id': nodeJsInstanceId,
#       'processName': processName,
#       'portNumber': portNumber
#     }
#     coreApi.killServiceOrProcess(item)

#   def testMissingInstanceId(self):
#     ssmApi.restartService([nodeJsInstanceId], serviceName)
#     sleep(.5)
#     item = {
#       'processName': processName
#     }
    
#     try:
#       coreApi.killServiceOrProcess(item)
#     except BadRequestError as ex:
#       print ex
      
#   def testMissingParameters(self):
#     ssmApi.restartService([nodeJsInstanceId], serviceName)
#     sleep(.5)
#     item = {
#       'id': nodeJsInstanceId
#     }
#     try:
#       coreApi.killServiceOrProcess(item)
#     except BadRequestError as ex:
#       print ex

  def testRemovePort(self):
    try:
      item = {
        'id': nodeJsInstanceId,
        'osType': 'Linux',
        'portNumber': nodeJsPortNumber
      }
      result = coreApi.removePort(item)
      print(json.dumps(result, default=utils.jsonSerializer))
    except Exception as ex:
      print ex

def main():
  unittest.main()

if __name__ == '__main__':
  main()

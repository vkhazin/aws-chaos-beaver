import unittest
import sys
import os
from time import sleep
from chalice import BadRequestError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chalicelib import core as coreApi
from chalicelib import ssm as ssmApi

ec2_id='i-019ebfaf92631c228'
serviceName='nodejs-restart'
processName='node'
portNumber=3000

redisOnLinuxInstanceId='i-0c7ac0aa037e4aa82'
redisOnLinuxServiceName='nodejs-restart'

class ec2Tests(unittest.TestCase):

  def testSsmDescribeInstances(self):
    print (coreApi.ssmDescribeInstances([redisOnLinuxInstanceId]))
        
#   def testStopService(self):
#     item = {
#       'id': ec2_id,
#       'serviceName': serviceName
#     }
#     coreApi.killServiceOrProcess(item)

#   def testKillProcessByName(self):
#     ssmApi.restartService([ec2_id], serviceName)
#     sleep(.5)
#     item = {
#       'id': ec2_id,
#       'processName': processName
#     }
#     coreApi.killServiceOrProcess(item)

#   def testKillProcessByPortNumber(self):
#     ssmApi.restartService([ec2_id], serviceName)
#     sleep(.5)
#     item = {
#       'id': ec2_id,
#       'portNumber': portNumber
#     }
#     coreApi.killServiceOrProcess(item)

#   def testKillProcessByNameAndPortNumber(self):
#     ssmApi.restartService([ec2_id], serviceName)
#     sleep(.5)
#     item = {
#       'id': ec2_id,
#       'processName': processName,
#       'portNumber': portNumber
#     }
#     coreApi.killServiceOrProcess(item)

#   def testMissingInstanceId(self):
#     ssmApi.restartService([ec2_id], serviceName)
#     sleep(.5)
#     item = {
#       'processName': processName
#     }
    
#     try:
#       coreApi.killServiceOrProcess(item)
#     except BadRequestError as ex:
#       print ex
      
#   def testMissingParameters(self):
#     ssmApi.restartService([ec2_id], serviceName)
#     sleep(.5)
#     item = {
#       'id': ec2_id
#     }
#     try:
#       coreApi.killServiceOrProcess(item)
#     except BadRequestError as ex:
#       print ex
    
def main():
  unittest.main()

if __name__ == '__main__':
  main()

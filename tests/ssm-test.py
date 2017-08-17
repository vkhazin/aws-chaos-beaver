import json
import unittest
from lib import ssm as ssmApi
from lib import utils

redisOnLinuxInstanceId='i-0c7ac0aa037e4aa82'

nodeJsOnLinuxInstanceId='i-0b314f9c31a99621c'
nodeJsLinuxServiceName='nodejs-restart'
nodeJsOnLinuxPortNumber=3000

mssqlInstanceId='i-0738d627d80a76421'
msSqlOnWinServiceName='mssqlserver'

class ec2Tests(unittest.TestCase):

#   def testStopRedisServerOnLinux(self):
#     result = ssmApi.stopService(ssmApi.ShellType.Linux, [redisOnLinuxInstanceId], redisOnLinuxServiceName)
#     self.assertIsNotNone(result)

#   def testRestartRedisServerOnLinux(self):
#     result = ssmApi.restartService(ssmApi.ShellType.Linux, [redisOnLinuxInstanceId], redisOnLinuxServiceName)
#     self.assertIsNotNone(result)

#   def testStopMsSqlServerOnWin(self):
#     result = ssmApi.stopService(ssmApi.ShellType.Win, [mssqlInstanceId], msSqlOnWinServiceName)
#     self.assertIsNotNone(result)    

#   def testDescribeInstances(self):
#     result = ssmApi.describeInstances([redisOnLinuxInstanceId])
# #     print result
#     self.assertGreater(len(result), 0, 'No information found')  

  def testDescribeInstances(self):
    result = ssmApi.removePort(ssmApi.ShellType.Linux, [nodeJsOnLinuxInstanceId], nodeJsOnLinuxPortNumber)
    print(json.dumps(result, default=utils.jsonSerializer))
#     self.assertGreater(len(result), 0, 'No information found')  

def main():
  unittest.main()

if __name__ == '__main__':
  main()

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chalicelib import ssm as ssmApi

redisOnLinuxInstanceId='i-0c7ac0aa037e4aa82'
redisOnLinuxServiceName='nodejs-restart'

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

  def testDescribeInstances(self):
    result = ssmApi.describeInstances([redisOnLinuxInstanceId])
#     print result
    self.assertGreater(len(result), 0, 'No information found')  
    
def main():
  unittest.main()

if __name__ == '__main__':
  main()

from lib import utils
from lib import ssm

def killServiceOrProcess(item):
  item = processInput(item)
  instanceId = item.get('instanceId')
  shellType = item.get('shellType')
  serviceName = item.get('serviceName')
  processName = item.get('processName')
  portNumber = item.get('portNumber')
  
  if (serviceName is not None):
    result = ssm.stopService(shellType, [instanceId], serviceName)
  elif (processName is not None and portNumber is None):
    result = ssm.killProcessByName(shellType, [instanceId], processName)
  elif (portNumber is not None and processName is None):
    result = ssm.killProcessByPortNumber(shellType, [instanceId], portNumber)
  elif (processName is not None and portNumber is not None):
    result = ssm.killProcessByNameAndPortNumber(shellType, [instanceId], processName, portNumber)
  else:
    raise Exception('serviceName, processName, and portNumber are empty! Sorry, do not know what to kill other than self!')

  return result
    
def ssmDescribeInstances(instanceIds):
  result = ssm.describeInstances(instanceIds)
  return result

def removePort(item):
  item = processInput(item)
  instanceId = item.get('instanceId')
  shellType = item.get('shellType')
  portNumber = item.get('portNumber')
  if (portNumber is None):
    raise Exception('portNumber is empty!')
  return ssm.removePort(shellType, [instanceId], portNumber)  
  
  
def processInput(item):
  instanceId = item.get('instanceId')
  if (instanceId is None):
    raise Exception('instanceId is empty')
    
  osType = item.get('osType')
  if (osType.lower() == 'linux'):
    item['shellType'] = ssm.ShellType.Linux
  elif (osType.lower() == 'win'):
    item['shellType'] = ssm.ShellType.Win
  else:
    raise Exception('osType invalid or is empty')  
    
  return item
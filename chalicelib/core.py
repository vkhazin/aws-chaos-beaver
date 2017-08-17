from chalicelib import ssm
from chalice import BadRequestError

def killServiceOrProcess(item):
  item = processInput(item)
  instanceId = item.get('instanceId')
  shellType = item.get('shellType')
  serviceName = item.get('serviceName')
  processName = item.get('processName')
  portNumber = item.get('portNumber')
  
  if (serviceName is not None):
    ssm.stopService(shellType, [instanceId], serviceName)
  elif (processName is not None and portNumber is None):
    ssm.killProcessByName(shellType, [instanceId], processName)
  elif (portNumber is not None and processName is None):
    ssm.killProcessByPortNumber(shellType, [instanceId], portNumber)
  elif (processName is not None and portNumber is not None):
    ssm.killProcessByNameAndPortNumber(shellType, [instanceId], processName, portNumber)
  else:
    raise BadRequestError('serviceName, processName, and portNumber are empty! Sorry, do not know what to kill other than self!')
    
def ssmDescribeInstances(instanceIds):
  result = ssm.describeInstances(instanceIds)
  return result

def removePort(item):
  item = processInput(item)
  instanceId = item.get('instanceId')
  shellType = item.get('shellType')
  portNumber = item.get('portNumber')
  if (portNumber is None):
    raise BadRequestError('portNumber is empty!')
  return ssm.removePort(shellType, [instanceId], portNumber)  
  
  
def processInput(item):
  instanceId = item.get('instanceId')
  if (instanceId is None):
    raise BadRequestError('instanceId is empty')
    
  osType = item.get('osType')
  if (osType.lower() == 'linux'):
    item['shellType'] = ssm.ShellType.Linux
  elif (osType.lower() == 'win'):
    item['shellType'] = ssm.ShellType.Win
  else:
    raise BadRequestError('osType invalid or is empty')  
    
  return item
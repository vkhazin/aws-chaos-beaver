from chalicelib import ssm
from chalice import BadRequestError

def killServiceOrProcess(item):
  
  instanceId = item.get('id')
  if (instanceId is None):
    raise BadRequestError('instanceId is empty')
    
  osType = item.get('osType')
  if (osType.lower() == 'linux'):
    shellType = ssm.ShellType.Linux
  elif (osType.lower() == 'win'):
    shellType = ssm.ShellType.Win
  else:
    raise BadRequestError('osType invalid or is empty')
    
  serviceName = item.get('serviceName')
  processName = item.get('processName')
  portNumber = item.get('portNumber')
  
  if (serviceName is not None):
    ssm.stopService([instanceId], serviceName)
  elif (processName is not None and portNumber is None):
    ssm.killProcessByName([instanceId], processName)
  elif (portNumber is not None and processName is None):
    ssm.killProcessByPortNumber([instanceId], portNumber)
  elif (processName is not None and portNumber is not None):
    ssm.killProcessByNameAndPortNumber([instanceId], processName, portNumber)
  else:
    raise BadRequestError('serviceName, processName, and portNumbers are empty! Sorry, do not know what to kill other than self!')
    
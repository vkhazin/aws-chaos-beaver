from chalicelib import ssm

def killServiceOrProcess(item):
  instanceId = item.get('id')
  serviceName = item.get('serviceName')
  processName = item.get('processName')
  portNumber = item.get('portNumber')
  if (serviceName is not None):
    ssm.stopService([instanceId], serviceName)
  else:
    ssm.killProcessByNameAndPortNumber([instanceId], processName, portNumber)
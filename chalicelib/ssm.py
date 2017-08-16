import os
import boto3
from enum import Enum

client = boto3.client(
    'ssm'
)

class ShellType(Enum):
  Linux   = 'AWS-RunShellScript'
  Win     = 'AWS-RunPowerShellScript'

def sendCommand(shellType, instanceIds, command):
  response = client.send_command(
      InstanceIds=instanceIds,
      DocumentName=shellType.value,
      TimeoutSeconds=60,
      Parameters={
          'commands': [
              command,
          ]
      }
  )
  return response

def restartService(shellType, instanceIds, serviceName):
  if (shellType == ShellType.Linux):
    command = 'service {serviceName} restart'.format(serviceName=serviceName)
  elif (shellType == ShellType.Win):
    command = 'Restart-Service  {serviceName} -force'.format(serviceName=serviceName)
  else:
    raise Exception('Unknown shell type')
  return sendCommand(shellType, instanceIds, command)

def stopService(shellType, instanceIds, serviceName):  
  if (shellType == ShellType.Linux):
    command = 'service {serviceName} stop'.format(serviceName=serviceName)
  elif (shellType == ShellType.Win):
    command = 'Stop-Service  {serviceName} -force'.format(serviceName=serviceName)
  else:
    raise Exception('Unknown shell type')
  
  return sendCommand(shellType, instanceIds, command)

def killProcessByNameAndPortNumber(shellType, instanceIds, processName, portNumber):
  if (shellType == ShellType.Linux):
    # ss documentation: http://man7.org/linux/man-pages/man8/ss.8.html
    command = "kill -9 $(ps -p $(ss -lpn 'sport = :{portNumber}'  | grep '(?<=pid=)(\d*)(?=,)' -Po) | grep '{processName}' | awk '{{print $1}}')" \
              .format(portNumber=portNumber, processName=processName)
  elif (shellType == ShellType.Win):
    raise Exception('Not implemented')
  else:
    raise Exception('Unknown shell type')

  return sendCommand(shellType, instanceIds, command)

def killProcessByPortNumber(shellType, instanceIds, portNumber):
  if (shellType == ShellType.Linux):
   command = "kill -9 $(ss -lpn 'sport = :{portNumber}' | grep '(?<=pid=)(\d*)(?=,)' -Po)".format(portNumber=portNumber)
  elif (shellType == ShellType.Win):
    raise Exception('Not implemented')
  else:
    raise Exception('Unknown shell type')  
  
  return sendCommand(shellType, instanceIds, command)

def killProcessByName(shellType, instanceIds, processName):
  if (shellType == ShellType.Linux):
   command = "kill -9 $(pgrep {processName})".format(processName=processName)
  elif (shellType == ShellType.Win):
    raise Exception('Not implemented')
  else:
    raise Exception('Unknown shell type')  
  
  return sendCommand(shellType, instanceIds, command)

def describeInstances(instanceIds):
  response = client.describe_instance_information(
      InstanceInformationFilterList = [
        {
            'key': 'InstanceIds',
            'valueSet': instanceIds
        },
      ]
  )
  return response['InstanceInformationList']

def removePort(shellType, instanceIds, portNumber):
  if (shellType == ShellType.Linux):
    command = "firewall-cmd --zone=public --remove-port={portNumber}/tcp".format(portNumber=portNumber)  
  elif (shellType == ShellType.Win):
    raise Exception('Not implemented')
  else:
    raise Exception('Unknown shell type')  
#   print shellType.value
  return sendCommand(shellType, instanceIds, command)  
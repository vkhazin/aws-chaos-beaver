import os
import boto3

client = boto3.client(
    'ssm'
)

def sendCommand(instanceIds, command):
  response = client.send_command(
      InstanceIds=instanceIds,
      DocumentName='AWS-RunShellScript',
      TimeoutSeconds=60,
      Parameters={
          'commands': [
              command,
          ]
      }
  )  
  return response

def stopService(instanceIds, serviceName):
  command = 'service {serviceName} stop'.format(serviceName=serviceName)
  return sendCommand(instanceIds, command)

def killProcessByNameAndPortNumber(instanceIds, processName, portNumber):
  command = "kill $(ss -lptn 'sport = :{portNumber}' | grep '(?<=pid=)(\d*)(?=,)' -Po)".format(portNumber=portNumber)
  return sendCommand(instanceIds, command)

# def killProcessByNameAndPortNumber(instanceIds, portNumber):
#   command = "kill $(ss -lptn 'sport = :{portNumber}' | grep '(?<=pid=)(\d*)(?=,)' -Po)".format(portNumber=portNumber)
#   return sendCommand(instanceIds, command)
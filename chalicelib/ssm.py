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

def restartService(instanceIds, serviceName):
  command = 'service {serviceName} restart'.format(serviceName=serviceName)
  return sendCommand(instanceIds, command)

def stopService(instanceIds, serviceName):
  command = 'service {serviceName} stop'.format(serviceName=serviceName)
  return sendCommand(instanceIds, command)

def killProcessByNameAndPortNumber(instanceIds, processName, portNumber):
  # ss documentation: http://man7.org/linux/man-pages/man8/ss.8.html
  # ps -p $(ss -lpn 'sport = :3000'  | grep '(?<=pid=)(\d*)(?=,)' -Po) | grep 'node'
  # kill $(ps -p $(ss -lpn 'sport = :3000'  | grep '(?<=pid=)(\d*)(?=,)' -Po) | grep 'node' | awk '{print $1}')
  #command = "kill -9 $(ss -lpn 'sport = :{portNumber}' | grep '(?<=pid=)(\d*)(?=,)' -Po)".format(portNumber=portNumber)
  command = "kill -9 $(ps -p $(ss -lpn 'sport = :{portNumber}'  | grep '(?<=pid=)(\d*)(?=,)' -Po) | grep '{processName}' | awk '{{print $1}}')" \
            .format(portNumber=portNumber, processName=processName)
  return sendCommand(instanceIds, command)

def killProcessByPortNumber(instanceIds, portNumber):
  command = "kill -9 $(ss -lpn 'sport = :{portNumber}' | grep '(?<=pid=)(\d*)(?=,)' -Po)".format(portNumber=portNumber)
  return sendCommand(instanceIds, command)

def killProcessByName(instanceIds, processName):
  command = "kill -9 $(pgrep {processName})".format(processName=processName)
  return sendCommand(instanceIds, command)
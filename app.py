from chalicelib import core
import datetime
from chalice import Chalice
from chalice import BadRequestError
from chalice import ChaliceViewError

appName = 'smith-poc-chaos-beaver'
app = Chalice(app_name=appName)
# app.debug = True

@app.route('/')
def echo():
    return {
      'name': appName,
      'author': 'Vlad Khazin <vladimir.khazin@icssolutions.ca',
      'version': '1.0.0',
      'description': 'Shutdown processes/services on ec2 instances to simulate failures'
    }

@app.route('/', methods=['POST'])
def killServiceOrProcess():
  try:
    startTime = datetime.datetime.now()
    body = app.current_request.json_body
    for item in body:
      core.killServiceOrProcess(item);
    timeTaken = datetime.datetime.now() - startTime
    return {
      'request': body,
      'executionTime': timeTaken.microseconds / 1000
    }
  except BadRequestError as ex:
    app.log.error(ex)
    raise
  except Exception as ex:
    app.log.error(ex)
    raise ChaliceViewError(str(ex))

from lib import utils
from lib import core as coreApi

def handler(event, context):
    method = event['method'].lower()
    path = event['path'].lower()
    if 'body' in event:
      body = event['body']
    
    if (method == 'delete' and path == '/port'):
      result = coreApi.removePort(body);
    elif (method == 'delete' and path == '/service'):
      result = coreApi.killServiceOrProcess(body);
    elif (method == 'delete' and path == '/process'):
      result = coreApi.killServiceOrProcess(body);
    elif (method == 'get' and path.startswith('/instance/')):
      pathPrefix = '/instance/'
      path = path[len(pathPrefix):]
      instanceIds = path.split(',')
      result = coreApi.ssmDescribeInstances(instanceIds);
    else:
      result = {
        'Error': 'Unknown method and path combination'
      }
      
    result = utils.serialize2Json(result)
    print result
    return result
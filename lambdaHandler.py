from lib import utils
from lib import core as coreApi

def handler(event, context):
    method = event['method'].lower()
    path = event['path'].lower()
    body = event['body']
    
    if (method == 'delete' and path == '/port'):
      result = coreApi.removePort(event['body']);
    elif (method == 'delete' and path == '/service'):
      raise Exception('Not implemented')
    elif (method == 'delete' and path == '/process'):
      raise Exception('Not implemented')
    elif (method == 'get' and path.startswith('/instance') == True):
      raise Exception('Not implemented')
    else:
      result = {
        'Error': 'Unknown method and path combination'
      }
      
    result = utils.serialize2Json(result)
    print result
    return result
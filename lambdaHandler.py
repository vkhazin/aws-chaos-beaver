import unittest
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chalicelib import utils
from chalicelib import core as coreApi

def handler(payload):
    method = payload['method'].lower()
    path = payload['path'].lower()
    body = payload['body']
    
    if (method == 'delete' and path == '/port'):
      result = coreApi.removePort(payload['body']);
      print result
    elif (method == 'delete' and path == '/service'):
      raise Exception('Not implemented')
    elif (method == 'delete' and path == '/process'):
      raise Exception('Not implemented')
    elif (method == 'get' and path.startswith('/instance') == True):
      raise Exception('Not implemented')
    else:
      raise Exception('Unknown method and path combination')
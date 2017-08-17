import datetime
import json

# Append python path
import sys
sys.path.append('./python_modules')

# Solve datetime json serialization
def jsonSerializer(val):
    if isinstance(val, datetime.datetime):
        return val.__str__()
      
def serialize2Json(object):
  return json.dumps(object, default=jsonSerializer)
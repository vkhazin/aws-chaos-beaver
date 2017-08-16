import datetime

# Solve datetime json serialization
def jsonSerializer(val):
    if isinstance(val, datetime.datetime):
        return val.__str__()
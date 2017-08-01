from chalice import Chalice
appName = 'aws-chaos-beaver'

app = Chalice(app_name=appName)


@app.route('/')
def echo():
    return {
      'name': appName,
      'author': 'Vlad Khazin <vladimir.khazin@icssolutions.ca',
      'version': '1.0.0',
      'description': 'Shutdown processes/services on ec2 instances to simulate failures'
    }


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

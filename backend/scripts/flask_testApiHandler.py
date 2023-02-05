
from flask_restful import Api, Resource, reqparse

class flask_testApiHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'it worked ig',
            'message': "hello api handler"
        }
    
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)

        request_type = args['type']
        request_json = args['message']

        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "your message requested: {}".format(ret_msg)
        else:
            message = "no msg"

        final_ret = {"status": "working", "message": message}

        return final_ret
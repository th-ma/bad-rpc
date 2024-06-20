from interfaces import IRpcClient, ITransport
from serializer import Serializer
from errorhandler import ClientErrorHandler


class DreamRpcClient(IRpcClient):

    def __init__(self, transport: ITransport):
        self._transport = transport

    def call_remote_function(self, function_name, *args):
        print(f"DreamRpcClient - call_remote_function - function_name: {function_name}")
        serialized_data = Serializer.serialize(args)
        result = self._transport.send_http_request(function_name, serialized_data)
        deserialized_result = Serializer.deserialize(result)
        checked_result = ClientErrorHandler.check_return_value(deserialized_result)
        return checked_result

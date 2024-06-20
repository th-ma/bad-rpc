from abc import ABC

from interfaces import ITransport
from server import DreamRpcServer


class BadDreamHttp(ITransport):
    def __init__(self, server: DreamRpcServer, endpoint: str = 'http://127.0.0.1:8080/'):
        self.server = server
        self.endpoint = endpoint

    def open_connection(self):
        print(f"BadDreamHttp - open_connection to {self.endpoint}")

    def close_connection(self):
        print(f"BadDreamHttp - close_connection")

    def send_http_request(self, function_name, *args):
        self.open_connection()
        print(f"BadDreamHttp - send_request, fake HTTP POST method")
        response = self.server.handle_http_request(function_name, *args)
        self.close_connection()
        return response

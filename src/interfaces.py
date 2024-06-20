from abc import ABC, abstractmethod


class ITransport(ABC):
    """
        Interface for all transport implementations.
    """
    @abstractmethod
    def open_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def send_http_request(self, function_name, *args):
        pass


class IRpcClient(ABC):
    """
        Interface for all RPC implementations.
    """
    @abstractmethod
    def call_remote_function(self, function_name, *args):
        pass

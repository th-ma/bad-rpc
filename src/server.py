from serializer import Serializer


class DreamRpcServerApplication:
    def __init__(self):
        self.greetings = "Greetings"

    def hello(self) -> str:
        return self.greetings

    def add(self, a: int, b: int) -> int:
        return a + b


class DreamRpcServer:
    def __init__(self):
        self.server_app = DreamRpcServerApplication()

    def handle_http_request(self, function_name: str, *args):
        data = Serializer.deserialize(args)
        print(f"DreamRpcServer - handle_request()")

        if function_name == "hello":
            return Serializer.serialize(self.server_app.hello())
        elif function_name == "add":
            # check args
            if len(*data) == 2:
                return Serializer.serialize(self.server_app.add(data[0][0], data[0][1]))
            else:
                raise ValueError(f"missing arguments")
        else:
            raise ValueError(f"Invalid function name: {function_name}")

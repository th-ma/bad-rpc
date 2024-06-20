from dream_rpc_client import DreamRpcClient
from server import DreamRpcServer
from bad_dream_http import BadDreamHttp


def main():

    function_hello = "hello"
    function_add = "add"
    a = 3
    b = 4

    server = DreamRpcServer()
    transport = BadDreamHttp(server)
    client = DreamRpcClient(transport)

    # remote function call hello()
    print(f"main - Call RPC function: {function_hello}")
    args = ()
    result = client.call_remote_function(function_hello, args)
    print(f"main - {function_hello} returns: {result}")
    print()

    # remote function call add(3, 4)
    print(f"main - Call RPC function: {function_add} with args: {a, b}")
    args = (a, b)
    result = client.call_remote_function(function_add, *args)
    print(f"main - {function_add} returns: {result}")


if __name__ == '__main__':
    main()

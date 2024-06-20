
class ClientErrorHandler:
    @staticmethod
    def check_return_value(data):
        print("ClientErrorHandler - check_return_value")
        if data:
            return data
        else:
            raise ValueError(f"ClientErrorHandler - invalid data received")

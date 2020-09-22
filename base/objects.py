from exceptions import UnnamedMethod


class BaseObject:
    def __init__(self):
        self.object_name = "Base"

    def __str__(self):
        return self.object_name

    def api_request(self, method_name=None):
        if not method_name:
            raise UnnamedMethod("The method_name parameter has not passed")
        pass

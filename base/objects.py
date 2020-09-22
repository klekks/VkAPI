from exceptions import UnnamedMethod, EmptyObjectException
from urls.urls import choose_url


class BaseObject:
    def __init__(self):
        self.name = "Base"

    def __str__(self):
        return self.name

    def api_request(self, method_name=None):
        if not method_name:
            raise UnnamedMethod("The method_name parameter has not passed")
        url = choose_url(self, method_name)
        url += 'v=5.100'
        from requests import get
        print(get('https://api.vk.com/method/' + url).text)

    @property
    def params(self):
        raise EmptyObjectException("The parameter_list method was called but object is empty")

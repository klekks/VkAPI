from base.objects import BaseObject
from random import randint as random_id


class Message(BaseObject):
    def __init__(self, message):
        self.object_name = "Message"
        self.message = message

    def attach(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def send(self):
        self.api_request(method_name="send")

    @property
    def params(self):
        return {
            'message': self.message,
            'access_token': '37f28df12020f0e1b88c9c0480ba69fe5450398eb6966cd1b5f6b7914dfc7dae1239eb3bbdff4a20de44e',
            'domain': 'klekks',
            'random_id': random_id(1, 9999999999999)
        }


Message("message").send()
from base.objects import BaseObject


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

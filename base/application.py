class BaseApplication:
    def __init__(self, sid, secure_key=None, access_token=None):
        self.id = sid
        self.secure_key = secure_key
        self.access_token = access_token
        self.is_authorized = self.authorize()

    def authorize(self):

        return False
class AttributeCanNotBeLoaded(Exception):
    def __init__(self, text):
        self.text = text


class AppAuthorizationException(Exception):
    def __init__(self, text):
        self.text = text


class UrlNotFoundException(Exception):
    def __init__(self, text):
        self.text = text


class UnnamedMethod(Exception):
    def __init__(self, text):
        self.text = text

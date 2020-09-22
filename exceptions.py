class StandardException(Exception):
    def __init__(self, text):
        self.text = text


class AttributeCanNotBeLoaded(StandardException): pass


class AppAuthorizationException(StandardException): pass


class UrlNotFoundException(StandardException): pass


class UnnamedMethod(StandardException): pass


class UrlManagerException(StandardException): pass


class EmptyObjectException(StandardException): pass


class MethodNotFound(StandardException): pass


class ValidationException(StandardException): pass

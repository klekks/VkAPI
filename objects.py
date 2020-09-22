from exceptions import AttributeCanNotBeLoaded


def attribute_is_exist(key):

    return key


class User:
    id = -1
    is_exist = False

    def __init__(self, id=False, data=None):
        if data is None:
            data = {}
        self.data = DataSet(self, data=data)
        self.id = id

    def __class__(self):
        return "User"

    def __getattr__(self, item):
        return self.data.get(item)

    def __getitem__(self, item):
        return self.__getattr__(str(item))


class DataSet:
    last_modified: int
    need_to_update = False
    waiting_for_updates = {}
    from time import time

    def __init__(self, obj, data=None):
        self.object = obj
        self.last_modified = self.modified()
        self.data_set = data

    """
        Метод загружает через API инфорацию о пользователе, востребованную через kwargs
    """
    
    def _api_get(self, *args, **kwargs):
        pass

    def _api_set(self, *args, **kwargs):
        pass
    
    """
        Метод возвращает элемент данных об объекте, востребованный как key. Если аттрибут отсутствует, то метод
        возвращает значение default, если оно было передано, или инициализирует загрузку информации об объекте,
        если default не передан.
    """

    def get(self, key, default=False):
        try:
            return self.data_set[key]
        except KeyError:
            if default:
                return default
            elif key in self.waiting_for_updates.keys():
                return self.waiting_for_updates[key]
            else:
                if attribute_is_exist(key):
                    self.data_set.update(self._api_get())
                    self.modified()
                    try:
                        return self.data_set[key]
                    except KeyError:
                        raise AttributeCanNotBeLoaded("""The attribute \"{0}\" cannot be loaded using the API. 
                                                         Check whether you have access to this information 
                                                         and try again.""".format(key))
                else:
                    raise AttributeError("The attribute does not exist.")

    """
        Метод обновляет данные об объекте. При передаче в именованный аргумент type любого значения кроме "all"
        приводит к обновлению атрибутов, перечисленных в итерируемом объекте keys.
    """
    def reload(self, type="all", keys=[]):
        if type == "all":
            self.data_set.update(self._api_get())
            self.modified()
            return True
        else:
            data = self._api_get(keys)
            self.data_set.update(data)
            self.modified()
            return data

    """
        Метод обновляет данные пользователя как на сервере VK, так и в текущей объект-сессии.
    """
    def update(self, key, value, lazy=False):
        if lazy:
            self.need_to_update = True
            self.waiting_for_updates.update({key: value})
        else:
            if attribute_is_exist(key):
                self.data_set[key] = value
            else:
                raise AttributeError("Атрибут не существует")

    """
        Метод устанавливает время последней модификации на "сейчас".
    """
    def modified(self):
        self.last_modified = int(self.time())
        return self.last_modified

    def __del__(self):
        if self.need_to_update:
            self.update()

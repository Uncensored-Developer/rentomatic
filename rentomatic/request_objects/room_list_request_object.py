import collections
from abc import ABC, abstractmethod


class InvalidRequestObject:

    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return bool(self.errors)

    def __bool__(self):
        return False


class ValidRequestObject(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, adict):
        pass

    def __bool__(self):
        return True


class RoomListRequestObject(ValidRequestObject):

    accepted_filters = ['code__eq', 'price__eq', 'price__lt', 'price__gt']

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict:
            if not isinstance(adict['filters'], collections.Mapping):
                invalid_req.add_error('filters', 'filters should be a mapping')
                return invalid_req

            for k, v in adict['filters'].items():
                if k not in cls.accepted_filters:
                    invalid_req.add_error(
                        'filters', 'key {} cannot be used'.format(k)
                    )
        if invalid_req.has_errors():
            return invalid_req
        return cls(filters=adict.get('filters', None))

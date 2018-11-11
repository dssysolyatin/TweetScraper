import abc
from json import JSONEncoder


class ISerializable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def serialize(self) -> dict:
        pass


class Encoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, ISerializable):
            return o.serialize()

        return super().default(o)

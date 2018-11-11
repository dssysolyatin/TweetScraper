from twitter.json.encoder import ISerializable


class Account(ISerializable):
    fullname: str
    href: str
    id: int

    def serialize(self) -> dict:
        return self.__dict__

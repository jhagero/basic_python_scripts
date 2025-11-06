from _typeshed import Incomplete

log: Incomplete

class Plugin:
    loaded: bool
    name: Incomplete
    import_path: Incomplete
    check: Incomplete
    def __init__(self, name, import_path, check=None, **named) -> None: ...
    def load(self): ...
    @classmethod
    def match(cls, *args) -> None: ...
    @classmethod
    def all(cls): ...
    @classmethod
    def by_name(cls, name): ...

def importByName(fullName): ...

class PlatformPlugin(Plugin):
    registry: Incomplete
    @classmethod
    def match(cls, key): ...

class FormatHandler(Plugin):
    registry: Incomplete
    @classmethod
    def match(cls, value): ...

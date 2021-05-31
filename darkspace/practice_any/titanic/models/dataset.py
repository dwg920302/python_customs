from dataclasses import dataclass

@dataclass
class Dataset(object):
    context: str
    fname: str
    train: str
    test: str
    id: str
    label: str

    @property
    def context(self) -> str: return self._context
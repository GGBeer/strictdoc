from abc import ABC, abstractmethod


class Node(ABC):
    @property
    @abstractmethod
    def is_requirement(self):
        raise NotImplementedError(self)

    @property
    @abstractmethod
    def is_section(self):
        raise NotImplementedError(self)

    @property
    @abstractmethod
    def is_composite_requirement(self):
        raise NotImplementedError(self)

    @property
    @abstractmethod
    def is_freetext(self):
        raise NotImplementedError(self)

from abc import ABC, abstractmethod

class ManipulatorInterface(ABC):
    @abstractmethod
    def transform(self, data):
        pass
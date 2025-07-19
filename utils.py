# utils.py
from abc import ABC, abstractmethod

class Utility(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def set_details(self):
        pass

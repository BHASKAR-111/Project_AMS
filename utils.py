# utils.py
<<<<<<< HEAD

# Importing abstract base class module
from abc import ABC, abstractmethod

# Utility is an abstract base class
class Utility(ABC):
    # Abstract method that must be implemented to set details (e.g., staff or ambulance)
    @abstractmethod
    def set_details(self):
        pass

    # Abstract method that must be implemented to get details (e.g., staff or ambulance)
    @abstractmethod
    def get_details(self):
        pass
=======
from abc import ABC, abstractmethod

class Utility(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def set_details(self):
        pass
>>>>>>> b861b440486eb2ccaf0ed503f37d645d6f3a36dd

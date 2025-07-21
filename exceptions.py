<<<<<<< HEAD
#exceptions.py
class InvalidEmpIDException(Exception):
    def __init__(self, message="❌ Employee ID must be a valid integer."):
        super().__init__(message)


class InvalidVehicleNumberException(Exception):
    def __init__(self, message="❌ Vehicle number must follow proper format like KA01AB1234."):
        super().__init__(message)


class DuplicateAmbulanceIDException(Exception):
    def __init__(self, message="❌ Ambulance ID already exists. Please enter a unique ID."):
        super().__init__(message)


class DuplicateEmpIDException(Exception):
    def __init__(self, message="❌ Employee ID already exists. Please enter a unique Employee ID."):
        super().__init__(message)
        
class OwnershipExcepiton(Exception):
    def __init__(self, message="❌ Please choose from own/outsourced"):
        super().__init__(message)
=======
# exceptions.py

class InvalidEmpIDException(Exception):
    def __init__(self):
        super().__init__("Employee ID must be an integer.")

class InvalidVehicleNumberException(Exception):
    def __init__(self):
        super().__init__("Vehicle number must be <= 10 characters and start with 'KA'.")
>>>>>>> b861b440486eb2ccaf0ed503f37d645d6f3a36dd

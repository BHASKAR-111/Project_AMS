# exceptions.py

class InvalidEmpIDException(Exception):
    def __init__(self):
        super().__init__("Employee ID must be an integer.")

class InvalidVehicleNumberException(Exception):
    def __init__(self):
        super().__init__("Vehicle number must be <= 10 characters and start with 'KA'.")

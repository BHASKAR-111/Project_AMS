# staff.py

from exceptions import InvalidEmpIDException, DuplicateEmpIDException

class Staff:
    # Class-level list to store all staff members
    all_staff = []

    def __init__(self, emp_id, name, phone, department): 
        # Initialize staff attributes
        self.emp_id = emp_id
        self.name = name
        self.phone = phone
        self.department = department
        self.role = "General"      # Default role is General
        self.assigned = False      # Staff is unassigned by default

    def set_details(self):
        # Check for duplicate emp_id
        if any(s.emp_id == self.emp_id for s in Staff.all_staff):
            raise DuplicateEmpIDException()
        # Add staff member to the staff list
        Staff.all_staff.append(self)
        print(f"✅ Staff with ID {self.emp_id} added successfully.")

    def get_details(self):
        # Print full staff details
        print(f" ID: {self.emp_id}")
        print(f" Name: {self.name}")
        print(f" Phone: {self.phone}")
        print(f" Department: {self.department}")
        print(f" Role: {self.role}")
        print(f" Availability: {'Available' if not self.assigned else 'Assigned'}")

    # Class method to return a list of available (not assigned) staff members
    @classmethod
    def get_all_available_staff(cls):
        available = []
        # Add relevant staff information to the list as a dictionary
        for staff in cls.all_staff:
            if not staff.assigned:
                available.append({
                    "emp_id": staff.emp_id,
                    "name": staff.name,
                    "role": staff.role
                })
        return available
        # return [s.__dict__ for s in cls.all_staff if not s.assigned]    


# Doctor is a specialized type of Staff
class Doctor(Staff):
    def __init__(self, emp_id, name, phone, department, speciality):
        # Call parent constructor
        super().__init__(emp_id, name, phone, department)
        self.speciality = speciality
        self.role = "Doctor"   # Override role as Doctor

    def get_details(self):
        # Extend base details with speciality
        super().get_details()
        print(f"Speciality: {self.speciality}")


# Nurse is another specialized Staff
class Nurse(Staff):
    def __init__(self, emp_id, name, phone, department):
        # Call parent constructor
        super().__init__(emp_id, name, phone, department)
        self.role = "Nurse"    # Override role as Nurse

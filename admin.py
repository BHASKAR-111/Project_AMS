# admin.py

from utils import Utility
from exceptions import InvalidEmpIDException, InvalidVehicleNumberException

class Ambulance(Utility):
    ambulance_list = []

    def __init__(self, emp_id, vehicle_no, ownership, driver_name, phone_no, facilities):
        if not isinstance(emp_id, int):
            raise InvalidEmpIDException()
        if len(vehicle_no) > 10 or not vehicle_no.lower().startswith("ka"):
            raise InvalidVehicleNumberException()
        
        self.emp_id = emp_id
        self.vehicle_no = vehicle_no
        self.ownership = ownership
        self.driver_name = driver_name
        self.phone_no = phone_no
        self.facilities = facilities

    def set_details(self):
        data = {
            "emp_id": self.emp_id,
            "vehicle_no": self.vehicle_no,
            "ownership": self.ownership,
            "driver_name": self.driver_name,
            "phone_no": self.phone_no,
            "facilities": self.facilities,
            "assigned_staff": []
        }
        Ambulance.ambulance_list.append(data)
        print("✅ Ambulance added successfully!\n")

    def get_details(self):
        return Ambulance.ambulance_list

    def print_summary(self):
        print("\n========= Ambulance Summary =========")
        print(f"Total Ambulances: {len(Ambulance.ambulance_list)}")
        own = 0
        for ambulance in Ambulance.ambulance_list:
            if ambulance["ownership"].lower() == "own":
                own += 1

        outsourced = len(Ambulance.ambulance_list) - own
        print(f"Own: {own}, Outsourced: {outsourced}")

        for amb in Ambulance.ambulance_list:
            print(f"""
            Emp ID: {amb['emp_id']}
            Vehicle No: {amb['vehicle_no']}
            Ownership: {amb['ownership']}
            Driver: {amb['driver_name']} ({amb['phone_no']})
            Facilities: {', '.join(amb['facilities'])}
            Assigned Staff: {', '.join(amb['assigned_staff']) if amb['assigned_staff'] else 'None'}
            """)
        print("=====================================\n")

    def edit_details(self, emp_id, key, new_value):
        for amb in Ambulance.ambulance_list:
            if amb["emp_id"] == emp_id:
                amb[key] = new_value
                print("✏️ Successfully edited.\n")
                return
        print("❌ Ambulance not found.")

    def delete_ambulance(self, emp_id):
        for amb in Ambulance.ambulance_list:
            if amb["emp_id"] == emp_id:
                Ambulance.ambulance_list.remove(amb)
                print("🗑️ Ambulance deleted successfully.\n")
                return
        print("❌ Ambulance not found.")

# admin.py

from exceptions import InvalidVehicleNumberException,DuplicateAmbulanceIDException,OwnershipExcepiton
from staff import Staff
from utils import Utility

class Ambulance(Utility):
    # Class variable to store all ambulance objects
    ambulances = []

    def __init__(self, id, vehicle_no, ownership, driver_name, phone_no, facilities):
        # Check for valid vehicle number format (starts with "KA" and ≤ 10 characters)
        if len(vehicle_no) > 10 or not vehicle_no.lower().startswith("ka"):
            raise InvalidVehicleNumberException()
        # Check for duplicate ID BEFORE creating the object
        if any(a.id == id for a in Ambulance.ambulances):
            raise DuplicateAmbulanceIDException(f"Ambulance ID {id} already exists.")

        # Initialize ambulance attributes
        self.id = id
        self.vehicle_no = vehicle_no
        self.ownership = ownership
        self.driver_name = driver_name
        self.phone_no = phone_no
        self.facilities = facilities
        self.assigned_staff = []  # Staff assigned to this ambulance

    def set_details(self):
        Ambulance.ambulances.append(self)
        print(f"\n✅ Ambulance ID {self.id} added successfully!")

    def get_details(self):
        # Display full details of an ambulance
        print(f"\n🚑 Ambulance ID: {self.id}")
        print(f"🚗 Vehicle Number: {self.vehicle_no}")
        print(f"🔑 Ownership: {self.ownership}")
        print(f"👨‍✈️ Driver Name: {self.driver_name}")
        print(f"📞 Phone Number: {self.phone_no}")
        print(f"🩺 Facilities: {', '.join(self.facilities) if self.facilities else 'None'}")

        # Display assigned staff if any
        if self.assigned_staff:
            print("👥 Assigned Staff:")
            for s in self.assigned_staff:
                print(f"   - ID: {s['emp_id']}, Name: {s['name']}, Role: {s['role']}")
        else:
            print("👥 Assigned Staff: None")

    def edit_details(self, id, key, value):
        # Edit a field of an ambulance if found
        for amb in Ambulance.ambulances:
            if amb.id == id:
                if hasattr(amb, key):
                    try:
                    # Re-validate vehicle number and ownership
                        if key == "vehicle_no":
                            if len(value) > 10 or not value.lower().startswith("ka"):
                                raise InvalidVehicleNumberException()
                        elif key=="ownership":
                            if key.lower() not in ["own", "outsourced"]:
                                raise  OwnershipExcepiton()
                        setattr(amb, key, value)
                        print("✅ Ambulance details updated successfully.")
                    except (InvalidVehicleNumberException,OwnershipExcepiton) as e:
                        print(f" {e}")
                        
                    else:
                        setattr(amb, key, value)
                        print("✅ Ambulance details updated successfully.")
                else:
                    print("❗ Invalid field name.")
                return
        print("❗ Ambulance not found.")

    def delete_ambulance(self, id):
        # Remove ambulance with given ID
        for amb in Ambulance.ambulances:
            if amb.id == id:
                Ambulance.ambulances.remove(amb)
                print(f"✅ Ambulance ID {id} deleted successfully.")
                return
        print("❗ Ambulance not found.")

    def assign_staff(self, amb_id, emp_id):
        # Assign available staff to ambulance
        for amb in Ambulance.ambulances:
            if amb.id == amb_id:
                # staff = next((s for s in Staff.all_staff if s.emp_id == emp_id), None)
                staff = None  # Initialize staff as None
                for s in Staff.all_staff:
                    if s.emp_id == emp_id:  # If the ID matches
                        staff = s  # Assign to staff
                        break  

                if staff:
                    # Checks if staff is already assigned
                    if staff.assigned:
                        print(f"❗ Staff ID {emp_id} is already assigned to another ambulance.")
                        return
                    # Add staff details to ambulance and mark them as assigned
                    amb.assigned_staff.append({
                        "emp_id": staff.emp_id,
                        "name": staff.name,
                        "role": staff.role
                    })
                    staff.assigned = True
                    print(f"✅ Staff ID {emp_id} assigned to Ambulance ID {amb_id}.")
                else:
                    print("❗ Staff ID not found.")
                return
        print("❗ Ambulance not found.")

    def print_summary(self):
        # Print a summary of all ambulances
        print("\n========= 🚑 AMBULANCE SUMMARY =========")
        print(f"Total Ambulances: {len(Ambulance.ambulances)}")

        # Count number of "own" ambulances
        own = 0
        for ambulance in Ambulance.ambulances:
            if ambulance.ownership.lower() == "own":
                own += 1
         # Count number of "outsourced" ambulances
        outsourced = len(Ambulance.ambulances) - own
        print(f"Own: {own}, Outsourced: {outsourced}")

        # Print details of each ambulance
        print("========== 🚐 DETAILS ========== ")
        for amb in Ambulance.ambulances:
            amb.get_details()
            print("-" * 40)

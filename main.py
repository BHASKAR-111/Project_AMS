# Import required classes from different modules
from admin import Ambulance
from staff import Staff, Doctor, Nurse
from exceptions import InvalidEmpIDException, InvalidVehicleNumberException, DuplicateEmpIDException, DuplicateAmbulanceIDException,OwnershipExcepiton

# Function to display available facilities and take user input
def get_facilities_input():
    options = ["oxygen", "ventilator", "duty doctor", "nurse"]
    print("\n========== AVAILABLE FACILITIES ==========")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    selected = input("Enter choices separated by commas (e.g., 1,3): ").split(',')
    facilities = []
    for item in selected:
        item = item.strip()
        if item.isdigit():
            index = int(item)
            if 1 <= index <= len(options):
                facilities.append(options[index - 1])
    return facilities

# Function to print the main menu
def main_menu():
    print("\n================ WELCOME TO AMBULANCE MANAGEMENT SYSTEM ================")
    print("1] ADD AMBULANCE\t\t2] VIEW SUMMARY\t\t3] EDIT AMBULANCE")
    print("4] DELETE AMBULANCE\t\t5] ADD STAFF\t\t6] ASSIGN STAFF TO AMBULANCE")
    print("=============================== *** ENTER 0 TO EXIT *** ===============================")

choice = 100  # default choice to keep the loop running

while choice != 0:
    main_menu()
    try:
        choice = int(input("\nEnter your choice: "))

        while choice != 9 and choice != 0:

            # Option 1: Add Ambulance
            if choice == 1:
                try:
                    id = int(input("Enter Ambulance ID: "))    
                    
                     # Check for duplicate ID BEFORE creating the object
                    if any(a.id == id for a in Ambulance.ambulances):
                        raise DuplicateAmbulanceIDException(f"Ambulance ID {id} already exists.")
                    
                    vehicle_no = input("Enter Vehicle Number: ")
                    # Check for valid vehicle number format (starts with "KA" and ≤ 10 characters)
                    if len(vehicle_no) > 10 or not vehicle_no.lower().startswith("ka"):
                        raise InvalidVehicleNumberException()
                    
                    ownership = input("Enter Ownership (own/outsourced): ")
                    #Check for owership input
                    if ownership.lower() not in ["own", "outsourced"]:
                        raise  OwnershipExcepiton()
                   
                    driver_name = input("Enter Driver Name: ")
                    phone_no = input("Enter Phone Number: ")
                    facilities = get_facilities_input()

                    # Create and register ambulance
                    amb = Ambulance(id, vehicle_no, ownership, driver_name, phone_no, facilities)
                    amb.set_details()
                except (InvalidEmpIDException, DuplicateAmbulanceIDException,InvalidVehicleNumberException, DuplicateEmpIDException,OwnershipExcepiton) as e:
                    print(f"Error: {e}")

                # Options after adding
                print("\n1] ADD NEW AMBULANCE")
                print("2] VIEW SUMMARY")
                print("9] GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

            # Option 2: View Ambulance Summary
            elif choice == 2:
                amb = Ambulance(0, "ka00", "own", "", "", [])
                amb.print_summary()
                print("\n9] GO BACK TO MAIN MENU")
                print("0] EXIT")
                choice = int(input("Enter choice: "))

            # Option 3: Edit Ambulance
            elif choice == 3:
                id = int(input("Enter Ambulance ID to edit: "))
                key = input("Enter field to edit (vehicle_no/ownership/driver_name/phone_no): ")
                value = input("Enter new value: ")
                amb = Ambulance(0, "ka00", "own", "", "", [])
                amb.edit_details(id, key, value)
                print("\n9] GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

            # Option 4: Delete Ambulance
            elif choice == 4:
                id = int(input("Enter Ambulance ID to delete: "))
                amb = Ambulance(0, "ka00", "own", "", "", [])
                amb.delete_ambulance(id)
                print("\n9] GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

            # Option 5: Add Staff (Doctor or Nurse)
            elif choice == 5:
                try:
                    emp_id = int(input("Enter Staff Employee ID: "))
                    if any(s.emp_id == emp_id for s in Staff.all_staff):
                        raise DuplicateEmpIDException()
                        
                    name = input("Enter Staff Name: ")
                    phone = input("Enter Phone Number: ")
                    department = input("Enter Department: ")
                    role = input("Enter Role (doctor/nurse): ").lower()

                    # Create doctor or nurse object based on role
                    if role == "doctor":
                        speciality = input("Enter Doctor's Speciality: ")
                        staff = Doctor(emp_id, name, phone, department, speciality)
                    elif role == "nurse":
                        staff = Nurse(emp_id, name, phone, department)
                    else:
                        print("Invalid role. Only 'doctor' or 'nurse' allowed.\n")
                        continue

                    # Save staff details
                    staff.set_details()

                except ( DuplicateEmpIDException) as e:
                    print(f"Error: {e}")

                print("\n5] ADD STAFF")
                print("9] GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

            # Option 6: Assign Staff to Ambulance
            elif choice == 6:

                print("\n=========== AVAILABLE STAFF (DOCTOR/NURSE) ===========")
                available_staff = Staff.get_all_available_staff()

                if not available_staff:
                    print("No available staff to assign.\n")
                else:
                    # Display available staff
                    for s in available_staff:
                        print(f"ID: {s['emp_id']} | Name: {s['name']} | Role: {s['role'] }")

                    # Take input to assign staff to ambulance
                    amb_id = int(input("Enter Ambulance ID to assign staff to: "))
                    staff_id = int(input("Enter Staff Employee ID to assign: "))
                    amb = Ambulance(0, "ka00", "own", "", "", [])
                    amb.assign_staff(amb_id, staff_id)

                print("\n9] GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

            # Invalid input handler
            else:
                print("Invalid choice.")
                print("9] GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

    # Handle non-integer menu input
    except ValueError:
        print("Please enter a valid number.")

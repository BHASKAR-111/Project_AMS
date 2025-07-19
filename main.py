# main.py

from admin import Ambulance
from exceptions import InvalidEmpIDException, InvalidVehicleNumberException

def get_facilities_input():
    options = ["oxygen", "ventilator", "duty doctor", "nurse"]
    print("Available Facilities:")
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

def main_menu():
    print("\n======================= *** WELCOME TO AMBULANCE MANAGEMENT SYSTEM *** =======================")
    print("\n=============================== *** ENTER YOUR CHOICE *** ===============================")
    print("1] ADD AMBULANCE\t\t2] VIEW SUMMARY\t\t3] EDIT AMBULANCE")
    print("4] DELETE AMBULANCE")
    print("=============================== *** ENTER 0 TO EXIT *** ===============================")

ambulances = []
choice = 100

while choice != 0:
    main_menu()
    try:
        choice = int(input("\nEnter your choice: "))

        while choice != 9 and choice != 0:
            if choice == 1:
                try:
                    emp_id = int(input("Enter Employee ID: "))
                    vehicle_no = input("Enter Vehicle Number: ")
                    ownership = input("Enter Ownership (own/outsourced): ")
                    driver_name = input("Enter Driver Name: ")
                    phone_no = input("Enter Phone Number: ")
                    facilities = get_facilities_input()

                    amb = Ambulance(emp_id, vehicle_no, ownership, driver_name, phone_no, facilities)
                    amb.set_details()
                except (InvalidEmpIDException, InvalidVehicleNumberException) as e:
                    print(f"❌ Error: {e}")
                print("\n1] ADD NEW AMBULANCE")
                print("9] GO BACK TO MAIN MENU")
                print("2] VIEW SUMMARY")
                choice = int(input("Enter choice: "))

            elif choice == 2:
                amb = Ambulance(0, "ka00", "own", "", "", [])  # Dummy
                amb.print_summary()
                print("\n9].GO BACK TO MAIN MENU")
                print("0].EXIT")
                choice = int(input("Enter choice: "))

            elif choice == 3:
                emp_id = int(input("Enter Employee ID to edit: "))
                key = input("Enter field to edit (vehicle_no/ownership/driver_name/phone_no): ")
                value = input("Enter new value: ")
                amb = Ambulance(0, "ka00", "own", "", "", [])
                amb.edit_details(emp_id, key, value)
                print("\n9].GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

            elif choice == 4:
                emp_id = int(input("Enter Employee ID to delete: "))
                amb = Ambulance(0, "ka00", "own", "", "", [])
                amb.delete_ambulance(emp_id)
                print("\n9].GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

            else:
                print("❗ Invalid choice.")
                print("9].GO BACK TO MAIN MENU")
                choice = int(input("Enter choice: "))

    except ValueError:
        print("⚠️ Please enter a valid number.")
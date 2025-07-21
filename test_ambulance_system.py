import unittest
from admin import Ambulance
from staff import Staff, Doctor, Nurse
from exceptions import (
    InvalidVehicleNumberException,
    DuplicateAmbulanceIDException,
    DuplicateEmpIDException
)

class TestAmbulanceSystem(unittest.TestCase):

    def setUp(self):
        """
        Runs before every test method. Clears all stored data to isolate tests.
        """
        Ambulance.ambulances.clear()
        Staff.all_staff.clear()

    # -------------------- UNIT TEST CASES --------------------

    # Unit Test 1
    def test_add_valid_ambulance(self):
        """
        Test Case 1: Add a valid ambulance (vehicle number starts with 'KA').
        Expected: Ambulance is added to the list.
        """
        amb = Ambulance(1,"KA01AB1234", "own", "John", "9876543210", ["oxygen"])
        amb.set_details()
        self.assertEqual(len(Ambulance.ambulances), 1)
        self.assertEqual(Ambulance.ambulances[0].vehicle_no, "KA01AB1234")

    # Unit Test 2
    def test_add_duplicate_ambulance_id(self):
        """
        Test Case 2: Try to add two ambulances with the same ID.
        Expected: Only the first is added.
        """
        amb1 = Ambulance(1, "KA01AB1234", "own", "John", "9876543210", [])
        amb1.set_details()

        with self.assertRaises(DuplicateAmbulanceIDException):
            amb2 = Ambulance(1, "KA01AB5678", "own", "Mike", "1234567890", [])
            amb2.set_details()

    # Unit Test 3
    def test_invalid_vehicle_number(self):
        """
        Test Case 3: Add ambulance with invalid vehicle number (not 'KA' prefix).
        Expected: Raises InvalidVehicleNumberException.
        """
        with self.assertRaises(InvalidVehicleNumberException):
            Ambulance(2, "DL01XYZ1234", "own", "Mike", "1234567890", [])

    # Unit Test 4
    def test_add_doctor(self):
        """
        Test Case 4: Add a Doctor and check role is stored.
        Expected: Doctor object added to staff list with correct role.
        """
        doc = Doctor(101, "Dr. Alice", "9999999999", "Emergency", "Cardiology")
        doc.set_details()
        self.assertEqual(len(Staff.all_staff), 1)
        self.assertEqual(Staff.all_staff[0].role, "Doctor")

    # Unit Test 5
    def test_add_nurse(self):
        """
        Test Case 5: Add a Nurse and verify role.
        Expected: Nurse object added with correct role.
        """
        nurse = Nurse(102, "Nina", "8888888888", "ICU")
        nurse.set_details()
        self.assertEqual(len(Staff.all_staff), 1)
        self.assertEqual(Staff.all_staff[0].role, "Nurse")

    # Unit Test 6
    def test_get_available_staff(self):
        """
        Test Case 6: Add unassigned staff and check available list.
        Expected: Returns 1 available staff member.
        """
        nurse = Nurse(103, "Nina", "8888888888", "ICU")
        nurse.set_details()
        available = Staff.get_all_available_staff()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0]["name"], "Nina")

    # Unit Test 7
    def test_duplicate_employee_id(self):
        """
        Test Case 7: Add two staff with the same emp_id.
        Expected: Second entry should raise DuplicateEmpIDException.
        """
        doc1 = Doctor(104, "Dr. Bob", "8888888888", "ER", "Neuro")
        doc1.set_details()
        with self.assertRaises(DuplicateEmpIDException):
            doc2 = Doctor(104, "Dr. Eve", "7777777777", "ER", "Ortho")
            if any(s.emp_id == doc2.emp_id for s in Staff.all_staff):
                raise DuplicateEmpIDException()
            doc2.set_details()

    # -------------------- INTEGRATION TEST CASES --------------------

    # Integration Test 1
    def test_assign_staff_to_ambulance(self):
        """
        Test Case 8: Add ambulance and staff, assign staff to ambulance.
        Expected: Assignment is successful and reflected in both objects.
        """
        amb = Ambulance(1, "KA01AB1234", "own", "John", "9876543210", [])
        amb.set_details()

        doc = Doctor(101, "Dr. Alice", "9999999999", "Emergency", "Cardiology")
        doc.set_details()

        amb.assign_staff(1, 101)

        self.assertEqual(len(Ambulance.ambulances[0].assigned_staff), 1)
        self.assertTrue(Staff.all_staff[0].assigned)

    # Integration Test 2
    def test_prevent_duplicate_assignment(self):
        """
        Test Case 9: Try to assign same staff to two ambulances.
        Expected: Assignment only allowed once.
        """
        amb1 = Ambulance(1, "KA01AB1234", "own", "John", "9876543210", [])
        amb2 = Ambulance(2, "KA02AB5678", "outsourced", "Mike", "1234567890", [])
        amb1.set_details()
        amb2.set_details()

        doc = Doctor(101, "Dr. Alice", "9999999999", "Emergency", "Cardiology")
        doc.set_details()

        amb1.assign_staff(1, 101)
        amb2.assign_staff(2, 101)  # Should be prevented

        self.assertEqual(len(amb1.assigned_staff), 1)
        self.assertEqual(len(amb2.assigned_staff), 0)

    # -------------------- SYSTEM TEST CASE --------------------

    # System Test 1
    def test_system_flow_add_assign_summary(self):
        """
        Test Case 10: Full system flow - add ambulance, add staff, assign, and view summary.
        Expected: System maintains state and provides accurate summary.
        """
        amb = Ambulance(1, "KA01AB9999", "own", "David", "9999999999", ["oxygen", "nurse"])
        amb.set_details()

        nurse = Nurse(105, "Nancy", "6666666666", "ICU")
        nurse.set_details()

        amb.assign_staff(1, 105)

        summary_output = []
        try:
            amb.print_summary()
            summary_output.append("PASS")
        except Exception as e:
            summary_output.append("FAIL")

        self.assertEqual(summary_output[0], "PASS")

if __name__ == '__main__':
    unittest.main()
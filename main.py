class Patient:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition
        self.appointment = None


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.appointments = []


class Prescription:
    def __init__(self, medicine, dosage):
        self.medicine = medicine
        self.dosage = dosage


class Hospital:
    def __init__(self):
        self.patient_records = []
        self.doctors = []
        self.queue = []
        self.prescriptions = []

    def add_patient(self, patient):
        self.patient_records.append(patient)

    def update_patient(self, name, new_condition):
        for patient in self.patient_records:
            if patient.name == name:
                patient.condition = new_condition
                print("Patient record updated successfully.")
                return
        print("Patient not found.")

    def remove_patient(self, name):
        for patient in self.queue:
            if patient.name == name:
                self.queue.remove(patient)
                print("Patient removed from the queue.")
                return
        print("Patient not found in the queue.")

    def display_queue(self):
        if not self.queue:
            print("No patients in the queue.")
        else:
            print("Patients in queue:")
            for patient in self.queue:
                print(patient.name)

    def add_to_queue(self, patient):
        self.queue.append(patient)
        print("Patient added to the queue.")

    def schedule_appointment(self, patient_name, doctor_name):
        for patient in self.patient_records:
            if patient.name == patient_name:
                for doctor in self.doctors:
                    if doctor.name == doctor_name:
                        if patient.appointment is None:
                            patient.appointment = doctor_name
                            doctor.appointments.append(patient_name)
                            print(f"Appointment scheduled for {patient_name} with {doctor_name}.")
                            return
                        else:
                            print("Patient already has an appointment.")
                            return
                print("Doctor not found.")
                return
        print("Patient not found.")

    def issue_prescription(self, patient_name, medicine, dosage):
        for patient in self.patient_records:
            if patient.name == patient_name:
                prescription = Prescription(medicine, dosage)
                self.prescriptions.append((patient_name, prescription))
                print(f"Prescription issued for {patient_name}: {medicine}, dosage: {dosage}.")
                return
        print("Patient not found.")

    def display_prescriptions(self):
        if not self.prescriptions:
            print("No prescriptions issued.")
        else:
            print("Prescriptions:")
            for patient_name, prescription in self.prescriptions:
                print(f"Patient: {patient_name}, Medicine: {prescription.medicine}, Dosage: {prescription.dosage}")

    def display_patient_records(self):
        if not self.patient_records:
            print("No patient records available.")
        else:
            print("Patient Records:")
            for patient in self.patient_records:
                print(f"Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}, "
                      f"Appointment: {patient.appointment}")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def display_doctors(self):
        if not self.doctors:
            print("No doctors available.")
        else:
            print("Available Doctors:")
            for doctor in self.doctors:
                print(doctor.name)


# Menu interface
def main_menu():
    print("\nMain Menu:")
    print("1. Add a new patient")
    print("2. Update patient information")
    print("3. Remove patient from queue")
    print("4. Show patients waiting for doctor")
    print("5. Schedule appointment")
    print("6. Issue prescription")
    print("7. Show patient records")
    print("8. Display prescriptions")
    print("9. Display available doctors")
    print("10. Exit")


# Function to display available doctors
def display_available_doctors(hospital):
    hospital.display_doctors()


hospital = Hospital()

# Sample usage - Adding doctors
doctor1 = Doctor("Dr. Smith", "Pediatrician")
doctor2 = Doctor("Dr. Johnson", "Dermatologist")
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        condition = input("Enter patient's condition: ")
        patient = Patient(name, age, condition)
        hospital.add_patient(patient)

    elif choice == "2":
        name = input("Enter patient's name: ")
        new_condition = input("Enter new condition: ")
        hospital.update_patient(name, new_condition)

    elif choice == "3":
        name = input("Enter patient's name: ")
        hospital.remove_patient(name)

    elif choice == "4":
        hospital.display_queue()

    elif choice == "5":
        patient_name = input("Enter patient's name: ")
        doctor_name = input("Enter doctor's name: ")
        hospital.schedule_appointment(patient_name, doctor_name)

    elif choice == "6":
        patient_name = input("Enter patient's name: ")
        medicine = input("Enter prescribed medicine: ")
        dosage = input("Enter dosage: ")
        hospital.issue_prescription(patient_name, medicine, dosage)

    elif choice == "7":
        hospital.display_patient_records()

    elif choice == "8":
        hospital.display_prescriptions()

    elif choice == "9":
        display_available_doctors(hospital)

    elif choice == "10":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

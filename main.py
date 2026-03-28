class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.records = []

    def add_record(self, text):
        self.records.append(text)

    def show_records(self):
        print(self.name, "records:")
        for r in self.records:
            print("-", r)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, age):
        self.patients.append(Patient(name, age))

    def find_patient(self, name):
        for p in self.patients:
            if p.name == name:
                return p

    def show_patients(self):
        for p in self.patients:
            print(p.name, p.age)


def run():
    hospital = Hospital()

    while True:
        print("\n1 Add Patient")
        print("2 Add Record")
        print("3 Show Patients")
        print("4 Show Records")
        print("5 Exit")

        c = input()

        if c == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            hospital.add_patient(name, age)

        elif c == "2":
            name = input("Name: ")
            p = hospital.find_patient(name)
            if p:
                p.add_record(input("Record: "))

        elif c == "3":
            hospital.show_patients()

        elif c == "4":
            name = input("Name: ")
            p = hospital.find_patient(name)
            if p:
                p.show_records()

        else:
            break


run()

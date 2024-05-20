from queue import Queue
def main():
    patient_queue = Queue()

    while True:
        print("Patient registration and appointment scheduling")
        print("1. Register patient")
        print("2. Remove patiet")
        print("3. Display patiemt queue")
        print("4. Exit")
        
        choice = input("Enter the number you want to select:")
        if choice == "1":
            register_patient(patient_queue)
        elif choice == "2":
            remove_patient(patient_queue)
        elif choice == "3":
            display_queue(patient_queue)
        elif choice == "4":
            ("logging out")
            break
        else:
            print("Invalid choice")
def register_patient(queue):
    patient_name = input("Enter the name of patient:")
    queue.put(patient_name)
    print(f"patient'{patient_name}' registered successfully")

def remove_patient(queue):
    if queue.empty():
        print("Patient is not in the queue")
    else:
        removed_patient = queue.get()
        print(f"patient'{removed_patient}' removed patient successfully")

def display_queue(queue):
    if queue.empty():
        print("No patient in the queue")
    else:
        print("Current patient queue")
        for index, patient in enumerate (list(queue.queue), start = 1):
            print(f"{index}. {patient}")
if __name__ == "__main__":
    main()
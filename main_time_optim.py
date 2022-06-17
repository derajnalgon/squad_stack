

car_number_slot_map = {}
slot_car_number_map = {}
car_number_age = {}
parking_space = []
age_vehicle_map = {}
age_slot_map = {}



def create_parking_lot(n):
    for i in range(n):
        parking_space.append(n-i)
    print("Created parking of %s slots" % n)



def get_slot_numbers_for_age(int_age):
    if int_age in age_slot_map:
        print(",".join(map(str, age_slot_map[int_age])))
    else:
        print(" ")


def get_slot_number_for_car_with_number(number):
    print(car_number_slot_map[number])

def get_vehicle_registration_number_for_driver_of_age(age_int):
    if age_int in age_vehicle_map:
        print(",".join(map(str, age_vehicle_map[age_int])))
    else:
        print(" ")









def insert_a_slot(slot_no):

    for i in range(len(parking_space)-1, -1, -1):
        if slot_no < parking_space[i]:
            parking_space.insert(i+1, slot_no)
            return ""

    parking_space.insert(0, slot_no)






def park_a_car(vehicle_no, age):
    parking_slot = parking_space.pop()
    car_number_slot_map[vehicle_no] = parking_slot
    slot_car_number_map[parking_slot] = vehicle_no
    car_number_age[vehicle_no] = age
    if age in age_vehicle_map:
        age_vehicle_map[age].append(vehicle_no)
    else:
        age_vehicle_map[age] = [vehicle_no]

    if age in age_slot_map:
        age_slot_map[age].append(parking_slot)
    else:
        age_slot_map[age] = [parking_slot]

    print('Car with vehicle registration number "%s" has been parked at slot number %s' % (vehicle_no, parking_slot))



def leave_a_car(slot_no):
    car_no = slot_car_number_map[slot_no]
    _ = insert_a_slot(slot_no)
    driver_age = car_number_age[car_no]
    age_vehicle_map[driver_age].remove(car_no)
    age_slot_map[driver_age].remove(slot_no)
    car_number_slot_map.pop(car_no, None)
    slot_car_number_map.pop(slot_no, None)
    print('Slot number %s vacated, the car with vehicle registration number "%s" left the space, the driver of the car was of age %s' % (slot_no, car_no, driver_age))





def main():


    with  open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    for i, line in enumerate(lines):
        line_contents = line.strip("\n").split()
        if line_contents[0] == "Create_parking_lot":
            create_parking_lot(int(line_contents[1]))

        elif line_contents[0].lower() == "park":
            park_a_car(line_contents[1], int(line_contents[3]))

        elif line_contents[0].lower() == "leave":
            leave_a_car(int(line_contents[1]))

        elif line_contents[0].lower() == "slot_numbers_for_driver_of_age":
            get_slot_numbers_for_age(int(line_contents[1]))

        elif line_contents[0].lower() == "slot_number_for_car_with_number":
            get_slot_number_for_car_with_number(line_contents[1])

        elif line_contents[0].lower() == "vehicle_registration_number_for_driver_of_age":
            get_vehicle_registration_number_for_driver_of_age(int(line_contents[1]))


if __name__ == '__main__':
    main()

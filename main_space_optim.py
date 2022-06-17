
slot_car_number_map = {}
car_num_driver_age_map = {}
parking_space = []



def create_parking_lot(n):
    for i in range(n):
        parking_space.append(n-i)
    print("Created parking of %s slots" % n)


def get_slot_numbers_by_age(driver_age):
    temp_val = []
    for key, val in slot_car_number_map.items():
        if car_num_driver_age_map[val] == driver_age:
            temp_val.append(key)
    if temp_val:
        print(",".join(map(str, temp_val)))
    else:
        print("")


def get_slot_number_by_car_num(car_number):
    for key, val in slot_car_number_map.items():
        if val == car_number:
            print(key)
            return
    print("There is no car at that slot")


def get_vehicle_registration_number_by_driver_age(age_int):
    temp_val = []
    for key, val in car_num_driver_age_map.items():
        if val == age_int:
            temp_val.append(key)
    if temp_val:
        print(",".join(map(str, temp_val)))
    else:
        print("")


def insert_new_slot(slot_no):

    for i in range(len(parking_space)-1, -1, -1):
        if slot_no < parking_space[i]:
            parking_space.insert(i+1, slot_no)
            return ""

    parking_space.insert(0, slot_no)


def park_a_car(vehicle_no, age):
    if parking_space:
        parking_slot = parking_space.pop()
        # car_number_slot_map[vehicle_no] = parking_slot
        slot_car_number_map[parking_slot] = vehicle_no
        car_num_driver_age_map[vehicle_no] = age
        print('Car with vehicle registration number "%s" has been parked at slot number %s' % (vehicle_no, parking_slot))
    else:
        print("No Parking slot is Empty.Please wait till someone leaves")


def leave_a_car(slot_no):
    if slot_no in slot_car_number_map:
        car_no = slot_car_number_map[slot_no]
        _ = insert_new_slot(slot_no)
        driver_age = car_num_driver_age_map[car_no]
        car_num_driver_age_map.pop(car_no, None)
        slot_car_number_map.pop(slot_no, None)
        print('Slot number %s vacated, the car with vehicle registration number "%s" left the space,'
              '\ the driver of the car was of age %s' % (slot_no, car_no, driver_age))
    else:
        print("Theres no car at the slot to leave")





def main():


    with  open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    for i, line in enumerate(lines):
        line_contents = line.strip("\n").split()
        if line_contents[0].lower() == "create_parking_lot":
            create_parking_lot(int(line_contents[1]))

        elif line_contents[0].lower() == "park":
            park_a_car(line_contents[1], int(line_contents[3]))

        elif line_contents[0].lower() == "leave":
            leave_a_car(int(line_contents[1]))

        elif line_contents[0].lower() == "slot_numbers_for_driver_of_age":
            get_slot_numbers_by_age(int(line_contents[1]))

        elif line_contents[0].lower() == "slot_number_for_car_with_number":
            get_slot_number_by_car_num(line_contents[1])

        elif line_contents[0].lower() == "vehicle_registration_number_for_driver_of_age":
            get_vehicle_registration_number_by_driver_age(int(line_contents[1]))


if __name__ == '__main__':
    main()

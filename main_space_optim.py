
class Parking_lot():
    def __init__(self, n):
        self.parking_space = self.create_parking_lot(n)
        self.car_num_driver_age_map = {}
        self.slot_car_number_map = {}

    def create_parking_lot(self, n):
        temp_parking_space = []
        for i in range(n):
            temp_parking_space.append(n-i)
        print("Created parking of %s slots" % n)
        return temp_parking_space


    def get_slot_numbers_by_age(self, driver_age):
        temp_val = []
        for key, val in self.slot_car_number_map.items():
            if self.car_num_driver_age_map[val] == driver_age:
                temp_val.append(key)
        if temp_val:
            print(",".join(map(str, temp_val)))
        else:
            print("")


    def get_slot_number_by_car_num(self, car_number):
        for key, val in self.slot_car_number_map.items():
            if val == car_number:
                print(key)
                return
        print("There is no car at that slot")


    def get_vehicle_registration_number_by_driver_age(self, age_int):
        temp_val = []
        for key, val in self.car_num_driver_age_map.items():
            if val == age_int:
                temp_val.append(key)
        if temp_val:
            print(",".join(map(str, temp_val)))
        else:
            print("")


    def insert_new_slot(self, slot_no):
        for i in range(len(self.parking_space)-1, -1, -1):
            if slot_no < self.parking_space[i]:
                self.parking_space.insert(i+1, slot_no)
                return ""

        self.parking_space.insert(0, slot_no)


    def park_a_car(self, vehicle_no, age):
        if self.parking_space:
            parking_slot = self.parking_space.pop()
            # car_number_slot_map[vehicle_no] = parking_slot
            self.slot_car_number_map[parking_slot] = vehicle_no
            self.car_num_driver_age_map[vehicle_no] = age
            print('Car with vehicle registration number "%s" has been parked at slot number %s' % (vehicle_no, parking_slot))
        else:
            print("No Parking slot is Empty.Please wait till someone leaves")


    def leave_a_car(self, slot_no):
        if slot_no in self.slot_car_number_map:
            car_no = self.slot_car_number_map[slot_no]
            _ = self.insert_new_slot(slot_no)
            driver_age = self.car_num_driver_age_map[car_no]
            self.car_num_driver_age_map.pop(car_no, None)
            self.slot_car_number_map.pop(slot_no, None)
            print('Slot number %s vacated, the car with vehicle registration number "%s" left the space, '
                  'the driver of the car was of age %s' % (slot_no, car_no, driver_age))
        else:
            print("Theres no car at the slot to leave")

def main():


    with  open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    line_contents = lines[0].strip("\n").split()
    if line_contents[0].lower() == "create_parking_lot":
        parking_lot = Parking_lot(int(line_contents[1]))
    else:
        print("Thhe first should be create parking lot")


    for i, line in enumerate(lines):
        line_contents = line.strip("\n").split()
        if i == 0:
            continue
        elif line_contents[0].lower() == "park":
            parking_lot.park_a_car(line_contents[1], int(line_contents[3]))

        elif line_contents[0].lower() == "leave":
            parking_lot.leave_a_car(int(line_contents[1]))

        elif line_contents[0].lower() == "slot_numbers_for_driver_of_age":
            parking_lot.get_slot_numbers_by_age(int(line_contents[1]))

        elif line_contents[0].lower() == "slot_number_for_car_with_number":
            parking_lot.get_slot_number_by_car_num(line_contents[1])

        elif line_contents[0].lower() == "vehicle_registration_number_for_driver_of_age":
            parking_lot.get_vehicle_registration_number_by_driver_age(int(line_contents[1]))


if __name__ == '__main__':
    main()

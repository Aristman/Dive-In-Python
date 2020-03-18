import os
import csv


class CarBase:
    car_types = ('car', 'truck', 'spec_machine')
    image_ext = ('.jpg', '.jpeg', '.png', '.gif')

    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = ''
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = self.car_types[0]


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = self.car_types[1]
        _body_str = body_whl.split('x')
        _body_whl = [0.0, 0.0, 0.0]
        if len(_body_str) == 3:
            for i in range(3):
                try:
                    _body_whl[i] = float(_body_str[i])
                except ValueError:
                    continue
                except IndexError:
                    break
        self.body_length, self.body_width, self.body_height = _body_whl

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = self.car_types[2]
        self.extra = extra


def get_car_list(file_name):
    try:
        with open(file_name) as f:
            car_table = list(csv.reader(f, delimiter=';'))
        result_table = []
        for row in car_table[1:]:
            if len(row) == 7:
                try:
                    carrying = float(row[5])
                    if row[0] in CarBase.car_types and \
                            row[1] != '' and \
                            os.path.splitext(row[3])[-1] in CarBase.image_ext:
                        if row[0] == 'car' and row[2].isdigit():
                            result_table.append(Car(row[1], row[3], carrying, row[2]))
                        elif row[0] == 'truck':
                            result_table.append(Truck(row[1], row[3], carrying, row[4]))
                        elif row[0] == 'spec_machine' and row[6] != '':
                            result_table.append(SpecMachine(row[1], row[3], carrying, row[6]))
                except TypeError:
                    continue
                except ValueError:
                    continue
        return result_table
    except FileNotFoundError:
        print('File not found')
        return None

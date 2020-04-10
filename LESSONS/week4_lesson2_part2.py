class WriteToFile:
    def __init__(self, file_name, value):
        self.file_name = file_name
        self.value = value

    def __set__(self, instance, value):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(f'{value}\n')

    def __get__(self, instance, owner):
        return self.value

class Account:

    def __init__(self, file_name, value):
        self._file_name = file_name
        self._value = value

    amount = WriteToFile(obj._file_name, value)


my_box = Account('log_1.txt', 0)
print(my_box.amount)
my_box.amount = 20
my_box.amount = 100
print(my_box.amount)

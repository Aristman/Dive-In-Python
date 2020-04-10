from os import path
import tempfile


class File:

    def __init__(self, file_name):
        self.file_name = file_name
        self.now_pos = 0
        self.end_pos = 0
        self.text = []
        if not path.exists(file_name):
            open(file_name, 'w').close()

    def read(self):
        with open(self.file_name) as f:
            return f.read()

    def write(self, str):
        with open(self.file_name, 'w') as f:
            f.write(str)

    def __add__(self, other):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file_name = tmp_file.name
        res = File(tmp_file_name)
        res.write(self.read() + other.read())
        return res

    def __radd__(self, other):
        self.__add__(other)

    def __str__(self):
        return self.file_name

    def __iter__(self):
        self.now_pos = 0
        self.end_pos = 0
        with open(self.file_name) as f:
            for row in f:
                self.text.append(str(row))
                self.end_pos += 1
        return self

    def __next__(self):
        if self.now_pos == self.end_pos:
            raise StopIteration
        result = self.text[self.now_pos]
        self.now_pos += 1
        return result

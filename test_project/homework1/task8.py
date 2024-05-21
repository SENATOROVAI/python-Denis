from contextlib import contextmanager


@contextmanager
def file_opener(name):
    print("Привет,", name, "!")
    yield name.upper()
    print("Пока,", name, "!")


with file_opener("Денис") as c:
    for row in c:
        for letter in row:
            print(letter * 3)


class FileOpener:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Привет,", self.name, end="!\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Пока,", self.name, "!")


f_opener = FileOpener('Денис')


with f_opener as test_file:
    for row in test_file.name:
        for letter in row:
            print(letter.upper() * 3)

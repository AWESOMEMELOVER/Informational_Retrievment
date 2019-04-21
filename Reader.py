import os


class Reader:
    def __init__(self):
        self.path = os.getcwd() + '\\docs\\'
        self.file_list = os.listdir(self.path)

    def generate_string_lines(self):
        for i in self.file_list:
            if i.endswith('.txt'):
                with open(self.path + i, 'r') as file:
                    for line in file:
                        if not line == '\n':
                            yield line.rstrip(), file.name.split('\\')[-1]


if __name__ == '__main__':
    reader = Reader()
    for i in reader.generate_string_lines():
        print(i)
    print(reader.file_list.index('Text-37.txt'))

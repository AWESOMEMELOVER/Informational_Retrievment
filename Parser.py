from nltk.tokenize import sent_tokenize, word_tokenize

from Query import Query
from Reader import Reader
from nltk.corpus import stopwords
import string, pickle


class Parser:
    res_dict = {}
    res_matrix = {}
    res_biword_index = {}
    stop_words = list(list(stopwords.words('english')) + list(string.printable) + list("'s"))

    def __init__(self):
        self.reader = Reader()

    def __create_inverted_index(self):
        for line in self.reader.generate_string_lines():
            words = word_tokenize(line[0])
            from_file = line[1]
            for word in words:
                if word.lower() not in self.stop_words:
                    if word.lower() in self.res_dict:
                        self.res_dict[word.lower()].add(self.reader.file_list.index(from_file))
                    else:
                        self.res_dict[word.lower()] = {self.reader.file_list.index(from_file)}
        return self.res_dict




    def __create_incident_matrix(self):
        inv_index = self.create_or_load_dictionary()
        for k, v in inv_index.items():
            inv_index[k] = self.__to_matrix(v)
        return inv_index

    def __to_matrix(self, list_of_presented_files):
        res_list = []
        for i in enumerate(self.reader.file_list):
            if i[0] in list_of_presented_files:
                res_list.append(1)
            else:
                res_list.append(0)
        return res_list

    def create_or_load_dictionary(self):
        try:
            with open('dict.pickle', "rb") as f:
                foo = pickle.load(f)
        except Exception:
            foo = self.__create_inverted_index()
            with open('dict.pickle', "wb") as f:
                pickle.dump(foo, f)
        return foo

    def create_or_load_matrix(self):
        try:
            with open('matrix.pickle', "rb") as f:
                foo = pickle.load(f)
        except Exception:
            foo = self.__create_incident_matrix()
            with open('matrix.pickle', "wb") as f:
                pickle.dump(foo, f)
        return foo


if __name__ == '__main__':
    parser = Parser()
    print(parser.create_or_load_dictionary())
    print(parser.create_or_load_matrix())
    query = Query('query.txt')
    print(query.process_query(parser.create_or_load_matrix()))

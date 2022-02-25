import logging

FORMAT = '%(levelname)s || %(asctime)s || %(module)s  || %(funcName)s  ||  %(lineno)d  ||  %(message)s'
logging.basicConfig(filename="Bag of word.log", format=FORMAT, level=logging.INFO)


class BagOfWord:
    def __init__(self):
        self.filename_list = []

    def count_of_word(self, file_path):
        """this function return a list of tuple with word and its respective count
                sample example -  [('sudh', 6 ) , ('kumar',3)]"""
        try:
            data = open(file_path, encoding='utf8')
            data = data.read()
            final_list = []

            for word in set(data.splitlines()):
                temp_list = [f"{word}", data.count(word)]
                final_list.append(tuple(temp_list))
                temp_list = []

            logging.info(f""" '{file_path}'  word count is : {final_list}""")
            return final_list
        except Exception as e:
            logging.error(e)

    def start_with_same_alphabate(self, file_path):
        """This function return a list of tuple with count of all the word starting with same alphabet
        sample example = [(a,56) , (b,34),...........]"""

        try:
            data = open(file_path, encoding='utf8')
            data = data.read()
            final_list = []
            print(type(data.splitlines()))
            for word in set(data.splitlines()):

                print()

        except Exception as e:
            logging.error(e)

    def remove_punc_number(self, file_path):
        """This function filter out of all word of file and return a new string
            .001.abstract = abstract
            =.002 = delete"""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
        try:
            data = open(file_path, encoding='utf8')
            data = data.read()
            final_list = []
            # print(type(data.splitlines()))
            x = [''.join(i for i in item if i not in punc) for item in data.splitlines()]
            return x

            # for word in len(data.splitlines()):
            #     if word in punc:
            #         data = data.replace(word, "")
            # logging.info(x)
        except Exception as e:
            logging.error(e)

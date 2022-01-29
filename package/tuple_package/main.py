import logging

FORMAT = '%(levelname)s || %(asctime)s || %(message)s || %(funcName)s || %(lineno)d '
logging.basicConfig(filename="tuple.log", format=FORMAT, level=logging.INFO)


class TupleParsing:
    def __init__(self, t):
        logging.info("Class __init__ method initialize tuple and check for valid tuple")
        if type(t) == tuple:
            self.t = t
            logging.info(f"tuple is : {self.t}")
        else:
            logging.exception(f"{t} object is not a tuple object! Please Enter A valid tuple")
            raise AttributeError(f"{t} object is not a tuple object! Please Enter A valid tuple")

    def get_tuple(self):
        """This function Return tuple"""
        logging.info("get_tuple function called.")
        return self.t

    def count_tuple(self, value):
        """this function count number of value which you pass in function """
        count = 0
        logging.info("count_tuple function called")
        for i in self.t:
            if i == value:
                count = count+1
        return count

    def index_tuple(self, value):
        """This function return list all index of value which you pass"""
        logging.info("index_tuple function called")
        index_list = []
        for i in range(len(self.t)):
            if self.t[i] == value:
                index_list.append(i)
        return index_list


a=TupleParsing((1,2,3,4,3,4,5,2,3,4,22,333,3,2))
print(a.get_tuple())
print(a.count_tuple(2))
print(a.index_tuple(2))
import logging

FORMAT = '%(levelname)s || %(asctime)s || %(message)s || %(funcName)s || %(lineno)d '
logging.basicConfig(filename="list.log", format=FORMAT, level=logging.INFO)


class ListParsing:
    def __init__(self,l):
        logging.info("Class __init__ method initialize list and check for valid list")
        if type(l) == list:
            self.new_list = []
            self.l = l
            logging.info(f"list is : {self.l}")

        else:
            logging.exception(f"{l} object is not a list object! Please Enter A valid List")
            raise AttributeError(f"{l} object is not a list object! Please Enter A valid List")

    def get_list(self):
        """this function return list which we pass in list_parsing class"""
        logging.info("get_list function called.")
        return self.l

    def append_list(self, value):
        """This function add item in list without change in list like
             eg. [1,3,2].append_list([4,5,6])
             output:[1,3,2,[4,5,6]]
        """
        logging.info("append_list function called")
        try:
            value = [value]
            self.l = self.l + value
            return self.l
        except Exception as e:
            logging.exception(e)

    def clear_list(self):
        """This function clear list (empty list)"""
        logging.info("clear_list function called")
        self.l = []
        return self.l

    def copy_list(self):
        """This function create a new copy of list."""
        logging.info("copy_list function called")
        new_list = self.l.copy()
        return new_list

    def count_list(self, value):
        """This function count item inside a list. """
        logging.info("copy_list function called")
        try:
            count = 0
            for i in self.l:
                if i == value:
                    count = count+1

            return count
        except Exception as e:
            logging.exception(e)

    def extend_list(self, value):
        """This function extend list like
            eg. [1,3,2].extend_list([4,5,6])
            output:[1,3,2,4,5,6]
        """
        logging.info("extend_list function called")
        try:
            itr_value = iter(value)
        except Exception as e:
            logging.exception(e)
            return e
        else:
            self.l = self.l + list(value)
            return self.l

    def index_list(self, value):
        """This function return list of all index of value which you pass """
        logging.info("index_list function called")

        try:
            index_list = []
            for i in range(len(self.l)):
                if self.l[i] == value:
                    index_list.append(i)
            if len(index_list) != 0:
                return index_list
            else:
                return "Value not found in list"
        except Exception as e:
            logging.exception(e)

    def insert_list(self, index, value):
        """This function insert item in specific index of list
        first parameter is index value
        second is parameter is value which we want to inserted """
        logging.info("insert_list function called")
        try:
            self.l = self.l[:index] + [value] + self.l[index:]
            return self.l
        except Exception as e:
            logging.exception(e)

    def pop_list(self):
        """This function remove item from last in list"""
        logging.info("pop_list function called")
        try:
            if len(self.l) == 0:
                self.custom_exception("List has Zero Item.")
            else:
                self.l = self.l[:-1]
        except IndexError as e:
            logging.exception(e)
            return e
        else:
            return self.l

    def custom_exception(self, msg):
        """this function raise custom exception"""
        raise IndexError(f"{msg}")

    def remove_list(self, value):
        """This function remove first match value which you pass"""
        logging.info("remove_list function called")
        temp_list = self.l.copy()
        try:
            self.l = self.clear_list()
            flag = True
            for i in temp_list:
                if flag:
                    if i == value:
                            flag = False
                            continue
                    else:
                        self.l.append(i)
                else:
                    self.l.append(i)

            return self.l
        except Exception as e:
            logging.exception(e)

    def reverse_list(self):
        """This function reverse a list"""
        logging.info("reverse_list function called")
        return self.l[::-1]

    def sort_list(self):
        """This function sort list item if list has all int"""
        logging.info("reverse_list function called")
        temp_list = self.l.copy()
        try:
            new_list = []
            while self.l:
                min = self.l[0]
                for i in self.l:
                    if i < min:
                        min = i
                new_list.append(min)
                self.l = self.remove_list(min)
            self.l = new_list
        except Exception as e:
            logging.exception(e)
        return self.l


a = ListParsing([1,2,3,3,3-9,-4,3,0,3,30,5,34])
print(a.get_list())
# print(a.pop_list())
# print(a.clear_list())
# print(a.reverse_list())
# print(a.remove_list(3))
# print(a.sort_list())
# print(a.index_list(3))
# print(a.count_list(3))
# print(a.copy_list())
# print(a.extend_list(12))
# print(a.insert_list(3,12))


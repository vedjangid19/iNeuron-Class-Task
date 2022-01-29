import logging

FORMAT = '%(levelname)s || %(asctime)s || %(message)s || %(funcName)s || %(lineno)d '
logging.basicConfig(filename="dict.log", format=FORMAT, level=logging.INFO)


class DictParsing:
    def __init__(self, d):
        logging.info("Class __init__ method initialize dict and check for valid dict")
        if type(d) == dict:
            self.d = d
            logging.info(f"dict is : {d}")
        else:
            logging.exception("f{d} object is not a dictionary object! Please Enter A valid dictionary Object")
            raise AttributeError("f{d} object is not a dictionary object! Please Enter A valid dictionary Object")

    def get_dict(self):
        """this function return dictionary"""
        logging.info("get_dict function called.")
        return self.d

    def get_dict_value(self, key):
        """this function get value of key which you pass to function
        eg: dict={"a":1,"b":2,"c":3}
            get_dict_value("b")
            output:2
            """
        logging.info("get_dict_value function called.")
        try:
            return self.d[key]
        except Exception as e:
            logging.exception(e)
            return e

    def keys_dict(self):
        """This function return a list of dictionary all keys
        eg:dict={"a":1,"b":2,"c":3}
            dict.keys_dict()
            output:["a","b","c"]
            """
        logging.info("keys_dict function called.")

        return self.d.keys()

    def values_dict(self):
        """This function return a list of dictionary all values
        eg:dict={"a":1,"b":2,"c":3}
            dict.values_dict()
            output:[1,2,3]
            """
        logging.info("values_dict function called.")

        return self.d.values()

    def clear_dict(self):
        """this function remove all elements from a dictionary
        eg:dict={"a":1,"b":2,"c":3}
            dict.clear_dict()
            output:{}
            """
        logging.info("clear_dict function called.")

        self.d = {}
        return self.d

    def copy_dict(self):
        """this function return a copy of dictionary"""
        logging.info("copy_dict function called.")

        return self.d.copy()

    def fromkeys_dict(self, key, value=None):
        """This function return a dictionary like
        eg: key=("A","B","C","D") #Iterable object
            value=(1,2,3,4) # 0
            dict.fromkeys_dict(key,value)
            output:{"A":1,"B":2,"C":3,"D":4}
            """
        pass
        # try:
        #     if len(key) != 0:
        #         _ = iter(key)
        #     else:
        #         if len(key) == len(value)
        # except Exception as e:
        #     print(e)

    def update_dict(self, d1):
        """this function insert key value in dictionary
        eg: x ={"a":1,"b":2,"c":3}
            x.update_dict({"d":4})
            output:x = {"a":1,"b":2,"c":3,"d":4}
            """
        logging.info("update_dict function called.")

        d1_keys = list(d1.keys())
        d1_values = list(d1.values())

        try:
            for i in range(len(d1_keys)):
                self.d[d1_keys[i]] = d1_values[i]

            return self.d
        except Exception as e:
            logging.exception(e)
            return self.d

    def pop_dict(self, key):
        """This function remove element from dictionary corresponding to key
        eg:x ={"a":1,"b":2,"c":3}
            pop_dict("c")
            output:x = {"a":1,"b":2}
            """
        logging.info("pop_dict function called.")

        try:
            del self.d[key]
        except Exception as e:
            logging.exception(e)

        return self.d

    def popitem_dict(self):
        """this function remove last element of dictionary
            eg: x ={"a":1,"b":2,"c":3}
                popitem_dict()
                output:x = {"a":1,"b":2}
            """
        logging.info("popitem_dict function called.")
        try:
            del self.d[list(self.keys_dict())[-1]]
            return self.d
        except Exception as e:
            logging.exception(e)
            return self.d


o = DictParsing({"a":1,"b":2,"c":3})
print(o.get_dict())
print(o.get_dict_value("d"))
# print(o.keys_dict())
# print(o.values_dict())
# print(o.clear_dict())
# print(o.copy_dict())
# print(o.update_dict({"ved":"jangid","l":[6,7,8,9]}))
# print(o.pop_dict("b"))
print(o.popitem_dict())
print(o.get_dict())


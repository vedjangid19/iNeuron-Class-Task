import logging

FORMAT = '%(levelname)s || %(asctime)s || %(message)s || %(funcName)s || %(lineno)d '
logging.basicConfig(filename="set.log", format=FORMAT, level=logging.INFO)


class SetParsing:
    def _init_(self, value):
        logging.info("Class __init__ method initialize set and check for valid set")

        if type(value) == set:
            self.s = value
            logging.info(f"set is : {self.s}")

        else:
            logging.exception(f"{value} object is not a set object! Please Enter A valid set")
            raise AttributeError(f"{value} object is not a set object! Please Enter A valid set")

    def get_set(self):
        """this function return set"""
        logging.info("get_set function called.")

        return self.s

    def add_set(self, value):
        """This function Add item Into set"""
        logging.info("add_set function called.")
        try:
            self.s = set(list(self.s) + list(value))
            return self.s
        except Exception as e:
            logging.exception(e)
            return self.s

    def clear_set(self):
        """This function return blank set (its clear all items in set)"""
        logging.info("clear_set function called.")

        self.s = set(list())
        return self.s

    def pop_set(self):
        """This function return a value which extract from set and update set
           eg: s = {1,2,3,4}
           s.pop_set()
           output : 1
                s : {2,3,4}
        """
        logging.info("pop_set function called.")
        try:
            pop_value = list(self.s)[0]
            self.s = set(list(self.s)[1:])
            return pop_value
        except Exception as e:
            logging.exception(e)

    def copy_set(self):
        """this function create new copy of set"""
        logging.info("copy_set function called.")

        new_set = self.s.copy()
        return new_set

    def remove_set(self, value):
        """this function remove specific item from set
            eg:
                s = {1,2,3,4}
                s.remove_set(3)
                output: s : {1,2,4}
        """
        logging.info("remove_set function called.")

        try:
            new_set = list(self.s)
            value_index = new_set.index(value)
            self.s = set(new_set[:value_index] + new_set[value_index+1:])
            return self.s
        except Exception as e:
            logging.exception(e)

    def update_set(self, set2):
        """This function update set
            eg: set1 = {1,2,3}
                set2 = {"A","B","C"}
                update_set(set1,set2)
                Output : set1 = {1,2,3,"A","B","C"}
                        set2 = {"A","B","C"}
            """
        logging.info("update_set function called.")
        try:
            self.s = set(list(self.s)+list(set2))
            return self.s
        except Exception as e:
            logging.exception(e)

    def difference_set(self, set2):
        """The returned set contains items that exist only in the first set, and not in both sets.
            eg: s1 = {1,2,3}
                s2 = {"A",3,"C"}
                s1.difference_set(set2)
                Output : s1 = {1,2}
                         s2 = {"A",3,"C"}
            """
        logging.info("difference_set function called.")
        try:
            match_item = self.intersection_set(self.s, set2)
            self.s = self.s - match_item
            return self.s
        except Exception as e:
            logging.exception(e)
            return self.s

    def intersection_set(self, s2):
        """ this function returned new set contains items that exist in both set
            eg:  x = {"apple", "banana", "cherry"}
                 y = {"google", "microsoft", "apple"}
                 x.intersection_set(y)
                 Output : {"apple"}
                 """
        logging.info("intersection_set function called.")
        try:
            l = []
            for item in self.s:
                if item in s2:
                    l.append(item)
            return set(l)
        except Exception as e:
            logging.exception(e)

    def discard_set(self, value):
        """This function method removes the specified item from the set.
            eg s = {1,2,3,4}
                s.discard_set(3)
                output: {1,2,4}
        """
        logging.info("discard_set function called.")

        if value in self.s:
            self.s = self.s - {value}
            return self.s
        else:
            try:
                raise AttributeError(f"{value} not found in set {self.s}")
            except Exception as e:
                logging.exception(e)
                return e

    def intersection_update_set(self, s2):
        """ this function returned first set contains items that exist in both set
            eg:  x = {"apple", "banana", "cherry"}
                 y = {"google", "microsoft", "apple"}
                 x.intersection_update_set(y)
                 print(x)
                 Output : {"apple"}
                 """
        logging.info("intersection_update_set function called.")

        self.s = self.intersection_set(self.s, s2)
        return self.s

    def isdisjoint_set(self, set1):
        """returns True if none of the items are present in both sets, otherwise it returns False."""
        logging.info("isdisjoint_set function called.")

        flag = False
        for item in self.s:
            if item in set1:
                flag = True
                break
        return flag

    def union_set(self, set1):
        """This function return set of all element of original set and all element of specific set."""
        logging.info("union_set function called.")

        self.s = set(list(self.s) + list(set1))
        return self.s

    def symmetric_difference_update(self, set1):
        """This function return a set of all items of both set
            but not the items that are present in both set.
            eg : x = {"apple", "banana", "cherry"}
                 y = {"google", "microsoft", "apple"}
                 z = x.symmetric_difference(y)
                 output : z = {'google', 'microsoft', 'banana', 'cherry'}
                """
        logging.info("symmetric_difference_update function called.")
        try:
            match_items = self.intersection_set(self.s, set1)
            self.s = set(list(self.s) + list(set1)) - match_items
            return self.s
        except Exception as e:
            logging.exception(e)
            return self.s

    def issubset_set(self, set1):
        """this function return True if all items of set exist in specific set otherwise return False."""
        logging.info("issubset_set function called.")

        flag = True
        for item in self.s:
            if item not in set1:
                flag = False
                break

        return flag


a = SetParsing({1,2,3,4})
print(a.get_set())
# print(a.add_set([2222,222222]))
# print(a.pop_set())
# print(a.clear_set())
# print(a.copy_set())
# print(a.remove_set("ved "))
# s1 = {1,2,3,4,5,67,88,99,33,0}
# s2 = {"ved","jangid",3,88,0}
# print(a.update_set(s1,s2))
# print(a.intersection_set(s1,s2))
# print(a.difference_set(s1,s2))
# print(a.discard_set(88))
# print(a.intersection_update_set({2,3,6,7,8,0}))
# print(a.get_set())
# print(a.isdisjoint_set({1,11,22,33,44}))
# print(a.union_set({1,2,11,22,33,44}))
# print(a.symmetric_difference_set({1,2,11,22,33,44}))
# print(a.issubset_set({1,2,11,22,3,33,4,44}))
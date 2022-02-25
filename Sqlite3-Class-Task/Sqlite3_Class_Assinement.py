import logging
from itertools import groupby
import sqlite3
import pandas as pd
import numpy as np

FORMAT = '%(levelname)s || %(asctime)s || %(module)s  || %(funcName)s  ||  %(lineno)d  ||  %(message)s'
logging.basicConfig(filename="Bag of word.log", format=FORMAT, level=logging.INFO)


class BagOfWord:
    def __init__(self):
        self.dataframe = pd.DataFrame()


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

            logging.info(f""" '{file_path}'  word count is : {final_list}""")
            return final_list

        except Exception as e:
            logging.error(e)

    def start_with_same_alphabate(self, file_path):
        """This function return a list of tuple with count of all the word starting with same alphabet
            sample example = [(a,56) , (b,34),...........]"""

        try:
            temp_list = self.remove_punc_number(file_path)
            temp_list = [i for i in temp_list if i]
            list1 = [(i, len(list(j))) for i, j in groupby(temp_list, key=lambda x: x[0])]

            logging.info(f""" '{file_path}'  word count start with same character is : : {list1}""")
            return list1

        except Exception as e:
            logging.error(e)

    def remove_punc_number(self, file_path):
        """This function filter out of all word of file and return a new string
            .001.abstract = abstract
            =.002 = delete"""
        punc = '''!()-[]{};:'"\,<>./=+?@#$%^&*_~0123456789'''
        try:
            data = open(file_path, encoding='utf8')
            data = data.read()
            x = [''.join(i for i in item if i not in punc) for item in data.splitlines()]
            logging.info(f""" '{file_path}'  remove punctution and number : {x}""")
            return x

        except Exception as e:
            logging.error(e)

    def create_database(self, DBName, filename):
        """Create database """
        try:
            conn = sqlite3.connect(DBName+'.db')
            query = f"""CREATE TABLE IF NOT EXISTS BAGOFWORD (
                    filename0 VARCHAR(250), 
                    filename1 VARCHAR(250),
                    filename2 VARCHAR(250),
                    filename3 VARCHAR(250),
                    filename4 VARCHAR(250)
                    );
                    """
            # print(query)
            conn.execute(query)
            logging.info(f"Databse '{DBName}' and table 'BAGOFWORD' created")
        except Exception as e:
            logging.error(e)
            return f"Something wrong in careation of database and table : {e}"
        return conn

    def insert_data(self, database_name, filename):
        """This function create database and create table with respect to filename as column"""
        conn = self.create_database(database_name, filename)

        try:
            for file in filename:
                data = open(file, encoding='utf8')
                data = data.read()
                column_value = data.splitlines()
                self.dataframe[file] = pd.Series(column_value)

            self.dataframe = self.dataframe.replace(np.nan, '', regex=True)
            record = self.dataframe.to_records(index=False)
            cursor = conn.cursor()
            cursor.executemany("insert into BAGOFWORD(filename0, filename1, filename2, filename3, filename4) values (?,?,?,?,?)", record)
            conn.commit()
            logging.info("Successfully Insert data in to database table")
        except Exception as e:
            logging.error(e)
            print(e)
        return "Successfully Insert data in to database table"
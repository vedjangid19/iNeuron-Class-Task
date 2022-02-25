import pymongo
import logging
import csv
import pandas as pd

FORMAT = '%(levelname)s || %(asctime)s || %(module)s  || %(funcName)s  ||  %(lineno)d  ||  %(message)s'
logging.basicConfig(filename="carbon_nano_tubes.log", format=FORMAT, level=logging.INFO)


class CarbonNanoTube:
    def __init__(self):
        self.client = ""
        self.db = ""
        self.db1 = ""
        self.coll = ""

    def make_connection(self, connection_url):
        """this function make connection to cluster and take parameter cluster name and password."""
        try:
            self.client = pymongo.MongoClient(connection_url)
            self.db = self.client.test
            logging.info(f"connection establish {self.db}")
            return self.db
        except Exception as e:
            logging.error(f"{e}")
            return e

    def create_database(self, dbname):
        """this function create database and take a parameter as database name."""
        try:
            self.db1 = self.client[dbname]
            logging.info(f"'{dbname}' Database Create successfully")
            return "Database Create successfully"
        except Exception as e:
            logging.error(f"e")
            print(e)

    def create_collection(self, collection_name):
        """this function create collection and take a parameter as collection name."""
        try:
            self.coll = self.db1[collection_name]
            logging.info(f"'{collection_name}' Collection Create successfully")
            return "Collection Create successfully"
        except Exception as e:
            logging.error(f"e")
            print(e)

    def insert_bulk_data(self, file_path):
        """this function insert bulk data from csv file (Remainder is canbon nanotubes csv file has delimeter is ;
        please check csv delimeter its has ";" before insert bulk data), it take a parameter as file_path(only csv
        file)"""
        try:
            if file_path.lower().endswith('.csv'):
                data_frame = pd.read_csv(file_path, delimiter=";")
                record = data_frame.to_dict('records')
                self.coll.insert_many(record)
                logging.info("Bulk insert Success")
            else:
                logging.warning("Please Select CSV File.")
                return "Please Select CSV File."
        except Exception as e:
            logging.error(e)
    def insertion(self, document):
        """this function insert one document into collection"""
        try:
            self.coll.insert_one(document)
            logging.info(f"Successfully insert document with respect query : {document}")
        except Exception as e:
            logging.error(f"{e}")
            print(e)

    def update_document(self, search_query, set_query):
        """this function update document with respect search query."""
        try:
            self.coll.update_many(search_query, set_query)
            logging.info(f"Successfully update document with respect query : {search_query} set value {set_query}")
        except Exception as e:
            logging.error(f"{e}")
            print(e)

    def delete_document(self, dict_query):
        """this function delete document"""
        try:
            self.coll.delete_one(dict_query)
            logging.info(f"Successfully delete document with respect query : {dict_query}")
        except Exception as e:
            logging.error(f"{e}")
            print(e)

    def find_document(self, search_query):
        """this function find all document with respect search query."""
        try:
            document_list = self.coll.find(search_query)
            logging.info(f"Successfully find document with respect search query : {search_query}")
            return document_list
        except Exception as e:
            logging.error(f"{e}")
            print(e)
            return []

    def filter_document(self, search_query):
        """this function filter documents"""
        try:
            document_list = self.coll.find(search_query)
            logging.info(f"Successfully find document with respect search query : {search_query}")
            return document_list
        except Exception as e:
            logging.error(f"{e}")
            print(e)
            return []


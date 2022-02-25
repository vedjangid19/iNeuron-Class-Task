import glob
import Sqlite3_Class_Assinement


def read_folder_file(path):
    """this function read all file of folder and return a list of file name."""
    try:
        filename_list = glob.glob(path)
        # logging.info(f"{path} folder files are {self.filename_list}")
        return filename_list
    except Exception as e:
        # logging.error(e)
        print(e)


a = Sqlite3_Class_Assinement.BagOfWord()

filename = read_folder_file("dataset\*.txt")
# x = map(read_folder_file())

# for file in filename:
#     print(f"'{file}'  word count is : {a.count_of_word(file)}")

# for file in filename:
#     print(f"'{file}'  word count is : {a.start_with_same_alphabate(file)}")

for file in filename:
    print(f"'{file}'  remove punctution and number : {a.remove_punc_number(file)}")




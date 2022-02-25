import glob
import Sqlite3_Class_Assinement


def read_folder_file(path):
    """this function read all file of folder and return a list of file name."""
    try:
        filename_list = glob.glob(path)
        return filename_list
    except Exception as e:
        print(e)


a = Sqlite3_Class_Assinement.BagOfWord()
filename = read_folder_file("dataset\*.txt")

# for file in filename:
#     print(f"'{file}'  word count is : {a.count_of_word(file)}")

# for file in filename:
#     print(f"'{file}'  word count start with same character is : {a.start_with_same_alphabate(file)}")

# for file in filename:
#     print(f"'{file}'  remove punctution and number : {a.remove_punc_number(file)}")

a.insert_data("Dataset", filename)


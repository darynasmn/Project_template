from app.io.input import input_text_from_console as input_console
from app.io.input import read_from_file_with_builtin as read_builtin
from app.io.input import read_from_file_with_pandas as read_pandas
from app.io.output import print_to_console
from app.io.output import write_to_file_with_builtin as write_to_file

def main():

    text_from_console = input_console()

    content_from_builtin = read_builtin("data/test.txt")

    data_from_pandas = read_pandas("data/test_csv.csv")
    all_texts = [text_from_console, content_from_builtin, str(data_from_pandas)]
    all_texts_str = '\n'.join(map(str, all_texts))
    
    print_to_console(all_texts)
    write_to_file("data/output.txt", all_texts_str)
    

if __name__ == "__main__":
    main()

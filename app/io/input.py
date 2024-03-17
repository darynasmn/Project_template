import pandas as pd
def input_text_from_console():
    """
    Function to input text from the console.

    Returns:
        str: Text input by the user.

    Raises:
        Exception: If an error occurs during input.
    """
    try:
        text = input("Enter text: ")
        return text
    except Exception as e:
        raise Exception("An error occurred during input.") from e

def read_from_file_with_builtin(file_path):
    """
    Function to read content from a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: Content read from the file.

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
        Exception: If an error occurs during file reading.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found at path: {file_path}") from e
    except Exception as e:
        raise Exception(f"An error occurred during file reading: {e}") from e

def read_from_file_with_pandas(file_path):
    """
    Function to read content from a file using the pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        DataFrame: Data read from the file using pandas.

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
        Exception: If an error occurs during file reading.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found at path: {file_path}") from e
    except Exception as e:
        raise Exception(f"An error occurred during file reading: {e}") from e

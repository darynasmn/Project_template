def input_text_from_console():
    """
    Function to input text from the console.

    Returns:
        str: Text input by the user.

    Examples:
        >>> input_text_from_console()
        Enter text: Hello, world!
        'Hello, world!'

    Raises:
        Exception: If an error occurs during input.
    """
    pass

def read_from_file_with_builtin(file_path):
    """
    Function to read content from a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: Content read from the file.

    Examples:
        >>> read_from_file_with_builtin('example.txt')
        'Content of the file.'

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
        Exception: If an error occurs during file reading.
    """
    pass

def read_from_file_with_pandas(file_path):
    """
    Function to read content from a file using the pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        DataFrame: Data read from the file using pandas.

    Examples:
        >>> read_from_file_with_pandas('data.csv')
        pandas DataFrame containing data from the file.

    Raises:
        FileNotFoundError: If the file specified by file_path does not exist.
        Exception: If an error occurs during file reading.
    """
    pass

def print_to_console(text):
    """
    Function to print text to the console.

    Args:
        text (str): The text to be printed to the console.

    Raises:
        Exception: If an error occurs during printing.
    """
    try:
        print(text)
    except Exception as e:
        raise Exception("An error occurred during printing.") from e

def write_to_file_with_builtin(file_path, content):
    """
    Function to write content to a file using Python's built-in capabilities.

    Args:
        file_path (str): The path to the file where content will be written.
        content (str): The content to be written to the file.

    Raises:
        Exception: If an error occurs during file writing.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print("Write operation successful.")
    except Exception as e:
        raise Exception(f"An error occurred during file writing: {e}") from e

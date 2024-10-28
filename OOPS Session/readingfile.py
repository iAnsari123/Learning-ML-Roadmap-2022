import logging


def process_file(file_path):
    """
    Process the file to replace occurrences of '1' with the line number + 1 after encountering a line containing '10'.

    Args:
        file_path (str): The path to the file to be processed.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs.
    """
    to_be_replaced = False

    try:
        with open(file_path, "r") as f:
            for num, line in enumerate(f):
                line = line.strip("\n")
                if "10" in line:
                    to_be_replaced = True
                    print(line)
                    continue
                if to_be_replaced:
                    line = line.replace("1", str(num + 1))
                print(line)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except IOError as e:
        logging.error(f"An I/O error occurred: {e}")


# Example usage:
process_file("demofile.txt")


import logging
import getpass


def password_manager(mode: str = "pass") -> str:
    """
    Manages passwords based on the specified mode.

    Parameters:
    mode (str): The mode to perform the operation ('view' to view passwords, 'add' to add a new password).

    Returns:
    str: Returns the passwords if 'view' mode is selected, or a success message if 'add' mode is selected.

    Raises:
    FileNotFoundError: If the passwords file does not exist.
    Exception: If an error occurs while adding a new password.
    """
    logger = logging.getLogger(__name__)

    if mode == "view":
        try:
            with open("./passwords.txt", mode="r") as passwords:
                if passwords.readable():
                    return passwords.read()
        except FileNotFoundError:
            logger.error("File doesn't exist")
        except Exception as e:
            logger.error(f"Error occurred: {e}")
    elif mode == "add":
        try:
            with open("./passwords.txt", mode="a") as passwords:
                website = input("Please enter the website name: ")
                password = getpass.getpass("Please enter the website password: ")

                # Implement secure password handling here (hashing or encryption)
                # Example: hashed_password = hash_function(password)
                # Store hashed_password instead of plain text password

                passwords.write(f"{website}: {password}\n")

                return "Successfully added new password"
        except Exception as e:
            logger.error(f"Error occurred: {e}")
    else:
        logger.error("Please enter mode(view or add)")
        pass


if __name__ == "__main__":
    master_password = "33ahnaf"
    user_answer = input("What is your master password: ")

    if user_answer.lower() == "33ahnaf":
        mode = input("What would you like to do(view password, add password): ").lower()
        print(password_manager(mode=mode))
    else:
        print("Wrong Password")
        quit()

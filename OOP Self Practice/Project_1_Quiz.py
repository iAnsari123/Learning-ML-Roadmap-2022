import numpy as np


def ask_math_questions(num_questions: int = 3) -> int:
    """
    Function to ask multiple-choice math questions and calculate the total marks based on correct answers.

    Args:
        num_questions (int): Number of questions to ask in the quiz.

    Returns:
        int: Total marks obtained by the user.
    """

    first_numbers = np.random.randint(1, 20, num_questions)
    second_numbers = np.random.randint(1, 20, num_questions)

    questions = [
        (
            f"what is {first_numbers[i]} + {second_numbers[i]}: ",
            first_numbers[i] + second_numbers[i],
        )
        for i in range(num_questions)
    ]

    marks = 0

    for question, answer in questions:
        while True:
            try:
                user_answer = int(input(question))
                if user_answer == answer:
                    marks += 1
                break
            except ValueError:
                print("Try giving a numerical value")

    return marks


if __name__ == "__main__":
    user = input("Do you want to play the game: ")
    if user == "y" or user == "Y":
        print(f"Your total obtained marks: {ask_math_questions(num_questions=3)}")
    elif user == "q" or user == "quit":
        quit()

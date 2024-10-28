def calculate_fees(study_branch: str, score: int, course_fee: int):
    """
    Calculate the final fee amount after applying scholarships based on the study branch and score.

    Args:
        study_branch (str): The branch of study (e.g., "arts", "engineering").
        score (int): The student's score.
        course_fee (int): The original fee of the course.

    Returns:
        int: The final fee amount after deducting the scholarship amount.
    """
    scholarship_amount = 0
    study_branch = study_branch.lower()
    if study_branch == "arts":
        if score >= 90:
            scholarship_amount = max(scholarship_amount, course_fee * 0.5)
        if score % 2 != 0:
            scholarship_amount = max(scholarship_amount, course_fee * 0.05)

    elif study_branch == "engineering":
        if score > 85:
            scholarship_amount = max(scholarship_amount, course_fee * 0.5)
        if score % 7 == 0:
            scholarship_amount = max(scholarship_amount, course_fee * 0.05)
    return course_fee - scholarship_amount

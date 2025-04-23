"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = []

    for student in student_scores:
        rounded_scores.append(round(student))

    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    failing = 0

    for student in student_scores:
        if student <= 40:
            failing += 1

    return failing


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the
    provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    the_best = []

    for student in student_scores:
        if student >= threshold:
            the_best.append(student)

    return the_best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    grades = []
    passing = 41
    grade_inc, rest = divmod(highest - passing, 4)

    for idx in range(4):
        if rest == 0:
            grade_threshold = passing + idx * grade_inc
            grades.append(grade_threshold)
        else:
            grade_threshold = (passing + idx * grade_inc) + idx
            grades.append(grade_threshold)

    return grades


print(letter_grades(highest=100))


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    names_and_scores = []

    for idx, student in enumerate(student_names):
        string_rep = f"{idx + 1}. {student}: {student_scores[idx]}"
        names_and_scores.append(string_rep)

    return names_and_scores


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a
    perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is
    found.
    """

    for student in student_info:
        if 100 in student:
            return student

    return []

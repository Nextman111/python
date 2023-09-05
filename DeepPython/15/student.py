import csv
from student_ex import NameError, ValueReadError, IncorrectValueError


class Student:
    def __init__(self, name, csv_filename):
        if not name.istitle() or not name.replace(" ", "").isalpha():
            raise NameError()

        self.name = name
        self.subjects = self.load_subjects_from_csv(csv_filename)
        self.scores = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}

    def load_subjects_from_csv(self, filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            return next(reader)

    def add_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueReadError(subject)

        if 2 > score > 5:
            raise IncorrectValueError(score)

        self.scores[subject].append(score)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueReadError(subject)

        if 0 > result > 100:
            raise IncorrectValueError(result, score_type="Результат теста")

        self.test_results[subject].append(result)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueReadError(subject)

        return sum(self.test_results[subject]) / len(self.test_results[subject]) if self.test_results[subject] else 0

    def average_score(self):
        total_scores = sum([sum(scores) for scores in self.scores.values()])
        total_count = sum([len(scores) for scores in self.scores.values()])
        return total_scores / total_count if total_count else 0
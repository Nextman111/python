class NameError(Exception):
    def __init__(self, message="Имя студента должно состоять только из букв и начинаться с заглавной буквы."):
        self.message = message
        super().__init__(self.message)

class ValueReadError(Exception):
    def __init__(self, subject):
        self.subject = subject
        self.message = f"Предмет '{subject}' не найден в файле CSV."
        super().__init__(self.message)

class IncorrectValueError(Exception):
    def __init__(self, score, score_type="Оценка"):
        self.score = score
        self.message = f"Ошибка значения {score_type} '{score}'. Оценки должны быть (от 2 до 5), а результаты тестов (от 0 до 100)."
        super().__init__(self.message)
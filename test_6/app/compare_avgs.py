class CompareAvgs:

    STR_1 = "Первый список имеет большее среднее значение"
    STR_2 = "Второй список имеет большее среднее значение"
    STR_3 = "Средние значения равны"

    def calc_avg(self, list_1: list[int]) -> float:
        if list_1:
            return sum(list_1) / len(list_1)

    def compare_avgs(self, list_1, list_2) -> str:
        if self.calc_avg(list_1) > self.calc_avg(list_2):
            result = self.STR_1
        elif self.calc_avg(list_1) < self.calc_avg(list_2):
            result = self.STR_2
        else:
            result = self.STR_3
        return result
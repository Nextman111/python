import pytest

from test_6.app.compare_avgs import CompareAvgs


class TestCompareAvgsOfLists():

    def setup(self) -> None:
        self.avgs = CompareAvgs()

    def teardown(self) -> None:
        print('Calculation done')

    @pytest.fixture
    def list_2(self) -> list[int]:
        """ list_2 is constant. """
        return [1, 2, 3]

    @pytest.fixture
    def empty_list(self):
        """ Empty list. """
        return []

    @pytest.mark.positive
    def test_calc_avg(self, list_2):
        """ Calculation of list average check. """
        assert self.avgs.calc_avg(list_2) == 2

    @pytest.mark.positive
    @pytest.mark.parametrize('list_1', [[10, 20, 30], [1, 1, 1, 1, 1], [1, 2, 3]],
                             ids=['больше первое', 'больше второе', 'равны'])
    def test_compare_avgs(self, list_1, list_2):
        """ Comparing of list averages check. """
        assert (self.avgs.compare_avgs(list_1, list_2) == CompareAvgs.STR_1 or
                self.avgs.compare_avgs(list_1, list_2) == CompareAvgs.STR_2 or
                self.avgs.compare_avgs(list_1, list_2) == CompareAvgs.STR_3)

    @pytest.mark.negative
    def test_calc_avg_null_list(self, empty_list):
        """ Average calculation of empty list check. """
        assert self.avgs.calc_avg(empty_list) is None

    @pytest.mark.negative
    def test_compare_avgs_null_list(self, empty_list, list_2):
        """ Comparing of empty list averages check. """
        with pytest.raises(TypeError):
            self.avgs.compare_avgs(empty_list, list_2)


if __name__ == '__main__':
    pytest.main(['-v'])

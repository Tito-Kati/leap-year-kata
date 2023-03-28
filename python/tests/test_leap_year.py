from src.leap_year import LeapYear


class TestLeapYear:

    def test_returns_false_if_year_not_divisible_by_4_like_1999(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(1999) == False

    def test_returns_false_if_year_not_divisible_by_4_like_2001(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(2001) == False

    def test_returns_true_if_year_divisible_by_4_like_1996(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(1996) == True

    def test_returns_true_if_year_divisible_by_4_like_1992(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(1992) == True

    def test_returns_false_if_year_divisible_by_100_but_not_by_400_like_1700(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(1700) == False

    def test_returns_false_if_year_divisible_by_100_but_not_by_400_like_1900(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(1900) == False

    def test_returns_true_if_year_divisible_by_400_like_1600(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(1600) == True

    def test_returns_true_if_year_divisible_by_400_like_2000(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(2000) == True

from src.leap_year import LeapYear


class TestLeapYear:

    def test_returns_false_if_year_not_divisible_by_4(
        self,
    ):
        # Given
        leap_year = LeapYear()
        # When

        # Then
        assert leap_year.is_leap_year(1999) == False

    def test_returns_true_if_year_divisible_by_4(
        self,
    ):
        leap_year = LeapYear()
        assert leap_year.is_leap_year(1996) == True

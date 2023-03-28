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

class LeapYear:

    def is_leap_year(
        self,
        year
    ) -> bool:
        if year % 100 == 0:
            return False

        return year % 4 == 0

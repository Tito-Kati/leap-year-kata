class LeapYear:

    def is_leap_year(
        self,
        year
    ) -> bool:
        if year % 4 == 0:
            return True

        return False

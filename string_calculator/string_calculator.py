class StringCalculator:
    def add(self, value: str) -> int:
        if not value:
            return 0

        value_list = value.split(",")
        return sum(map(int, value_list))

import re


class StringCalculator:
    def add(self, value: str) -> int:
        if not value:
            return 0

        if value.startswith("//"):
            delimeter, value = value[2:].split("\n")
        else:
            delimeter = ',|\n'


        value_list = re.split(delimeter, value)
        return sum(map(int, value_list))

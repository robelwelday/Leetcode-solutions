class Solution:
    def intToRoman(self, num: int) -> str:
        final = ""  # the final roman number
        coll = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        for size, roman in coll:  # iterate through the roman numbers
            while num >= size:
                num -= size
                final += roman  # append the roman symbol to the result
        return final
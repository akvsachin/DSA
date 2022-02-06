class Solution:
    def trailingZeroes(self, n: int) -> int:
        factors_of_5, factor = 0, 5
        while factor <= n:
            factors_of_5 += n//factor
            factor *= 5
        return factors_of_5

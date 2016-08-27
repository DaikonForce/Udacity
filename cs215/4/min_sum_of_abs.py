#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
#
# Your code should run in Theta(n) time
# to understand answer use: http://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations
import statistics


def minimize_absolute(L):
    # the value of x in SUM_{i=0}^{n-1} |L[i] - x| is the median of L.
    return statistics.median(L)

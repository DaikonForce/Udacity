#
# Given a list of numbers, L, find a number, a, that
# minimizes the sum of the square of the difference
# between each element in L and x: SUM_{i=0}^{n-1} (L[i] - a)^2
#
# Your code should run in Theta(n) time
# answer derived from http://mathworld.wolfram.com/LeastSquaresFitting.html setting R^2 = sum[(y_i - f(a))^2]
# -> partial(R^2)/partial(a) = 0 = -2 sum[y_i-a] = 2*a*n - 2*sum[y_i]
# -> a = sum[y_i]/n


def minimize_square(L):
    # look at lines 7-9 for derivation
    a = float(sum(L))/float(len(L))
    return a

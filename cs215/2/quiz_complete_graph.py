#
# How many edges in a complete graph on n nodes?
#


def clique(n):
    """Returns number of edges"""
    # Return the number of edges
    # Number of edges is a triangle of the number of nodes-1
    if type(n) == int:
        if n >= 1:
            n -= 1
            return n*(n+1)//2
    print("Error: clique only takes in integers >= 1")
    return None

if __name__ == '__main__':
    print(clique(1))
    print(clique(2))
    print(clique(3))

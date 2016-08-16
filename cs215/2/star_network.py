# returns number of edges in a star network graph
# a star network is a graph that has a node at the center that is connected to all the other nodes.


def star_network(n):
    """ returns number of edges in a star network graph given number of nodes n"""
    return n-1  # since only 1 node is connected to all the other nodes there is 1 connect per node, but the don't count the center node


def main():
    """ main for star_network.py"""
    for i in range(1, 10):
        print(star_network(i))

if __name__ == '__main__':
    main()

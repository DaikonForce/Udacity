# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


def find_eulerian_tour(graph):
    """input: a graph of edges
    output: a list of nodes that the tour follows"""
    odds = find_odd(graph)
    if not odds:  # if there are no odd values
        return fill_tour(graph, graph[0][0])
    elif len(odds) == 2:  # if there are 2 even values
        return fill_tour(graph, odds[0])
    else:  # anything else and it won't work(?) maybe only if even number of odd values
        print("Error: There is no possible tour. find_eulerian_tour function failed.")
        return -1


def find_odd(graph):
    """input: a graph of edges
    output: all odd nodes in the graph"""
    flat = sorted([item for sublist in graph for item in sublist])
    tmp_node = flat[0]
    count = 0
    odds = []
    for node in flat:
        if (node == tmp_node):
            count += 1
        else:
            if count % 2 == 1:
                odds.append(tmp_node)
            count = 1
        tmp_node = node
    if odds:
        return odds
    else:
        return None


def find_in_graph(graph, node_value):
    """input: graph of edges, a node
    output: the location of the node in the graph"""
    flat = [item for sublist in graph for item in sublist]
    node_location = flat.index(node_value)
    return [node_location // 2, node_location % 2]


def fill_tour(graph, node_value):
    """Returns a tour given a graph and a start value"""
    node_location = find_in_graph(graph, node_value)  # location in the graph
    tour = []
    edge = graph.pop(node_location[0])
    tour.append(edge[node_location[1]])
    tour.append(edge[node_location[1]-1])
    while graph:
        try:
            node_location = find_in_graph(graph, tour[-1])
            edge = graph.pop(node_location[0])
            tour.append(edge[node_location[1]-1])
        except:
            print("Error: There is no possible tour. fill_tour function failed.")
            raise
    return tour


if __name__ == '__main__':
    print(find_eulerian_tour([(4, 5), (2, 3), (1, 2),  (5, 6), (3, 4), (6, 1), (3, 1)]))
    print(find_eulerian_tour([(1, 2), (2, 3), (3, 1)]))

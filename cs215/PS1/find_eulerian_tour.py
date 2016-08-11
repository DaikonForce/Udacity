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
    graph = graph[:]
    odds = find_odd(graph)
    if not odds:  # if there are no odd values
        graph = reorder(graph, graph[0][0])
        return fill_tour(graph, graph[0][0])
    elif len(odds) == 2:  # if there are 2 even values
        graph = reorder(graph, graph[0][0])
        return fill_tour(graph, odds[0])
    else:  # anything else and it won't work(?) maybe only if even number of odd values
        print("Error: There is no possible tour. find_eulerian_tour function failed.")
        return -1


def find_odd(graph):
    """input: a graph of edges
    output: all odd nodes in the graph"""
    flat = sorted([item for sublist in graph[:] for item in sublist])
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


def graph_find(graph, node_value):
    """input: graph of edges, a node
    output: the location of the node in the graph"""
    flat = [item for sublist in graph[:] for item in sublist]
    if node_value in flat:
        node_location = flat.index(node_value)
        return [node_location // 2, node_location % 2]
    else:
        return None


def reorder(graph, node_value):
    """reorders a graph so that all but the first values of node_value are in the back of the graph.
    Used to make sure the graph ends on up being a tour"""
    node_location = graph_find(graph[1:], node_value)
    tmp_graph = []
    while node_location:
        x = graph.pop(node_location[0]+1)
        tmp_graph.append(x)
        node_location = graph_find(graph[1:], node_value)
    return graph + tmp_graph


def fill_tour(graph, node_value):
    """Returns a tour given a graph and a start value
    WARNING IT WILL MODIFY GRAPH"""
    node_location = graph_find(graph, node_value)  # location in the graph
    tour = []
    edge = graph.pop(node_location[0])
    tour.append(edge[node_location[1]])
    tour.append(edge[node_location[1]-1])
    graph_backup = []
    while graph:
        node_location = graph_find(graph, tour[-1])
        try:
            edge = graph.pop(node_location[0])
            tour.append(edge[node_location[1]-1])
        except TypeError:  # if there are extra edges untouched, it will return a TypeError
            # so here, we will try to attach the extra nodes to the end of the graph
            tmp_node = None
            for edge in graph:
                for node in edge:
                    if node in tour:
                        tmp_node = node
            if not tmp_node:
                print("Error: No valid Eulerian tour from graph!")
                return -1
            tour2 = fill_tour(graph, tmp_node)  # makes a sub-tour for the leftover bits
            insertion_point = tour.index(tour2[0])
            # we ignore the last point of tour2 because of double counting when inserting.
            tour = tour[:insertion_point] + tour2[:-1] + tour[insertion_point:]
    return tour


def valid_tour(graph, tour):
    """Checks if the tour is a valid tour. Takes in a graph its corresponding tour."""
    i = 0
    l = len(tour)
    graph = graph[:]
    if tour[0] != tour[-1]:  # check if it's a tour (starts and ends at same place)
        return False
    while graph:  # check if the path is a valid path and uses all possible edges
        # for some reason using "if edge in graph" doesn't fucking work
        tmp_edge = (tour[i], tour[i+1])
        for edge in graph:
            if tmp_edge == edge or tmp_edge[::-1] == edge:
                graph.remove(edge)
                edge_removed = 1
                break
        i += 1
        if edge_removed == 0:
            return False
        edge_removed = 0
    return True


if __name__ == '__main__':
    graph1 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    tour1 = find_eulerian_tour(graph1)
    print(tour1)
    print(valid_tour(graph1, tour1))

    graph2 = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9), (5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9), (7, 14),  (10, 13)]
    tour2 = find_eulerian_tour(graph2)
    print(tour2)
    print(valid_tour(graph2, tour2))

    graph3 = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13), (3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19), (1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
    tour3 = find_eulerian_tour(graph3)
    print(tour3)
    print(valid_tour(graph3, tour3))

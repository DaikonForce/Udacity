import collections

# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
#
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1},
#      'b': {'a': 1, 'd': 1},
#      'c': {'a': 1, 'd': 1},
#      'd': {'c': 1, 'b': 1, 'e': 1},
#      'e': {'d': 1, 'g': 1, 'f': 1},
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1}
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'},
#      'b': {'a': 'green', 'd': 'red'},
#      'c': {'a': 'green', 'd': 'green'},
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'},
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'},
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'}
#      }
#


def create_rooted_spanning_tree(G, root):   # may not work on more complex graphs
    S = {node: {} for node in G.keys()}
    open_list = collections.deque([root])
    layer = {node: 0 for node in G.keys()}
    layer[root] = 1
    visited = {root}
    while open_list:
        current = open_list.popleft()
        S[current] = {}
        next_layer = layer[current] + 1
        next_layer_count = 0
        prev_layer = layer[current] - 1
        prev_layer_count = 0
        for neighbor in G[current]:
            # print(neighbor)
            if neighbor not in visited:
                open_list.append(neighbor)
                visited.add(neighbor)
            if neighbor not in S[current].keys():
                S[current][neighbor] = 'green'
                S[neighbor][current] = 'green'
            if not layer[neighbor]:
                layer[neighbor] = next_layer
            else:
                if layer[neighbor] == prev_layer and prev_layer_count < 1:
                    prev_layer_count += 1
                elif layer[neighbor] == next_layer and next_layer_count < 2:
                    next_layer_count += 1
                else:
                    S[current][neighbor] = 'red'
                    S[neighbor][current] = 'red'
    return S


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces


def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    S = create_rooted_spanning_tree(G, "a")
    assert  S == ({'a': {'c': 'green', 'b': 'green'},    # doesn't always fork for some reason...
                   'b': {'a': 'green', 'd': 'red'},
                   'c': {'a': 'green', 'd': 'green'},
                   'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                   'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                   'f': {'e': 'green', 'g': 'red'},
                   'g': {'e': 'green', 'f': 'red'}} or
            S == { 'a': {'b': 'green', 'c': 'green'},
                   'b': {'d': 'green', 'a': 'green'},
                   'c': {'a': 'green', 'd': 'red'},
                   'd': {'b': 'green', 'c': 'red', 'e': 'green'},
                   'e': {'d': 'green', 'f': 'green', 'g': 'green'},
                   'f': {'e': 'green', 'g': 'red'},
                   'g': {'e': 'green', 'f': 'red'}}), "\n S = {0}".format(S)    # this is not all possible permutations


# S = {'a': {'b': 'green', 'c': 'green'},
#      'b': {'d': 'green', 'a': 'green'},
#      'c': {'d': 'red', 'a': 'green'},
#      'd': {'b': 'green', 'c': 'red', 'e': 'green'},
#      'e': {'g': 'green', 'd': 'green', 'f': 'green'},
#      'f': {'g': 'red', 'e': 'green'},
#      'g': {'f': 'red', 'e': 'green'}}
###########


def post_order(S, root):    # broken, probably keep idea of locking nodes until usable
    open_list = [root]
    po = {}
    po_counter = 1
    locked = {root}
    layer = {node: 0 for node in S.keys()}
    layer[root] = 1
    while open_list:
        current = open_list.pop()
        unused_green = 0
        for neighbor in S[current]:
            if S[current][neighbor] == 'green':
                if neighbor not in po:
                    unused_green += 1
                    if neighbor not in locked:
                        open_list.append(neighbor)
                        locked.add(neighbor)
        if unused_green == 1 and current != root:   # adds to post order
            po[current] = po_counter
            po_counter += 1
            for neighbor in S[current]:
                if S[current][neighbor] == 'green' and neighbor not in po and neighbor != root:
                    locked.discard(neighbor)
                    open_list.append(neighbor)
    po[root] = po_counter
    return po

# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces


def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    # because dictionaries won't run the same way twice when iterating through a dictionary, need to list all 4 answers.
    assert (po == {'a': 7, 'b': 1, 'c': 6, 'd': 5, 'e': 4, 'f': 2, 'g': 3} or
            po == {'a': 7, 'b': 1, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 2} or
            po == {'a': 7,  'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1} or
            po == {'a': 7,  'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 1, 'g': 2}), "\n po = {0}".format(po)

##############


def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node, includes the node itself
    descendants = {node: 0 for node in list(S.keys())}
    open_list = collections.deque([root])
    paths = {root: root}
    while open_list:
        current = open_list.popleft()
        for node in paths[current]:
            descendants[node] += 1
        for neighbor in S[current]:
            if neighbor not in paths:
                if S[current][neighbor] == 'green':
                    open_list.append(neighbor)
                    paths[neighbor] = paths[current] + neighbor
    return descendants


def test_number_of_descendants():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a': 7, 'b': 1, 'c': 5, 'd': 4, 'e': 3, 'f': 1, 'g': 1}, "\n nd ={0}".format(nd)

###############


def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    lowest_po_tuples = {node: [po[node], po[node]] for node in po}     # {node: (po, conditional po)}
    open_list = [root]
    paths = {root: root}
    while open_list:
        current = open_list.pop()
        for neighbor in S[current]:
            if neighbor not in paths:
                if S[current][neighbor] == 'green':
                    open_list.append(neighbor)
                    paths[neighbor] = paths[current] + neighbor
            if S[current][neighbor] == 'red':
                if lowest_po_tuples[neighbor][0] < lowest_po_tuples[current][1]:
                    lowest_po_tuples[current][1] = lowest_po_tuples[neighbor][0]
        for path_node in paths[current]:
            for i in range(2):
                if lowest_po_tuples[current][i] < lowest_po_tuples[path_node][i]:
                    lowest_po_tuples[path_node][i] = lowest_po_tuples[current][i]
    lowest_po = {node: min(lowest_po_tuples[node]) for node in lowest_po_tuples}
    return lowest_po


def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert (l == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2} or                  # cases where 'b' == 1 -> 'f' or 'g' == 2
            l == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}), "l was invalid"   # cases where 'b' == 6 -> 'f' or 'g' == 1

################


def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    highest_po_tuples = {node: [po[node], po[node]] for node in po}     # {node: (po, conditional po)}
    open_list = [root]
    paths = {root: root}
    while open_list:
        current = open_list.pop()
        for neighbor in S[current]:
            if neighbor not in paths:
                if S[current][neighbor] == 'green':
                    open_list.append(neighbor)
                    paths[neighbor] = paths[current] + neighbor
            if S[current][neighbor] == 'red':
                if highest_po_tuples[neighbor][0] > highest_po_tuples[current][1]:
                    highest_po_tuples[current][1] = highest_po_tuples[neighbor][0]
        for path_node in paths[current]:
            for i in range(2):
                if highest_po_tuples[current][i] > highest_po_tuples[path_node][i]:
                    highest_po_tuples[path_node][i] = highest_po_tuples[current][i]
    highest_po = {node: max(highest_po_tuples[node]) for node in highest_po_tuples}
    return highest_po
    pass


def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    print("\n{0}".format(po))
    h = highest_post_order(S, 'a', po)
    print("\n{0}\n".format(h))
    assert (h == {'a': 7, 'b': 5, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 3} or  # cases where 'b' == 1
            h == {'a': 7, 'b': 6, 'c': 6, 'd': 6, 'e': 3, 'f': 2, 'g': 2})  # cases where 'b' == 6

#################


def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    lpo = lowest_post_order(S, root, po)
    hpo = highest_post_order(S, root, po)
    descendants = number_of_descendants(S, root)
    bridges = []
    for node1 in S.keys():
        for node2 in S[node1].keys():
            if po[node1] > po[node2]:   # check if is node1 is parent of node2
                if (hpo[node2] <= po[node2] and
                   lpo[node2] > po[node2] - descendants[node2] and
                   not any('red' == S[node2][edge] for edge in S[node2])):  # if any edge is red, this node isn't counted
                    bridges.append((node1, node2))
    return bridges


def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]

if __name__ == '__main__':
    # test_create_rooted_spanning_tree()
    # test_post_order()
    # test_number_of_descendants()
    # test_lowest_post_order()
    # test_highest_post_order()
    test_bridge_edges()

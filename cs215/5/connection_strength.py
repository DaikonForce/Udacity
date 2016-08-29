# computes the connection strength between all comic book characters in a graph and returns the largest connection strength
import csv


def make_link(graph, node0, node1):
    # makes an edge between two nodes of a graph(dictionary)
    nodes = [node0, node1]
    for i in range(len(nodes)):
        # print(nodes[i], nodes[1-i])
        if nodes[i] not in graph:
            graph[nodes[i]] = {}
        # if nodes[1-i] not in graph[i].keys():
        graph[nodes[i]][nodes[i-1]] = 1


def read_tsv(filename):
    # reads a tsv file and outputs a graph and characters
    with open(filename, mode='r') as tsv_open:
        tsv_reader = csv.reader(tsv_open, delimiter='\t')
        characters = set()
        graph = {}
        for nodes in tsv_reader:
            make_link(graph, nodes[0], nodes[1])
            characters.add(nodes[0])
    return graph, characters


def make_connections(graph, char1, char2):
    # makes a numerical connection between 2 nodes and edits input graph
    chars = [char1, char2]
    most_connections = 0
    chars_with_most_cons = []
    for i in range(len(chars)):
        if chars[i] not in graph:
            graph[chars[i]] = {}
        if chars[1-i] not in graph[chars[i]]:
            graph[chars[i]][chars[1-i]] = 1
        else:
            graph[chars[i]][chars[1-i]] += 1


def make_connections_graph(graph, characters):
    # makes a graph between characters listing their connection strength
    connections_graph = {}
    for char1 in characters:
        for book in graph[char1]:
            for char2 in graph[book]:
                if char1 > char2:
                    make_connections(connections_graph, char1, char2)
    return connections_graph


def find_most_connected(graph):
    # finds the most connected characters in a connections_graph
    char_pair = [0, 0]
    connection_number = 0
    unlock = 0
    for i, char1 in enumerate(graph):
        if not(i % 200):
            unlock = 1
        for char2 in graph[char1]:
            if unlock == 1:
                unlock = 0
                print(i, char1, char2, graph[char1][char2])
            if graph[char1][char2] > connection_number:
                connection_number = graph[char1][char2]
                char_pair = [char1, char2]
    return char_pair, connection_number


def main():
    filename = 'data/comics.tsv'
    print("Reading {0}".format(filename))
    graph, characters = read_tsv('data/comics.tsv')
    print("Building con_graph")
    con_graph = make_connections_graph(graph, characters)
    print("Finding most connected pair")
    char_pair, connection_number = find_most_connected(con_graph)
    print("Printing Result:\n")
    print("{0}\:{1}".format(char_pair, connection_number))


if __name__ == '__main__':
    main()

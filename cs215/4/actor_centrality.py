#!/usr/bin/env python3
import sys
from collections import deque
from random import choice
import csv
import os.path
import random

""" returns the centrality given a TSV data set of edges
ex:
apple\tbanana
pear\torange
apple\torange"""

""" download link for data file http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckALEgZDb3Vyc2UiBWNzMjE1DAsSCUNvdXJzZVJldhgBDAsSBFVuaXQY69QQDAsSDEF0dGFjaGVkRmlsZRiSrQsM&_ga=1.133049287.838228685.1471486311
"""


def make_link(G, node1, node2):
    # makes a link between node1 and node2 in graph G
    if node1 not in G:
        G[node1] = {}
    G[node1][node2] = 1
    if node2 not in G:
        G[node2] = {}
    G[node2][node1] = 1
    return G


def read_graph(filename):
    # Reads an undirected graph in TSV format. each line is an edge
    # Outputs a graph and a list of actors
    # first node is 1 section, anything after the first tab is grouped together
    G = {}
    actors = set()
    with open(filename, mode='r', encoding='utf-8') as file:
        tsv_reader = csv.reader(file, delimiter='\t')
        for nodes in tsv_reader:
            make_link(G, nodes[0], ''.join(nodes[1:]))
            actors.add(nodes[0])
    return G, actors


def path(G, v1, v2):
    # looks for shortest path between v1 and v2 in graph G (breadth first search)
    dist_from_start = {}
    open_list = deque([v1])     # allows for popleft() instead of pop(0)
    dist_from_start[v1] = 0
    path_from_start = [v1]
    while open_list:
        current = open_list.popleft()
        for neighbor in G[current].keys():
            if neighbor not in dist_from_start:
                dist_from_start[neighbor] = dist_from_start[current] + 1
                if neighbor == v2:
                    return dist_from_start[v2]
                open_list.append(neighbor)


def centrality(G, v):
    # returns the centrality of a given node
    # figure out a way to write the search go out then in and then back out again(?)
    distance_from_start = {}
    open_list = deque([v])
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list.popleft()
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)


def inserted_sort(in_list, in_val):
    if not in_list:
        in_list = [in_val]
    for i, val in enumerate(in_list):
        if in_val > val:
            in_list.insert(in_val, i)
            return


def main(argv):
    # write in comments
    tsvs = ["data/imdb-1.tsv",
            "data/imdb-2.tsv",
            "data/imdb-3.tsv",
            "data/imdb-4.tsv"]
    graph = {}
    actors = set()
    dict_of_stupid_shit = {}
    if len(argv) > 1:
        if argv[1] == "1":
            graph, actors = read_graph(tsvs[0])
        elif argv[1] == "2":
            graph, actors = read_graph(tsvs[1])
        elif argv[1] == "3":
            graph, actors = read_graph(tsvs[2])
        elif argv[1] == "4":
            graph, actors = read_graph(tsvs[3])
        elif os.path.isfile():
            graph, actors = read_graph(argv[1])
        else:
            print("ERROR: File not found, using data/imdb-1.tsv")
            graph, actors = read_graph(tsvs[0])
    else:
        print("Reading", tsvs[0])
        graph, actors = read_graph(tsvs[0])
    for i, actor in enumerate(actors):
        centrality_number = centrality(graph, actor)
        dict_of_stupid_shit[centrality_number] = actor
        if not (i % 100):
            print("{0}: {1}: {2}".format(i, dict_of_stupid_shit[centrality_number], centrality_number))
    list_of_stupid_shit_numbers = list(dict_of_stupid_shit.keys())
    list_of_stupid_shit_numbers.sort()
    for i, key in enumerate(list_of_stupid_shit_numbers[:25]):
        print(i, dict_of_stupid_shit[key], key)
    output_file = "data/data.csv"
    with open(output_file, mode='w', newline='') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for i, key in enumerate(list_of_stupid_shit_numbers):
            tsv_writer.writerow([dict_of_stupid_shit[key], str(key)])


if __name__ == '__main__':
    main(sys.argv)

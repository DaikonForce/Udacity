#!/usr/bin/env python3
import time
import sys
from collections import deque
from random import choice
import csv

""" returns the shortest path length given a TSV data set of edges
ex:
apple\tbanana
pear\torange
apple\torange"""

""" download link for data file http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckALEgZDb3Vyc2UiBWNzMjE1DAsSCUNvdXJzZVJldhgBDAsSBFVuaXQYkacNDAsSDEF0dGFjaGVkRmlsZRiByhEM&_ga=1.125387715.838228685.1471486311
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


def read_graph(filename, return_all=False):
    # Reads an undirected graph in CSV format. each line is an edge, return all returns dict(graph), set(node1), set(node2)
    tsv = csv.reader(open(filename, mode='r'), delimiter='\t')
    G = {}
    node1_all = set()
    node2_all = set()
    for (node1, node2) in tsv:
        make_link(G, node1, node2)
        if return_all:
            node1_all.add(node1)
            node2_all.add(node2)
    if return_all:
        return G, node1_all, node2_all
    return G


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


def random_hero(G, heroes=[]):
    # returns a random hero from graph G, will exclude any hero in list heroes
    hero_pool = list(G.keys())
    tmp_name = choice(hero_pool)   # replace hero with a random different hero
    while tmp_name in heroes:
        tmp_name = choice(hero_pool)
    return tmp_name


def main(argv):
    filename = "data/marvel.tsv"
    if len(argv) >= 2:  # extra args
        argument = argv[1].upper()
        if argument == "HELP" or argument == "H":
            print("h for help\nl for list for characters and comics\nch for a list of characters\nco for a list of comics.")
        elif argument == "L" or argument == "LIST":
            print(read_graph(filename, False))
        elif argument == "CH" or argument == "CHARACTERS":
            G, chars, comics = read_graph(filename, True)
            print(chars)
        elif argument == "CO" or argument == "COMICS":
            G, chars, comics = read_graph(filename, True)
            print(comics)
        else:
            print("use argument \"h\" for help.")
        return -1
    G = read_graph(filename)    # reads in graph and sets it to G
    if len(G.keys()) <= 1:
        print("Error: Graph of length 1.")
        return -1
    print("Enter two different marvel heroes or comic-id's")
    heroes = []             # list of heroes used in path(G, v1, v2) to find shortest path
    not_in_list = False     # activates if any input is not in the graph. prints out helpful statement at end
    for i in range(0, 2):   # list of 2 heroes
        heroes.append(input("Entry {0}: ".format(i+1)).upper())
        if heroes[i] not in G.keys():   # replace input with a different hero if input not in hero pool.
            not_in_list = True
            tmp_name = random_hero(G, heroes)
            print("Warning: {0} was not in character/comic pool. Using {1} instead.".format(heroes[i], tmp_name))
            heroes[i] = tmp_name
        print()
    print("Degrees of separation between {0} and {1}: {2}".format(heroes[0], heroes[1], path(G, heroes[0], heroes[1])))
    if not_in_list:
        print()
        print("For full list of comics and characters type use the \"L\" command")

if __name__ == '__main__':
    main(sys.argv)

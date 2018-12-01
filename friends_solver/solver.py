import networkx as nx
import os
import numpy as np
import copy

def score_output(graph_in, num_buses, size_bus, constraints, assignments):
    '''
        Takes an input and an output and returns the score of the output on that input if valid
        
        Inputs:
            input_folder - a string representing the path to the input folder
            output_file - a string representing the path to the output file

        Outputs:
            (score, msg)
            score - a number between 0 and 1 which represents what fraction of friendships were broken
            msg - a string which stores error messages in case the output file is not valid for the given input
    '''
    #graph = nx.read_gml(input_folder + "/graph.gml")
    #parameters = open(input_folder + "/parameters.txt")
    #num_buses = int(parameters.readline())
    #size_bus = int(parameters.readline())
    #constraints = []

    #for line in parameters:
    #    line = line[1: -2]
    #    curr_constraint = [node.replace("'","") for node in line.split(", ")]
    #    constraints.append(curr_constraint)

    #output = open(output_file)
    #assignments = []
    #for line in output:
    #    line = line[1: -2]
    #    curr_assignment = [node.replace("'","") for node in line.split(", ")]
    #    assignments.append(curr_assignment)
    #print(assignments)

    #assignments = output_file

    graph = graph_in.copy()
    if len(assignments) != num_buses:
        return -1, "Must assign students to exactly {} buses, found {} buses".format(num_buses, len(assignments))
    
    # make sure no bus is empty or above capacity
    #for i in range(len(assignments)):
    #    if len(assignments[i]) > size_bus:
    #        return -1, "Bus {} is above capacity".format(i)
    #    if len(assignments[i]) <= 0:
    #        return -1, "Bus {} is empty".format(i)
        
    bus_assignments = {}
    attendance_count = 0
        
    # make sure each student is in exactly one bus
    attendance = {student:False for student in graph.nodes()}
    for i in range(len(assignments)):
        if not all([student in graph for student in assignments[i]]):
            return -1, "Bus {} references a non-existant student: {}".format(i, assignments[i])

        for student in assignments[i]:
            # if a student appears more than once
            if attendance[student] == True:
                return -1, "{0} appears more than once in the bus assignments".format(student)
                
            attendance[student] = True
            bus_assignments[student] = i
    
    # make sure each student is accounted for
    if not all(attendance.values()):
        return -1, "Not all students have been assigned a bus"
    
    total_edges = graph.number_of_edges()
    # Remove nodes for rowdy groups which were not broken up
    for i in range(len(constraints)):
        busses = set()
        for student in constraints[i]:
            busses.add(bus_assignments[student])
        if len(busses) <= 1:
            for student in constraints[i]:
                if student in graph:
                    graph.remove_node(student)

    # score output
    score = 0
    for edge in graph.edges():
        if bus_assignments[edge[0]] == bus_assignments[edge[1]]:
            score += 1
    score = score / total_edges


    return score

def parse_input(folder_name):
    '''
        Parses an input and returns the corresponding graph and parameters

        Inputs:
            folder_name - a string representing the path to the input folder

        Outputs:
            (graph, num_buses, size_bus, constraints)
            graph - the graph as a NetworkX object
            num_buses - an integer representing the number of buses you can allocate to
            size_buses - an integer representing the number of students that can fit on a bus
            constraints - a list where each element is a list vertices which represents a single rowdy group
    '''
    graph = nx.read_gml(folder_name + "/graph.gml")
    parameters = open(folder_name + "/parameters.txt")
    num_buses = int(parameters.readline())
    size_bus = int(parameters.readline())
    constraints = []
    
    for line in parameters:
        line = line[1: -2]
        curr_constraint = [num.replace("'", "") for num in line.split(", ")]
        constraints.append(curr_constraint)

    return graph, num_buses, size_bus, constraints

def gen_random(nodes, num_buses, size_bus):
    buses = [[] for i in range(num_buses)]
    for i in range(len(nodes)):
        buses[i % num_buses].extend(nodes[i])
    for i in range(100): # number of swaps
        first = np.random.randint(num_buses)
        second = np.random.randint(num_buses)
        while second == first:
            second = np.random.randint(num_buses)
        first_index = np.random.randint(len(buses[first]))
        second_index = np.random.randint(len(buses[second]))
        buses[first][first_index], buses[second][second_index]= buses[second][second_index], buses[first][first_index]
    return buses

def modify(buses, size_bus):
    new_buses = copy.deepcopy(buses)
    for j in range(2): # num iters
        a = np.random.randint(2)
        if a == 0: # swap
            first = np.random.randint(num_buses)
            second = np.random.randint(num_buses)
            while second == first:
                second = np.random.randint(num_buses)
            first_index = np.random.randint(len(new_buses[first]))
            second_index = np.random.randint(len(new_buses[second]))
            new_buses[first][first_index], new_buses[second][second_index]= new_buses[second][second_index], new_buses[first][first_index]
        if a == 1: # move
            first = np.random.randint(num_buses)
            while len(new_buses[first]) < 2:
                first = np.random.randint(num_buses)
            second = np.random.randint(num_buses)
            while second == first or len(buses[second]) >= size_bus:
                second = np.random.randint(num_buses)
            first_index = np.random.randint(len(new_buses[first]))
            temp = new_buses[first][first_index]
            new_buses[second].append(temp)
            new_buses[first].remove(temp)
    return new_buses


def solve(graph, num_buses, size_bus, constraints):
    all_nodes = list(graph.nodes)
    print(all_nodes)
    bs = gen_random(all_nodes, num_buses, size_bus)
    #print(bs)
    max_score = score_output(graph, num_buses, size_bus, constraints, bs)
    #print(max_score)
    for i in range(100): # number of iterations
        new_buses = list(modify(bs, size_bus))
        #print(new_buses)
        new_score = score_output(graph, num_buses, size_bus, constraints, new_buses)
        #print(new_score)
        if new_score > max_score:
            #print(new_score, max_score)
            max_score = new_score
            bs = copy.deepcopy(new_buses)
            #print(new_buses)
    return score_output(graph, num_buses, size_bus, constraints, bs), bs


graph, num_buses, size_bus, constraints = parse_input('../easy_input/')
print(solve(graph, num_buses, size_bus, constraints))
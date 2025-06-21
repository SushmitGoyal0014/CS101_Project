import networkx as nx
import numpy as np
import random
import csv

G=nx.DiGraph()  #created a graph G

with open('/Users/sushmitgoyal/Desktop/Python Project/project2_data.csv', 'r') as f:
    reader=csv.reader(f)
    next(reader)  #to skip the headings line of the data
    #the following for loop is used to add an edge from one node to the node which it asked a question
    for row in reader:
        for i in range(1,len(row)):
            if row[i]!='nan':
                G.add_edge(row[0],row[i])


def RW(G):
    node_list = list(G.nodes())  #creating a list that will contain the nodes of graph G
    if len(node_list) == 0:
        return []  #Return an empty dictionary if G has zero nodes

    #creating a dictionary that stores the number of random walk points of a node
    points={node: 0 for node in node_list}  #all nodes have zero points initially
    n=random.choice(node_list)  #choosing a node at random from the node_list
    points[n]+=1  #now incrementing the points of the selected node by 1
    
    linked_nodes=list(G.out_edges(n))  #finding the nodes with which our selected node is connected
    k=0
    while k != 100000:  
        #if there are no links then we choose another random node    
        if len(linked_nodes)==0:
            new_n=random.choice(node_list)

        else:
            t=random.uniform(0,1)  #teleportation
            #if the probability is less than 0.15 then we choose a new random node, else we choose a random linked node
            if t<0.15:
                new_n=random.choice(node_list)

            #else choose a random link
            else:
                n1=random.choice(linked_nodes)
                new_n=n1[1]

        points[new_n]+=1  #incrementing the points of the new node that we have visited by 1
        linked_nodes=list(G.out_edges(new_n))  #updating the linked_nodes list with the links of the new node
        k += 1

    return points


l = RW(G)   #calling the function
sorted_list=sorted(l.items(), key=lambda x: x[1], reverse=True)  #sorting the occurance values of nodes in the dictionary
print(sorted_list)
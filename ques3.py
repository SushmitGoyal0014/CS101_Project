import networkx as nx
import csv

G=nx.DiGraph()
with open('/Users/sushmitgoyal/Desktop/Python Project/project2_data.csv','r') as f:
    reader=csv.reader(f)
    next(reader)  #skip the headings line of the data
    for row in reader:
        for i in range(1,len(row)):
            if row[i]!='nan':  #if there is 'nan' then there will be no edge between the nodes,otherwise we add an edge between the two nodes
                G.add_edge(row[0],row[i])

#separating the initial graph into two different graphs for mcb and csb
CSB_G=nx.DiGraph()
MCB_G=nx.DiGraph()
#the following for loop adds the nodes having 'CSB' in them in CSB_G and having 'MCB' in MCB_G
for node in G.nodes():
    if "CSB" in node:
        CSB_G.add_node(node)
    elif "MCB" in node:
        MCB_G.add_node(node)

#adding edges in both graphs from original graph
for edge in G.edges():
    start_node, end_node = edge  #edge is stored in form of tuple
    #if both the nodes are in CSB_G then add an edge in it
    if start_node in CSB_G.nodes() and end_node in CSB_G.nodes():
        CSB_G.add_edge(start_node,end_node)
    #if both the nodes are in MCB_G then add an edge in it
    elif start_node in MCB_G.nodes() and end_node in MCB_G.nodes():
        MCB_G.add_edge(start_node,end_node)

#defining a function to calculate the ratio of actual number of edges to the total number of edges
def calc_r(graph):
    act_edges=graph.number_of_edges()
    total_edges=graph.number_of_nodes() * (graph.number_of_nodes() - 1)  #total edges are n(n-1) where n is the number of nodes
    r=act_edges/total_edges  #calculating the required ratio
    return r

#now finding the ratio for CSB and MCB
CSB_r=calc_r(CSB_G)
MCB_r=calc_r(MCB_G)

print("Ratio for CSB graph:", CSB_r)
print("Ratio for MCB graph:", MCB_r)
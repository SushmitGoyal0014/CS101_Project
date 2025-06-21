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
            if row[i]!='nan':   #if there is 'nan' between two nodes then there is no edge between them. In case of no 'nan' then we will add an edge between them
                G.add_edge(row[0],row[i])

#creating a function that will take the graph as input and find the number of missing links in it
def find_mis_links(G):
    node_list=sorted(G.nodes())  #creating a list to store the nodes of the graph in sorted order
    no_of_nodes=len(node_list)  #length of 'node_list' gives number of nodes
    adj_mat_1=nx.to_numpy_array(G,node_list)    #this matrix gives information about the links between the nodes
    mis_links=[]    #inititalizing a list to store missing links
    value_range=[]   #initializing a list to check value range

    #this nested for loop first iterates through rows and then through columns
    for i in range(len(node_list)):
        for j in range(len(node_list)):
            #if both Aij element and Aji element are zero then there is a case of missing link
            if i!=j and adj_mat_1[i,j]==0 and adj_mat_1[j,i]==0:
                adj_mat_2=adj_mat_1.copy()  #copying the above matrix
                col=np.delete(adj_mat_2[i],j)   #taking out the jth column and removing the Aij element
                row=np.delete(adj_mat_2[:,j],i)   #taking out the ith row and removing the Aij element
                adj_mat_2=np.delete(adj_mat_2,(i),axis=0)   #deleting the ith row using axis=0 syntax
                adj_mat_2=np.delete(adj_mat_2,(j),axis=1)   #deleting the jth column using axis=1 syntax
                x=np.linalg.lstsq(adj_mat_2,row,rcond=None)[0]   #to find the coefficents of linear combination
                val=np.dot(x,col)   #doing dot product of the above coefficients with 'col'

                #if 'val' comes out to be greater than the threshold (here 0.5) then we say that there is a missing link
                if val>0.5:
                    mis_links.append((node_list[i],node_list[j]))

    print("missing links found are: ",len(mis_links))

find_mis_links(G)
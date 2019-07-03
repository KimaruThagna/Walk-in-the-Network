import networkx as nx

Friends=nx.empty_graph()# each edge represents connection between friends
Friends.add_edge(1,2)# person 1 is friends with 2
Friends.add_edge(2,3)
Friends.add_edge(3,4)
Friends.add_edge(3,1)# 3 is friends with 1
Friends.add_edge(2,5)
Friends.add_edge(7,9)

# is there a relationship between person 1 and 5? if yes, through who
try:
    print(nx.dijkstra_path(Friends, 1, 5))

except:
    print('No path')

#alternate implementation
if nx.has_path(Friends,1,5):
    print("TRUE")
else:
    print("FALSE")

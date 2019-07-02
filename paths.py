import networkx as nx

Friends=nx.empty_graph()
Friends.add_edge(1,2)
Friends.add_edge(2,3)
Friends.add_edge(3,4)
Friends.add_edge(3,1)
Friends.add_edge(2,5)
Friends.add_edge(7,9)


try:
    print(nx.dijkstra_path(Friends, 1, 5))

except:
    print('No path')

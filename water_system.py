import networkx as nx
'''
Considering you are in charge of the water system in Nairobi County,
Below is the water system network. The weights represent the difficulty in terms of pumping costs due to terrain.
Using dijkstra's algorithm, one can find the shortest most effecient path considering weights.
The same concept can be applied with air travel. The weights can be the weather conditions. Since its dynamic, the weights can be randomized
'''
water_system=nx.empty_graph()
water_system.add_edge("ngara","pangani",weight=10)
water_system.add_edge("kahawa","pangani",weight=30)
water_system.add_edge("parklands","ngara",weight=2)
water_system.add_edge("ngara","pangani",weight=5)
water_system.add_edge("pangani","nyayo",weight=90)
water_system.add_edge("pumwani","parklands",weight=41)
water_system.add_edge("pumwani","pangani",weight=100)

try:
    print(nx.bidirectional_dijkstra(water_system, "pumwani", "pangani"))#optimal path and cost

except:
    print('No existing path')





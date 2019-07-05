import plotly
from water_system import *
from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot, plot
init_notebook_mode(connected=True)


#layout can be one of several, spectral, spring, fruchterman_reingold_layout among others
pos=nx.fruchterman_reingold_layout(water_system)
print(pos)# key is node index and value is an array of cordinates the layout algorithm has assigned each node
import plotly
from water_system import *
import plotly.plotly as py
import plotly.graph_objs as go



#layout can be one of several, spectral, spring, fruchterman_reingold_layout among others
pos=nx.fruchterman_reingold_layout(water_system)
print(pos)# key is node index and value is an array of cordinates the layout algorithm has assigned each node

Xs=[pos[k][0] for k in pos]
Ys=[pos[k][1] for k in pos]
#define traces for nodes
trace_nodes=dict(type='scatter',
                 x=Xs,
                 y=Ys,
                 mode='markers',
                 marker=dict(size=28, color='rgb(0,240,0)'),
                 hoverinfo='text')
#record coordinates for edge ends
Xe=[]
Ye=[]
weights=[]
for e in water_system.edges():
    Xe.extend([pos[e[0]][0], pos[e[1]][0], None])
    Ye.extend([pos[e[0]][1], pos[e[1]][1], None])
    #weights.append()
#define trace for edges
trace_edges=dict(type='scatter',
                 mode='lines',
                 x=Xe,
                 y=Ye,
                 line=dict(width=1, color='rgb(25,25,25)'),
                 hoverinfo='none'
                )

# plot the data

axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
            )
layout = dict(title='Nairobi Water System',
              font=dict(family='Balto'),
              width=600,
              height=600,
              autosize=False,
              showlegend=False,
              xaxis=axis,
              yaxis=axis,
              margin=dict(
                  l=40,
                  r=40,
                  b=85,
                  t=100,
                  pad=0,
              ),
              hovermode='closest',
              plot_bgcolor='#efecea',  # set background color
              )

fig = dict(data=[trace_edges, trace_nodes], layout=layout)
py.plot(fig)
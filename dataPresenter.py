import plotly.graph_objects as go
import json

def parseLabels():
    with open('data.json') as json_file:
        data = json.load(json_file)

    for p in data['people']:
        userLabel = p['year']
        if(userLabel == ''):
            userLabel = 'Professor'
        if(userLabel not in labels):
            labels.append(userLabel)
            values.append(1)
        else:
            values[labels.index(userLabel)] = values[labels.index(userLabel)] + 1
    print(labels)
    print(values)

    
        


    
labels = []
values = []
parseLabels()
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

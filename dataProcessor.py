import json

#returns a dictionary with (year: occurences) pairs
#Ex/ {("Freshman": 3), ("Junior": 3), ... }
def parseLabels():
    #reads the json
    with open('data.json') as json_file:
        data = json.load(json_file)

    #will hold the year:value pairs
    labels = {}

    for p in data['people']:
        current = p['year']
        
        #Choose a default
        if(current == ''):
            current = 'N/A'

        #Create a new label when needed
        if(current not in labels.keys()):
            labels[current] = 1
        else:
            #increment counter for the label
            labels[current] = labels[current] + 1
    print(labels)
    return labels


#returns a dictionary with (Language: occurences) pairs
#Ex/ {("R": 3), ("Go": 3), ... }
def parseLangs():
    #reads the json
    with open('data.json') as json_file:
        data = json.load(json_file)

    #will hold the year:value pairs
    labels = {}

    for p in data['people']:
        current = p['optionalInformation']
        for lang in current['favoriteLanguages']:
            #Choose a default
            if(lang == ''):
                lang = 'Python'

            #Create a new label when needed
            if(lang not in labels.keys()):
                labels[lang] = 1
            else:
                #increment counter for the label
                labels[lang] = labels[lang] + 1
    print(labels)
    return labels



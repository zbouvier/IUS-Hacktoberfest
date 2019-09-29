import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json, argparse, sys

TITLE  = 'HACKTOBER'


def checkFields(fields):
    """
    """
    if(len(sys.argv) == 1): # no flags were entered, default all to True
        for flag in vars(fields):
            setattr(fields,flag,True)

def appendDict(dictn,label):
    """
    """
    if(type(label) is list):
        for item in label: appendDict(dictn,item)
        return
    if label in dictn:
        dictn[label] += 1
    else:
        dictn[label] = 1  
        
def dictToFig(dictn):
    """
    """
    labels = list(dictn.keys())
    values = list(dictn.values())
    return go.Pie(labels = labels, values = values)

def buildGraphs(fields):
    """
    """
    
    names      = []
    major      = {}
    role       = {}
    year       = {}
    profile    = []
    email      = []
    favLang    = {}
    hobbies    = {}
    graphSpecs = []
    
    # Get data from JSON file
    with open('data.json') as json_file:
        data = json.load(json_file)
        
    # Loop through all the people listed in the file
    for person in data['people']:
        if(fields.showName):
            names.append(person['name'])
        if(fields.showMajor):
            appendDict(major,person['major'])
        if(fields.showRole):
            appendDict(role,person['role'])
        if(fields.showYear):
            if(person['year'] == ''): person['year'] = 'Professor'
            appendDict(year,person['year'])
        if(fields.showProfile):
            profile.append(person['profile'])
        if(fields.showEmail):
            email.append(person['optionalInformation']['email'])
        if(fields.showFavLang):
            appendDict(favLang,person['optionalInformation']['favoriteLanguages'])
        if(fields.showHobbies):
            appendDict(hobbies,person['optionalInformation']['hobbies'])
            
    if(fields.showName) or (fields.showProfile) or (fields.showEmail):
        graphSpecs.append([{'type' : 'table'}])
    if(fields.showMajor):
        graphSpecs.append([{'type' : 'pie'}])
    if(fields.showRole):
        graphSpecs.append([{'type' : 'pie'}])
    if(fields.showYear):
        graphSpecs.append([{'type' : 'pie'}])
    if(fields.showFavLang):
        graphSpecs.append([{'type' : 'pie'}])
    if(fields.showHobbies):
        graphSpecs.append([{'type' : 'pie'}])
    
    allFigs = make_subplots(rows = len(graphSpecs),cols = 1, vertical_spacing = 0.05, specs = graphSpecs)
    rowCounter = 1
    
    if(fields.showName) or (fields.showProfile) or (fields.showEmail):
        headerLabels = []
        values = []
        if(fields.showName):    
            headerLabels.append('Name')
            values.append(names)
        if(fields.showProfile): 
            headerLabels.append('Profile')
            values.append(profile)
        if(fields.showEmail):   
            headerLabels.append('Email')
            values.append(email)
        
        personalInfoTable = go.Table(header = dict(values=headerLabels,font=dict(size=10),align="center"),
                                     cells  = dict(values=values, align = "left"))
        allFigs.add_trace(personalInfoTable,row=rowCounter,col=1)
        rowCounter += 1
        
    if(fields.showMajor):
        allFigs.add_trace(dictToFig(major),row=rowCounter,col=1)
        rowCounter += 1
    
    if(fields.showRole):
        allFigs.add_trace(dictToFig(role),row=rowCounter,col=1)
        rowCounter += 1
        
    if(fields.showYear):
        allFigs.add_trace(dictToFig(year),row=rowCounter,col=1)
        rowCounter += 1
        
    if(fields.showFavLang):
        allFigs.add_trace(dictToFig(favLang),row=rowCounter,col=1)
        rowCounter += 1
        
    if(fields.showHobbies):
        allFigs.add_trace(dictToFig(hobbies),row=rowCounter,col=1)
        rowCounter += 1
    
    allFigs.update_layout(title_text=TITLE)    
    allFigs.show()

# Create a Parser Object to Read in Command Line Input
parser = argparse.ArgumentParser(description='Description Here')

# Setup Command Line Flags
parser.add_argument('-n', '--name',    dest='showName',    action='store_true', help='Show participants\' names')
parser.add_argument('-m', '--major',   dest='showMajor',   action='store_true', help='Show major data')
parser.add_argument('-r', '--role',    dest='showRole',    action='store_true', help='Show role data')
parser.add_argument('-y', '--year',    dest='showYear',    action='store_true', help='Show year data')
parser.add_argument('-p', '--profile', dest='showProfile', action='store_true', help='Show profile data')
parser.add_argument('-e', '--email',   dest='showEmail',   action='store_true', help='Show email data')
parser.add_argument('-l', '--favlang', dest='showFavLang', action='store_true', help='Show favorite langauge data')
parser.add_argument('-b', '--hobbies', dest='showHobbies', action='store_true', help='Show hobby data')

# Parse user entered arguments
fields = parser.parse_args()

checkFields(fields)
    
# Maybe add method that check all the fields in the JSON file are formatted correctly

# Retrieve
buildGraphs(fields)

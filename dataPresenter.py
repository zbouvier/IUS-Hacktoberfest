import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json, argparse, sys

TITLE                    = 'HACKTOBER'
SUBPLOT_VERTICAL_SPACING = 0.05
SUBPLOT_HEIGHT           = 500
LINE_STYLE               = {
                            'color' : '#000000',
                            'width' : 2
                           }
SUBPLOT_FONT_SIZE        = 12
TABLE_HEADER_FONT_SIZE   = 25
TABLE_BODY_FONT_SIZE     = 20
TABLE_LINE_COLOR         = 'black'
TABLE_HEADER_FILL_COLOR  = 'darkred'
TABLE_BODY_FILL_COLOR    = 'firebrick'
TABLE_TEXT_ALIGNMENT     = 'center'
TABLE_HEADER_FONT_COLOR  = 'white'
TABLE_BODY_FONT_COLOR    = 'white'
TABLE_HEADER_ROW_HEIGHT  = 60
TABLE_BODY_ROW_HEIGHT    = 40


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
    return go.Pie(labels = labels, values = values, 
                  textinfo='label',
                  textfont_size=SUBPLOT_FONT_SIZE,
                  marker=dict(line=LINE_STYLE))

def buildGraphs(fields):
    """
    """
    
    names         = []
    major         = {}
    role          = {}
    year          = {}
    profile       = []
    email         = []
    favLang       = {}
    hobbies       = {}
    graphSpecs    = []
    subPlotTitles = []
    
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
        subPlotTitles.append('Participant Information')
    if(fields.showMajor):
        graphSpecs.append([{'type' : 'pie'}])
        subPlotTitles.append('Majors')
    if(fields.showRole):
        graphSpecs.append([{'type' : 'pie'}])
        subPlotTitles.append('Roles')
    if(fields.showYear):
        graphSpecs.append([{'type' : 'pie'}])
        subPlotTitles.append('Year')
    if(fields.showFavLang):
        graphSpecs.append([{'type' : 'pie'}])
        subPlotTitles.append('Favorite Language')
    if(fields.showHobbies):
        graphSpecs.append([{'type' : 'pie'}])
        subPlotTitles.append('Hobbies')
    
    allFigs = make_subplots(rows = len(graphSpecs),cols = 1, vertical_spacing = SUBPLOT_VERTICAL_SPACING, specs = graphSpecs, subplot_titles = subPlotTitles)
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
        
        personalInfoTable = go.Table(header = dict(values=headerLabels,
                                                   font=dict(color=TABLE_HEADER_FONT_COLOR,size=TABLE_HEADER_FONT_SIZE),
                                                   align = TABLE_TEXT_ALIGNMENT,
                                                   line_color = TABLE_LINE_COLOR,
                                                   fill_color = TABLE_HEADER_FILL_COLOR,
                                                   height = TABLE_HEADER_ROW_HEIGHT),
                                     cells  = dict(values=values, 
                                                   font=dict(color=TABLE_BODY_FONT_COLOR,size=TABLE_BODY_FONT_SIZE),
                                                   align = TABLE_TEXT_ALIGNMENT,
                                                   line_color = TABLE_LINE_COLOR,
                                                   fill_color = TABLE_BODY_FILL_COLOR,
                                                   height = TABLE_BODY_ROW_HEIGHT)
                                     )
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
    
    allFigs.update_layout(height=(rowCounter*SUBPLOT_HEIGHT),title_text=TITLE,showlegend=False)    
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

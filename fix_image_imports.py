#Imports
import sys
import pandas as pd

#Cli argument
file_name = sys.argv[1]

file = pd.read_csv(file_name, keep_default_na=False) #disables default NA values and sents them to NaN, probably not needed

#TODO:: Maybe make the funciton take in the file as well as col name ot avoid hardcoding them
#TODO:: Make the forloop into a function to avoid repteaded code

#Strings containing files
image = 'Image' #in finds
condition_image = 'Condition Image' #in heritage asses
document = 'Document' #in information resource

if image in file.columns:
    for path in file[image].iteritems():
        if path[1]:
            file.at[path[0], image] = dict(eval(path[1])[0])['url']
    file.to_csv(f'{file_name}')

elif condition_image in file.columns:
    for path in file[condition_image].iteritems():
        if path[1]:
            if len(eval(path[1])) > 0:
                file.at[path[0], condition_image] = dict(eval(path[1])[0])['url']
    file.to_csv(f'{file_name}')

elif document in file.columns:
    for path in file[document].iteritems():
        if path[1]:
            file.at[path[0], document] = dict(eval(path[1])[0])['url']
    file.to_csv(f'{file_name}')

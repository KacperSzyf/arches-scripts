import json 

with open('res.json') as json_file:
    data = json.load(json_file)

def prepend(lst):
    '''
    Rebuild dictionary and prepend ID as first element
    '''
    new_list = []
    print('list', lst)

    for dictionary in lst:
        print('dict', dictionary)

        #Create a new dictionary entry at the end of the dictionary 
        dictionary.update({'id': dictionary['@admin']['id']})

        # Remove old entry
        dictionary.pop('@admin')

        #Get all dictionary keys in order 
        keys = list(dictionary.keys())

        #Remove the recently created 'id' field and place it at the front of the list
        keys.insert(0, keys.pop(keys.index('id')))

        #Rebuild the dictionary according to old key order 
        new = [{key: dictionary[key]} for key in keys]
        new_list.append(new)
    return new_list

   

for hit in data["hits"]["hits"]:
        source = hit["_source"]
        if "maker" in source.get("creation"):
            source['creation']['maker'] = prepend(source.get("creation").get("maker"))
        if 'classification' in source:
            source['classification'] = prepend(source.get('classification'))


with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)

        
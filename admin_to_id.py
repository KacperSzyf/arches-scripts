#Function
def replace_key(dictionary, oldKey, *args):
    ```
    Takes dictionary to change keys in, including optional keys if defaults are not desired
    ```
        
        #Unpack the optional arg
        newKey = args
        if args:
            newKey = list(args)[0]

        #Check if the new or old key are in the dictionary
        if (oldKey or newKey) in dictionary.keys():
            
            #Create the new key value pair
            dictionary[ newKey  or 'id'] = dictionary[oldKey][newKey or 'id']
            
            #Delete old key value pair
            del(dictionary[oldKey])

        return sort_dict_alphabetically(dictionary)

#Sort dictionary alphabetically by keys
def sort_dict_alphabetically(dictionary):
    return {key: dictionary[key] for key in sorted(dictionary)}
    
#Replace data with whatever the json is called
for hit in data["hits"]["hits"]:

    source = OrderedDict(hit["_source"])

    for key in list(hit["_source"]):
        if key == '@admin':
            source = replace_key(source, key)

        if key == 'classification':
            source[key] = [replace_key(record, '@admin') for record in source[key]]

        if key == 'department':
            source[key] = [replace_key(record, '@admin') for record in source[key]]

        if key == 'creation':
            if 'maker' in source[key].keys():
                source[key]['maker'] = [replace_key(record, '@admin') for record in source[key]['maker']]
                source[key]['maker'] = [replace_key(record, '@link', 'role') for record in source[key]['maker']]
    
    hit["_source"] = source

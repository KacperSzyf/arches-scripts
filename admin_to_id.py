import json 

with open('res.json') as json_file:
    data = json.load(json_file)

# for hit in data['hits']['hits']:
#     source = hit['_source'].items()

#     for key, value in source:
#         print(f'{key} : {value}')
#         if key == '@admin':
#             source.insert(0, ('id', value['id']))

def prepend(lst):
    new_list = []
    print('list', lst)
    for dictionary in lst:
        print('dict', dictionary)
        dictionary.update({'id': dictionary['@admin']['id']})
        dictionary.pop('@admin')
        keys = list(dictionary.keys())
        keys.insert(0, keys.pop(keys.index('id')))
        new = [{key: dictionary[key]} for key in keys]
        new_list.append(new)
    return new_list

   

for hit in data["hits"]["hits"]:
        source = hit["_source"]
        if "maker" in source.get("creation"):
            source['creation']['maker'] = prepend(source.get("creation").get("maker"))
        if 'classification' in source:
            source['classification'] = prepend(source.get('classification'))
            # new_list = []
            # for classification in source.get('classification'):
            #     new_list.append(prepend(classification))
            # source['classification'] = new_list


# print(data['hits']['hits'])

# for value in data['hits']['hits']:
#     source = value['_source']
#     source['@admin'] = source['@admin']['id']
#     source['id'] = source.pop('@admin')

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)

        
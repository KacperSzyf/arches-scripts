import json, sys

def make_readable(concepts_file, mapping_file, data_file):

    concepts = {}
    with open(concepts_file) as json_file:
        concepts = json.load(json_file)
        
    mapping = {}
    with open(mapping_file) as json_file:
        mapping = json.load(json_file)
        
    data = {}
    with open(data_file) as json_file:
        data = json.load(json_file)
    
    print(type(data))
    
    for resource in data.get('business_data').get('resources'):  
        for tile in resource.get('tiles'):
            #within tile data ------------------------------------------------------------
            for node in mapping.get('nodes'):
                #mapping related ---------------------------------------------------------
                for key in list(tile['data'].keys()):
                     #concept related ---------------------------------------------------------
                    for concept in concepts:
                        for option in concepts[concept]:
                            if option == tile['data'][key]:
                                tile['data'][key] = concepts[concept][option]

                    #end of concept relate ---------------------------------------------------
                    if node.get('arches_nodeid') == key:
                        tile['data'][node.get('arches_node_name')] = tile['data'].pop(key)
                #end of mapping related --------------------------------------------------

            #end of tile data ------------------------------------------------------------
        #resource itself ---------------------------------------------------------------------
        for key in resource.get('resourceinstance').keys():
            if mapping['resource_model_id'] == resource.get('resourceinstance')[key]:
                resource.get('resourceinstance')[key] = mapping['resource_model_name']
        #end of resource itself --------------------------------------------------------------

    with open('humandata.json', 'w') as outfile:
        json.dump(data, outfile, indent = 2)

if __name__ == "__main__":
    make_readable(sys.argv[1], [2], [3])
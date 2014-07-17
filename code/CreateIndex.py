from pyelasticsearch import ElasticSearch
import json

es = ElasticSearch('http://192.168.2.90:9200/')


index= {'mappings': {
            'address': {
               'properties': {
                    'id': {'type': 'long', 'store':'yes'},
                    'FirstName': { 'type':'string','store':'yes','index':'analyzed'},
                    'LastName': { 'type':'string','store':'yes','index':'analyzed'},
                    'NickName': { 'type':'string','store':'yes','index':'analyzed'},
                    'Street1': { 'type':'string','store':'yes','index':'analyzed'},
                    'Street2': { 'type':'string','store':'yes','index':'analyzed'},
                    'City': { 'type':'string','store':'yes','index':'analyzed'},
                    'State': { 'type':'string','store':'yes','index':'analyzed'},
                    'Postal': { 'type':'string','store':'yes','index':'analyzed'},
                    'Country': { 'type':'string','store':'yes','index':'analyzed'},
                    'CreateDate': { 'type':'date','store':'yes','format':'MM/dd/YYYY'},
                    'ModifiedDate': { 'type':'date','store':'yes','format':'MM/dd/YYYY'},
                    }
               }
            }
        }

res = es.delete_index('names')
print(res)
res2 = es.create_index('names',index)
print(res2)
res3 = es.get_mapping('names')
print(res3)




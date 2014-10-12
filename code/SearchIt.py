from elasticsearch import Elasticsearch
import json

es = Elasticsearch('http://192.168.2.90:9200/')


print("Enter a search term. XXX to quit.")


data = input()
while(data != 'XXX'):

    query = {'query': {
            'filtered': {
               'query': {
                 'query_string': {'query': 'FirstName:' + data}}}}}

    #res3 = es.search(query, index='contacts')
    res3 = es.search(query, index='names')

    res3j = json.dumps(res3)

    print(res3j)

    print("Enter a search term. XXX to quit.")
    data = input()

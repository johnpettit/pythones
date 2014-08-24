from elasticsearch import Elasticsearch
import json

es = Elasticsearch('192.168.2.90:9200/')

#es.index("contacts", "person", {"name":"Joe Tester", "age": 25, "title": "QA Master"})
#es.index("contacts", "person", {"name":"Joe Tester", "age": 25, "title": "QA Master"}, id=1)

#es.index("contacts", "person", {"name":"Jessica Coder", "age": 32, "title": "Programmer"}, id=2)

#es.index("contacts", "person", {"name":"Freddy Tester", "age": 29, "title": "Office Assistant"}, id=3)

#es.refresh('contacts')

#res = es.get('contacts', 'person', 2)

#print(res)

#res2 = es.search('name:joe OR name:freddy', index='contacts')

#print(res2)

query = {'query': {
            'filtered': {
               'query': {
                 'query_string': {'query': 'FirstName:Fred'}}}}}

#res3 = es.search(query, index='contacts')
res3 = es.search(query, index='names')

res3j = json.dumps(res3)

print(res3j)



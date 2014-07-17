from pyelasticsearch import ElasticSearch
import json

es = ElasticSearch('http://192.168.2.90:9200/')

data = raw_input("Enter search term. XXX to exit. --> ")

while(data != 'XXX'):

    data = data + '*'
    #print(data)
    #query = {"query": {"wildcard": {"FirstName":data}}}
    #query = {"size":"1", "query": {"query_string": {"query" : "FirstName:" + data}}}
    #query = {"version": "true", "query": {"query_string": {"query" : "FirstName:" + data}}}
    query = {"fields": ["FirstName","LastName"], "query": {"query_string": {"query" : "LastName:" + data}}}
    #query = {"query": {"query_string": {"query" : "FirstName:" + data}}}
    #print(query)
    res3 = es.search(query, index='names')

    #print(res3)

    listhits = res3['hits']['hits']
    for ele in listhits:
        #print k
        #print v[0]['_id'];
        print ele['fields']['FirstName'][0] + ' ' + ele['fields']['LastName'][0] + ' ' + ele['_id']
        #for x in v:
        #    print x

    res3j = json.dumps(res3,indent=4,sort_keys=True)

    #print(res3j)

    data = raw_input("Enter a serch term. XXX to exit. --> ")

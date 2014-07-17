from pyelasticsearch import ElasticSearch
import json

es = ElasticSearch('http://192.168.2.90:9200/')

data = es.cluster_state()

print(data)



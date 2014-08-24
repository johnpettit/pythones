#-*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
import json

es = Elasticsearch('192.168.2.90:9200/')

data = es.info()

print(json.dumps(data,indent=4,sort_keys=True))



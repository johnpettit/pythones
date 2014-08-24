from elasticsearch import Elasticsearch

class esManager:
    es = Elasticsearch('192.168.2.90:9200/')

    def insert(self):
        print("hi INSERT")

    def update(self):
        print("HI UPDATE")

    def search(self):
        print("HI SEARCH")



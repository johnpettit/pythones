from pyelasticsearch import ElasticSearch

class esManager:
    es = ElasticSearch('http://192.168.2.90:9200/')

    def insert():
        print("hi INSERT")

    def update():
        print("HI UPDATE")

    def search():
        print("HI SEARCH")



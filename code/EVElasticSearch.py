#-*- coding: utf-8 -*-

from ElasticSearchManager import esManager

class EVElasticSearch:
    """Base Class for EV Data Objects"""
    _internalCount = 0
    _es = esManager()

    def __init__(self):
        self._internalCount = self._internalCount + 1

    def showCount(self):
        return self._internalCount

    def insert(self):
        self._es.insert()

# self test

#jp = EVBase()
#print(jp.__doc__)
#print(jp.showCount())
#jp.insert()

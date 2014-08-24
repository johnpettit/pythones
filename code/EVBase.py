#-*- coding: utf-8 -*-

from ElasticSearchManager import esManager as es

class EVBase:
    """Base Class for EV Data Objects"""
    _internalCount = 0

    def __init__(self):
        self._internalCount = self._internalCount + 1

    def showCount(self):
        return self._internalCount


# self test

#jp = EVBase()
#print(jp.__doc__)
#print(jp.showCount())

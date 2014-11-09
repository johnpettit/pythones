#-*- coding: utf-8 -*-

from EVBase import EVBase
from EVElasticSearch import EVElasticSearch

class AccountCollection(EVBase, EVElasticSearch):
    """AccountCollection Object"""

    _indexName = "account"
    _accounts = list()

    def __init__(self):
        self._accounts.clear()

    def getAll(self):
        if id == '':
            #TODO better to Throw
            self._errorMessage = 'Required Field Missing: id'
            return False

        res = self._es.es.mget(index='names', doc_type='address', body={'_id', 'FirstName', 'LastName'})
        #TODO check result
        print(res)
        return res

    #######-- Private Methods -- #######################################

#------------TEST-------------------------------------------------------

jp = AccountCollection()
print(jp.__doc__)
jp.getAll()
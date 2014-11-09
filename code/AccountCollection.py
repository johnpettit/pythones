#-*- coding: utf-8 -*-

from EVBase import EVBase
from EVElasticSearch import EVElasticSearch
from Account import *

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

        res = self._es.es.search(index='names', doc_type='address')
        #TODO check result
        results = res['hits']['hits']
        for account in results:
            print(account['_id'])
            add = Account()
            add.getByID(account['_id'])
            self._accounts.append(add)
        print(len(self._accounts))
        return True

    #######-- Private Methods -- #######################################

#------------TEST-------------------------------------------------------

jp = AccountCollection()
#print(jp.__doc__)
jp.getAll()
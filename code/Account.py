#-*- coding: utf-8 -*-

from EVBase import EVBase
from EVElasticSearch import EVElasticSearch

class Account(EVBase, EVElasticSearch):
    """Account Object"""

    _indexName = "account"

    _fields = {
        "id": str,
        "FirstName": str,
        "LastName": str,
    }

    _requiredFields = ["FirstName", "LastName"]

    def __init__(self):
        self._fields = {
            "id": "",
            "FirstName": "",
            "LastName": "",
        }

    def create(self):
        #check for values and type
        for field in self._requiredFields:
            if self._fields[field] == '':
                self._errorMessage = 'Required Field Missing: ' + field
                return False

        #good  ADD RECORD
        res = self._es.es.index(index='names', doc_type='address', body={'FirstName': self._fields['FirstName'], 'LastName': self._fields['LastName']})
        #print(res)
        self._es.es.indices.refresh(index='names')
        self._fields['id'] = res['_id']
        return True

    def getByID(self, id):
        if id == '':
            #TODO better to Throw
            self._errorMessage = 'Required Field Missing: id'
            return False

        res = self._es.es.get(index='names', doc_type='address', id=id)
        #TODO check result
        print(res)
        self._fields['id'] = id
        self._fields['FirstName'] = res['_source']['FirstName']
        self._fields['LastName'] = res['_source']['LastName']
        return res

jp = Account()
print(jp.__doc__)
jp._fields['FirstName'] = 'John'
jp._fields['LastName'] = 'Smith'
res = jp.create()
if res:
    print(res)
else:
    print(jp.geterrormessage())

result = jp.getByID(jp._fields['id'])
if result:
    print(jp._fields['FirstName'])
else:
    print(jp.geterrormessage())


    


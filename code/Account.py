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

    required_fields = ["FirstName", "LastName"]

    def __init__(self):
        self._fields = {
            "id": "",
            "FirstName": "",
            "LastName": "",
        }

    def create(self):
        #check for values
        returnval = True
        for field in self.required_fields:
            if self._fields[field] == '':
                returnval = False

        #good  ADD RECORD
        return returnval

jp = Account()
print(jp.__doc__)
res = jp.create()
if res:
    print(res)
else:
    print('HI')


    


#-*- coding: utf-8 -*-

from EVBase import EVBase

class Account(EVBase):
    """Account Object"""

    _indexName = "account"

    fields = {
        "id": str,
        "FirstName": str,
        "LastName": str,
    }

    def __init__(self):
        self.data = {
            "id": None,
            "FirstName": None,
            "LastName": None,
        }

#jp = Account()
#print(jp.__doc__)




    


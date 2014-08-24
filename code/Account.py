#-*- coding: utf-8 -*-

from EVBase import EVBase

class Account(EVBase):
    """Account Object"""

    _indexName = "account"


jp = Account()
print(jp.__doc__)
print(jp.internalCount)




    


#-*- coding: utf-8 -*-

class EVBase:
    """Base Class for EV Data Objects"""

    _errorMessage = ''

    def __init__(self):
        self._errorMessage = ''

    def geterrormessage(self):
        return self._errorMessage

# self test

#jp = EVBase()
#print(jp.__doc__)
#print(jp.showCount())
#jp.insert()

#-*- coding: utf-8 -*-

from DataItem import DataItem

class Account(DataItem):
    fields = {
            "FirstName":str,
            "LastName":str,
            "NickName":str,
            "Street1":str,
            "Street2":str,
            "City":str,
            "State":str,
            "Zip":str,
            }

    def __init__(self):
        self.data = {
                "FirstName":None,
                "LastName":None,
                "NickName":None,
                "Street1":None,
                "Street2":None,
                "City":None,
                "State":None,
                "Zip":None,
                }

    


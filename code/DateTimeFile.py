import csv
from Account import Account
from elasticsearch import Elasticsearch
from datetime import date

es = Elasticsearch('192.168.2.90:9200/')

acs = []
count = 0
with open('data2.csv','rb') as datafile:
    datareader = csv.reader(datafile,delimiter=',')
    for row in datareader:
        print row
        count += 1
        new = Account()
        new.fields['FirstName'] = row[0]
        new.fields['LastName'] = row[1]
        new.fields['NickName'] = row[2]
        new.FirstName = row[0]
        new.LastName = row[1]
        new.NickName = row[2]
        new.Street1 = row[3]
        new.Street2 = row[4]
        new.City = row[5]
        new.State = row[6]
        new.Postal = row[7]
        new.Country = row[8]
        new.CreateDate = row[9]
        new.ModifiedDate = row[10]
        acs.append(new)

for acc in acs:
    #for k,v in acc.fields.items():
    print "First Name  : " + acc.FirstName
    print "Last Name  : " + acc.LastName
    cdate = acc.CreateDate
    mdate = acc.ModifiedDate
    cpieces = cdate.split('/')
    mpieces = mdate.split('/')
    cgoodDate = date(int(cpieces[2]),int(cpieces[0]),int(cpieces[1]))
    print cgoodDate.strftime('%m/%d/%Y')
    mgoodDate = date(int(mpieces[2]),int(mpieces[0]),int(mpieces[1]))
    es.index('names','address', {'FirstName':acc.FirstName,'LastName':acc.LastName,'NickName':acc.NickName,'Street1':acc.Street1,'Street2':acc.Street2,'City':acc.City,'State':acc.State,'Postal':acc.Postal,'Country':acc.Country,'CreateDate':cgoodDate.strftime('%m/%d/%Y'),'ModifiedDate':mgoodDate.strftime('%m/%d/%Y')})

es.refresh('names')


print len(acs)

print count



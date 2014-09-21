import csv
from Account import Account
from elasticsearch import Elasticsearch

es = Elasticsearch('192.168.2.90:9200/')

acs = []
count = 0
with open('data.csv','rb') as datafile:
    datareader = csv.reader(datafile,delimiter=',')
    for row in datareader:
        print(row)
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
    #    print k + " : " + v
    #print "First Name : " + acc.fields['FirstName']
    #print "Last Name  : " + acc.fields['LastName']
    print("First Name  : " + acc.FirstName)
    print("Last Name  : " + acc.LastName)
    es.index('names','address', {'FirstName':acc.FirstName,'LastName':acc.LastName,'NickName':acc.NickName,'Street1':acc.Street1,'Street2':acc.Street2,'City':acc.City,'State':acc.State,'Postal':acc.Postal,'Country':acc.Country,'CreateDate':acc.CreateDate,'ModifiedDate':acc.ModifiedDate})

es.indices.refresh(index='names')

print(len(acs))

print(count)



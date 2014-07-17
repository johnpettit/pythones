import json

data = [{'Hola':'Hello','Hoi':'Hello','noun':'hello'}]

print 'DATA:',(data)

print dir(json)
print json.__file__

json_end = json.dumps(data)

print "Encoded:"
print json_end

dec_data = json.loads(json_end)

print "Decoded:"
print dec_data



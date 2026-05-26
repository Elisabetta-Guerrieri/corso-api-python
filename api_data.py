import json

raw_data='{"server":"amazon","config":{"port": 80,"active": true}, "macchina": "audi"}'

data = json.loads(raw_data)
print (data["config"]["port"])
print(data["macchina"])
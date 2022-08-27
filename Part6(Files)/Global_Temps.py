import json

json_data_source = 'temperature_anomaly.json'

with open(json_data_source, encoding='utf-8') as data:
    anomalies = json.load(data)

print(anomalies)
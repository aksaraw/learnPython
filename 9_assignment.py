import json
import csv

path = '/Users/jakaaksara/Documents/Private/Data Scientist Material/Data Scientist - Purwadhika/Code/MODUL1/9_files/'

########################
#JSON to CSV

filejson = open(path+'9_filejson.json', 'r')
bacajson = json.load(filejson)
# print(bacajson)
outputjson_key = bacajson[0].keys()
# print(outputjson_key)

tocsv = open(path+'9_tocsv.csv', 'w')
tulis = csv.DictWriter(tocsv, fieldnames=outputjson_key) 
tulis.writeheader()
tulis.writerows(bacajson)

########################
#CSV to JSON

filecsv = open(path+'9_filecsv.csv', 'r')
bacacsv = csv.DictReader(filecsv)

csv_list = []
for i in bacacsv:
    csv_list.append(dict(i)) 
# print(csv_list)

tojson = open(path+'9_tojson.json', 'w')
json.dump(csv_list, tojson)





#!/usr/bin/env python

from sqlalchemy import *
import json
import sys
import cgi

# function that gets current data for all stations and returns as JSON
db = create_engine('sqlite://bikedb')
conn = db.connect()

dataQuery = conn.execute("""select * 
	from montrealdatanow
	inner join montrealstations 
	on montrealdatanow.id == montrealstations.id""")

dataList = []
for row in dataQuery:
	dataList.append({'id': row['id'], 
		'name': row['name'],
		'nbBikes': row['nbBikes'],
		'nbEmptyDocks': row['nbEmptyDocks'],
		'lastCommWithServer': row['lastCommWithServer']})
stations = json.dumps({'mtlData': dataList})

conn.close()

sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")
result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['data'] = stations
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()

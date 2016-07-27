import json, requests, codecs, sys
from time import strftime
from datetime import datetime

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

with open('observations.json') as data_file:
    observations = json.load(data_file)


# determine spawn points
spawnpoints = []
for obs in observations:
        spawnpoints.append(obs['spawnpoint_id'])

# drop duplicates
spawnpoints = list(set(spawnpoints))

for spawnpoint in spawnpoints:
        print spawnpoint
        for obs in observations:
                if obs['spawnpoint_id'] == spawnpoint:
                        print datetime.fromtimestamp(int(obs["disappear_time"]/1000)).strftime('%Y-%m-%d %H:%M:%S'),
                        print obs['pokemon_name']
        print "----"


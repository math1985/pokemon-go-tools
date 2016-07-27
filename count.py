import json, requests, codecs, sys
from time import strftime
from datetime import datetime

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

counter = {}
final_count = {}

with open('observations.json') as data_file:
    observations = json.load(data_file)


# determine spawn points
spawnpoints = []
for obs in observations:
        spawnpoints.append(obs['spawnpoint_id'])

# drop duplicates
spawnpoints = list(set(spawnpoints))

for spawnpoint in spawnpoints:
        observations_at_spawnpoint = []
        for obs in observations:
                if obs['spawnpoint_id'] == spawnpoint:
                        observations_at_spawnpoint.append(obs['pokemon_name'])
        observations_at_spawnpoint = list(set(observations_at_spawnpoint))
        for pokemon in observations_at_spawnpoint:
                if pokemon in counter:
                        counter[pokemon] = counter[pokemon] + 1
                else:
                        counter[pokemon] = 1

for pokemon, number in sorted(counter.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (pokemon, number)


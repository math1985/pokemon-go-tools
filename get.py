# -*- coding: utf-8 -*-

import json, requests, codecs, sys
from geopy.distance import vincenty
from termcolor import colored

server = 'http://ENTER.SERVER.HERE/'

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

url = server + 'raw_data?pokemon=true&pokestops=false&gyms=false&scanned=false'
resp = requests.get(url=url)
observations = json.loads(resp.text)

known_pokemon = [u'Caterpie', u'Chansey', u'Charmander', u'Dratini', u'Drowzee', u'Eevee', u'Electabuzz', u'Fearow',
                                        u'Gastly', u'Goldeen', u'Golduck', u'Hypno', u'Jigglypuff', u'Jynx', u'Kakuna', u'Kingler', u'Koffing',
                                        u'Krabby', u'Machop', u'Magikarp', u'Magnemite', u'Meowth', u'Nidoran♀', u'Oddish', u'Omanyte', u'Onix',
                                        u'Paras', u'Pidgeot', u'Pidgeotto', u'Pidgey', u'Poliwag', u'Porygon', u'Psyduck', u'Ratciate', u'Rattata',
                                        u'Seel', u'Shellder', u'Slowpoke', u'Spearow', u'Staryu', u'Tentacruel', u'Tentacool', u'Venonat', u'Vuplix', u'Weedle',
                                        u'Zubat', u'Horsea'],

# open old observations
with open('observations.json') as data_file:
    observations_out = json.load(data_file)

# check which encounters we already saw
seen_observation_ids = []
for obs in observations_out:
        seen_observation_ids.append(obs['encounter_id'])

for observations2 in observations.values():
        for observation in observations2:
                already_seen = False
                for seen_observation_id in seen_observation_ids:
                        if observation['encounter_id'] == seen_observation_id:
                                already_seen = True
                if not already_seen:
                        observations_out.append(
                                {
                                        "spawnpoint_id": observation['spawnpoint_id'],
                                        "pokemon_name": observation['pokemon_name'],
                                        "encounter_id": observation['encounter_id'],
                                        "disappear_time": observation['disappear_time'],
                                        "latitude": observation['latitude'],
                                        "longitude": observation['longitude']
                                }
                        )
                if not (observation['pokemon_name'] in known_pokemon[0]):
                        location = (observation['latitude'], observation['longitude'])
                        my_location = (52.035538, 4.496642)
                        distance = (vincenty(location, my_location).km)

                        string = "New pokemon: " + observation['pokemon_name'] + "; distance " + format(distance, '.2f') + "km"

                        if distance < 0.2:
                                color='magenta'
                        elif distance < 0.5:
                                color='red'
                        else:
                                color='grey'

                        print colored(string, color)

f = open('observations.json', 'w')
f.write(json.dumps(observations_out))

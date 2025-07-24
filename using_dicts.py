airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
print(f"{airports['MCO'] = }")
airports['VCE'] = 'Venice'
airports['MCO'] = "Mouseville"
print(f"{airports['MCO'] = }")
print(f"{airports = }\n")
# print(f"{airports['FCO'] = }")
print(f"{'FCO' in airports = }")
print(f"{'MCO' in airports = }")
print(f"{airports.get('MCO') = }")
print(f"{airports.get('FCO') = }")
print(f"{airports.get('FCO', 'NOT FOUND') = }")

print(f"{airports.setdefault('MCO') = }")
print(f"{airports.setdefault('FCO', 'Rome') = }")
print(f"{airports = }")
print('-' * 60)

for key in airports:
    print(key)
print('-' * 60)

for value in airports.values():
    print(value)
print('-' * 60)

for code, city in airports.items():
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

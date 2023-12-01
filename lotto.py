#változók
szelvenyek = []
xszelveny = []

number_to_word = {
    1: 'egy',
    2: 'kettő',
    3: 'három',
    4: 'négy',
    5: 'öt',
    6: 'hat',
    7: 'hét',
    8: 'nyolc',
    9: 'kilenc',
    10: 'tíz',
    11: 'tizenegy',
    12: 'tizenkettő',
    13: 'tizenhárom',
    14: 'tizennégy',
    15: 'tizenöt',
    16: 'tizenhat',
    17: 'tizenhét',
    18: 'tizennyolc',
    19: 'tizenkilenc',
    20: 'húsz',
    21: 'huszonegy',
    22: 'huszonkettő',
    23: 'huszonhárom',
    24: 'huszonnégy',
    25: 'huszonöt',
    26: 'huszonhat',
    27: 'huszonhét',
    28: 'huszonnyolc',
    29: 'huszonkilenc',
    30: 'harminc',
    31: 'harmincegy',
    32: 'harminckettő',
    33: 'harminchárom',
    34: 'harmincnégy',
    35: 'harmincöt',
}

variables_dict = {
    'egy': 0,
    'kettő': 0,
    'három': 0,
    'négy': 0,
    'öt': 0,
    'hat': 0,
    'hét': 0,
    'nyolc': 0,
    'kilenc': 0,
    'tíz': 0,
    'tizenegy': 0,
    'tizenkettő': 0,
    'tizenhárom': 0,
    'tizennégy': 0,
    'tizenöt': 0,
    'tizenhat': 0,
    'tizenhét': 0,
    'tizennyolc': 0,
    'tizenkilenc': 0,
    'húsz': 0,
    'huszonegy': 0,
    'huszonkettő': 0,
    'huszonhárom': 0,
    'huszonnégy': 0,
    'huszonöt': 0,
    'huszonhat': 0,
    'huszonhét': 0,
    'huszonnyolc': 0,
    'huszonkilenc': 0,
    'harminc': 0,
    'harmincegy': 0,
    'harminckettő': 0,
    'harminchárom': 0,
    'harmincnégy': 0,
    'harmincöt': 0
}



#adatgyűjtés
for i in range(int(input("hany szelvényed van?: "))):
    print(f"{i+1}. szelvény")
    for x in range(int(input("hanyas lottó?:"))):
        xszelveny.append(int(input(f"{x+1}. szam:")))
    szelvenyek.append(xszelveny)
    xszelveny = []


#debug
print(szelvenyek)

#adatfeldolgozáa
for i  in range(len(szelvenyek)):
    for x in range(len(szelvenyek[i])):
        a = number_to_word[szelvenyek[i][x]]
        variables_dict[a] += 1

for key, value in variables_dict.items():
    print(f"{key}: {value}")

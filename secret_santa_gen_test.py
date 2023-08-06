import pandas as pd
import random as rnd

# still running into issue of sometimes a santa has no giftee options


relationships = {
    "Andre": ['Shannon'],
    "Shannon": ['Andre'],
    "Alex": ['Madz'],
    "Madz": ['Alex'],
    "Andrea": [],
    "Ian": ['Lauren', 'Andre'],
    "Lauren": ['Ian'],
    "Allison": [],
    "Jesse": ['Miranda'],
    "Miranda": ['Jesse']
}

a = pd.DataFrame(relationships.items(), columns=['Person', 'Related'])
a

santas = list(relationships.keys())
a['Giftee'] = None
b = None
i=0

while i < len(a):
    
    if a['Giftee'].isnull().sum() < len(santas):
        print("NOT ENOUGH GIFTEES AVAILABLE")
        # break
    
    i+=1
    
    num = rnd.randint(0, len(santas)-1)

    santa = a[a['Person'].isin(santas)]['Person'].iloc[num]

    santas.remove(santa)

    b = a[a["Person"] != santa]

    not_related = b[b["Related"].apply(lambda x: santa not in x)]

    giftee_choice = not_related[~not_related['Person'].isin(a['Giftee'])]['Person'].sample(n=1).iloc[0]

    a.loc[a['Person'] == santa, 'Giftee'] = giftee_choice
    
a

emails = {
    "Andre": "ama@gmail.com"
}

emails[a['Person'][0]]

a[['Person', 'Giftee']]



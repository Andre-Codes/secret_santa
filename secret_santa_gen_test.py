import pandas as pd
import random as rnd



def generate_santas(people_data):
    
    while True:
        
        santas = list(people_data['Person'].values)
        people_data['Giftee'] = None
        i=0
        
        try:
            while i < len(people_data):
                
                if people_data['Giftee'].isnull().sum() < len(santas):
                    print("NOT ENOUGH GIFTEES AVAILABLE")
                    break
                
                i+=1
                
                rand_santa = rnd.randint(0, len(santas)-1)

                santa = people_data[people_data['Person'].isin(santas)]['Person'].iloc[rand_santa]

                santas.remove(santa)

                all_others = people_data[people_data["Person"] != santa]

                not_related = all_others[all_others["Related"].apply(lambda related: santa not in related)]

                giftee = not_related[~not_related['Person'].isin(people_data['Giftee'])]['Person'].sample(n=1).iloc[0]

                people_data.loc[people_data['Person'] == santa, 'Giftee'] = giftee
            
            missing_giftee = people_data['Giftee'].isnull().sum()
            
            if missing_giftee == 0:
                break 
            else:
                "Trying again..."    
        
        except ValueError:
            print("Trying again...")
                
    return people_data
        

# Convert JSON to a DataFrame
def create_df(data):
    df = pd.DataFrame.from_dict(data, orient='index')

    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Person'}, inplace=True)
    
    return df


people = {
    'Andre': {
        'Related': ['Shannon'],
        'Email': 'alice@example.com'
    },
    'Shannon': {
        'Related': ['Andre'],
        'Email': 'bob@example.com'
    },
    'Alex': {
        'Related': ['Madz'],
        'Email': 'charlie@example.com'
    },
    'Madz': {
        'Related': ['Alex', 'Lydia'],
        'Email': 'david@example.com'
    },
    'Lydia': {
        'Related': ['Madelyn'],
        'Email': 'david@example.com'
    },
    'Ian': {
        'Related': ['Lauren'],
        'Email': 'david@example.com'
    },
    'Lauren': {
        'Related': ['Ian'],
        'Email': 'david@example.com'
    },
    'Andrea': {
        'Related': [],
        'Email': 'david@example.com'
    },
    'Allison': {
        'Related': [],
        'Email': 'david@example.com'
    }
}

players = create_df(people)

results = generate_santas(players)

results
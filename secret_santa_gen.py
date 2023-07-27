import random
import pandas as pd

friends = ["Andre", "Shannon", "Alex", "Madelyn", "Ian", "Lauren", "Andrea"]

related = [("Andre", "Shannon"), ("Alex", "Madelyn"), ("Ian", "Lauren"), "Andrea"]

santas = friends.copy()
random.shuffle(santas)

# Create a dictionary to hold the secret santa assignments
secret_santas = {}

# Assign each person to another, skipping if related
while (len(secret_santas) < len(friends)):
    for friend in friends:
        for santa in santas:
            # Check if the friend and potential receiver are related
            if friend != santa and (friend, santa) not in related and (santa, friend) not in related:
                # Assign the receiver and remove them from the list
                secret_santas[friend] = santa
                santas.remove(santa)
                break
    if len(secret_santas) == len(friends):
        df = pd.DataFrame(list(secret_santas.items()), columns=['Santa', 'Receiver'])
        print(df)
    else:
        santas = friends.copy()
        random.shuffle(santas)
        secret_santas = {}
        

##########################################
##########################################
# ALTERNATE METHOD (simplified)


# List of lists where each sublist contains people related to each other
related = [["Andre", "Shannon"], ["Alex", "Madelyn"], ["Ian", "Lauren", "Peter"], ["Andrea"]]

# Get the length of the largest group of related people
# This is the number to skip by, ensuring related people do not get paired
skip = len(max(related, key=len))

# Shuffle the the friends (mainting relations)
random.shuffle(related)

# Initialize an empty list to hold the new friends list
friends = []
# Initialize an empty dictionary to hold the secret santa assignments
secret_santas = {}

# Flatten the list, removing relation sublists
# Go through each group of related people
for person in related:
    # If the group is a list or relations, extend the friends list with the group
    if isinstance(person, list):
        friends.extend(person)
    # If the group is not a list, append the person to the friends list
    else:
        friends.append(person)
        
# Append the first 'skip' friends to the end of the friends list to allow 
# wrapping around for the last few friends to have a partner
friends.extend(friends[:skip])
        
# Go through each friend
for index, santa in enumerate(friends):
    # If the friend is not one of the last 'skip' (appended) friends in the list
    if index <= (len(friends) - (skip + 1)):
        # Assign the friend a secret santa who is 'skip' places ahead in the list
        secret_santas[santa] = friends[index+skip]

# Print the secret santa assignments
secret_santas




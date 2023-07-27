import random

# List of sublists containing people related to each other
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

# Flatten the list, removing relation sublists while maintaing positions
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




import random

# List of lists containing people related to each other
related = [["Andre", "Shannon", "Arwen"], ["Alex", "Madelyn"], ["Ian", "Lauren"], ["Andrea"], ["Bob"], ["Jesse", "Miranda"]]

# Shuffle the friends (maintaining relations)
random.shuffle(related)

# Get the length of the largest group of related people
# This is the number to skip by, ensuring related people do not get paired
max_relation = len(max(related, key=len))

# Flatten the list to prepare for
all_friends = [name for sublist in related for name in sublist]
all_friends

name_cnt = len(all_friends)

# If the max len for any one relationship is greater than half to total number of
# individuals there will not be enough assignments available
if max_relation > (name_cnt / 2):
    pass

# Initialize an empty dictionary to hold the secret santa assignments
secret_santas = {}
     
# Append the first 'max_relation' friends to the end of the friends list to allow
# wrapping around for the last few friends to have a partner
all_friends.extend(all_friends[:max_relation])
all_friends
        
# Go through each friend
for index, santa in enumerate(all_friends):
    # If the friend is not one of the last 'max_relation' (appended) friends in the list
    if index <= (len(all_friends) - (max_relation + 1)):
        # Assign the friend a secret santa who is 'max_relation' places ahead in the list
        secret_santas[santa] = all_friends[index+max_relation]

# Print the secret santa assignments
secret_santas




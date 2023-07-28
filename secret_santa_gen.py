import random
import pandas as pd


def contains_relationship(people_list):
    for item in people_list:
        if isinstance(item, list):
            return True
    return False


# List of lists containing people related to each other
people = ["Andre", "Shannon", "Arwen", "Jesse", "Miranda", "Andrea",
          "Alex", "Madelyn", "Ian", "Lauren"]

# EXAMPLE - not enough non-related people
# related = [["Andre", "Shannon", "Arwen", "Jesse", "Miranda", "Andrea"],
#            ["Alex", "Madelyn"], ["Ian", "Lauren"]]

# Shuffle the friends (maintaining relations)
random.shuffle(people)
print(people)

if contains_relationship(people):
    # Get the length of the largest group of related people
    # This is the number to skip by when assigning pairs, ensuring related people do not get paired
    max_relation = len(max(people, key=len))
    # Flatten the list to prepare for assignments
    all_friends = [name for sublist in people for name in sublist]
    name_cnt = len(all_friends)
    # If the max len for any one relationship is greater than half to total number of
    # individuals there will not be enough assignments available
    if max_relation > (name_cnt / 2):
        print("NOT ENOUGH TO ASSIGN - RELATED PEOPLE WILL BE PAIRED")
    # Append the first 'max_relation' friends to the end of the friends list to allow
    # wrapping around for the last few friends to have a partner
    all_friends.extend(all_friends[:max_relation])
else:
    all_friends = people
    max_relation = 1
    all_friends.extend(all_friends[:max_relation])

# for item in people:
#     if isinstance(item, list):
#         # Get the length of the largest group of related people
#         # This is the number to skip by when assigning pairs, ensuring related people do not get paired
#         max_relation = len(max(people, key=len))
#         # Flatten the list to prepare for assignments
#         all_friends = [name for sublist in people for name in sublist]
#         name_cnt = len(all_friends)
#         # If the max len for any one relationship is greater than half to total number of
#         # individuals there will not be enough assignments available
#         if max_relation > (name_cnt / 2):
#             print("NOT ENOUGH TO ASSIGN - RELATED PEOPLE WILL BE PAIRED")
#         # Append the first 'max_relation' friends to the end of the friends list to allow
#         # wrapping around for the last few friends to have a partner
#         all_friends.extend(all_friends[:max_relation])


# Initialize an empty dictionary to hold the secret santa assignments
secret_santas = {}

# Go through each friend
for index, santa in enumerate(all_friends):
    # If the friend is not one of the last 'max_relation' (appended) friends in the list
    if index <= (len(all_friends) - (max_relation + 1)):
        # Assign the friend a secret santa who is 'max_relation' places ahead in the list
        secret_santas[santa] = all_friends[index + max_relation]

# Print the secret santa assignments
# Create a list of tuples with name pairs
assignments = [(santa, receiver) for santa, receiver in secret_santas.items()]

# Convert the list of tuples to a DataFrame
df = pd.DataFrame(assignments, columns=['Santa', 'Receiver'])
print(df.sort_values('Santa'))

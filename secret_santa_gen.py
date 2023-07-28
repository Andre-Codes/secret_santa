import random
import pandas as pd


def contains_relationship(people_list):
    for item in people_list:
        if isinstance(item, list):
            return True
    return False


# List containing the people to be assigned to each other
# Can contain lists containing people related to each other
people = [
    ["John", "Jane"], ["Michael"], ["Emily", "Robert"],
    ["Olivia"], ["William"], ["Sophia", "James", "Ava"],
    ["David", "Mia"], ["Joseph"], ["Isabella"], ["Daniel"],
    ["Emma"], ["Andrew"], ["Charlotte", "Matthew"], ["Amelia"]
]

# EXAMPLE - not enough non-related people
# related = [["Sophia", "James", "Ava", "John", "Jane", "Michael"],
#            ["Emma", "Andrew"], ["Charlotte"], ["Robert"]]

# Shuffle the friends (maintaining relations)
random.shuffle(people)

if contains_relationship(people):
    # Get the length of the largest group of related people
    # This is the number to skip by when assigning pairs, ensuring related people do not get paired
    max_relation = len(max(people, key=len))
    # Shuffle people within a relationship for increased randomness
    for relations in people:
        random.shuffle(relations)
    # Flatten the list to prepare for assignments
    people = [name for sublist in people for name in sublist]
    # Get the total count of individuals
    name_cnt = len(people)
    # If the max len for any one relationship is greater than half to total number of
    # individuals there will not be enough assignments available
    if max_relation > (name_cnt / 2):
        print("NOT ENOUGH TO ASSIGN - RELATED PEOPLE WILL BE PAIRED")
    # Append the first 'max_relation' friends to the end of the friends list to allow
    # wrapping around for the last few friends to have a partner
    people.extend(people[:max_relation])
else:
    max_relation = 1
    people.extend(people[:max_relation])

# Initialize an empty dictionary to hold the secret santa assignments
secret_santas = {}

# Go through each person in the list
for index, santa in enumerate(people):
    # If the friend is not part of the last 'max_relation' (appended) friends in the list
    if index <= (len(people) - (max_relation + 1)):
        # Assign the friend a secret santa who is 'max_relation' places ahead in the list
        secret_santas[santa] = people[index + max_relation]

# Print the secret santa assignments
# Create a list of tuples with name pairs
assignments = [(santa, receiver) for santa, receiver in secret_santas.items()]

# Convert the list of tuples to a DataFrame
df = pd.DataFrame(assignments, columns=['Santa', 'Receiver'])
print(df.sort_values('Santa'))

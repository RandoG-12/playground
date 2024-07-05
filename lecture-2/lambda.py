# a list of dictionaries
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# people.sort()
# ^ this causes an error
# doesn't know how to sort

#define sort funtions
def fname(person):
    '''
    sort by name
    '''
    return person["name"]

def fhouse(person):
    '''
    sort by house
    '''
    return person["house"]

people.sort(key=fname)
print(people)

people.sort(key=fhouse)
print(people)

# this is the lambda syntax for sorting
people.sort(key=lambda person: person["name"])
print(people)

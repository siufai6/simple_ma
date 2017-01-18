# list comprehension
# syntax: [ (do something on item) for item in list if condition ]

l = [1,2,3,4,5]
new_l = [ x*2 for x in l if x < 4]
# [2, 4, 6]

# appends an item to a list if not in list now
l = [1,2,3,4,5]
y=[1,10]
new_l = l + [ x for x in y if x not in l]
# [1, 2, 3, 4, 5, 10]

# create a duple from a few list based on a few conditions
l=[1,2,3,4,5]
m=[1,3,5]
n=['testing1','testing2']
new_l = [ (a,b,c) for a in l for b in m for c in n if a>b and c!='testing2']
# [(2, 1, 'testing2'), (3, 1, 'testing2'), (4, 1, 'testing2'), (4, 3, 'testing2'), (5, 1, 'testing2'), (5, 3, 'testing2')]


# to do : lambda, pandas dataframe
# lambda ..
# lambda input : logic

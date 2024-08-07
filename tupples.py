
# tupples!

# what are tupples?
# Tupples are a data type that are simular to lists, with the exception that they are immutable
# immutable : you cannot change or edit the data of a tuple, but we can reassign what is stored in a variable 
# ordered : just like lists they have an order, we can access elements in a tuple by indexing
# like lists, tuples can store a variety of objects, any data type, including duplicate elements
# why bother?
# you can create a collection of data that cannot be changed by you or another developer
# iterating over a tuple is much faster than iterating over a list
# 
# 
# we can use ( ) to define tuples, just like a list we use [ ] empty_list = [ ]
empty_tup = () #      empty tuple
# singleton, tuple with one element inside of it
singleton = ('element',) #  requires a trailing comma for python to see it as a tuple

print(type(singleton))
print(singleton)


# tuple with multiple items inside of it
# with multiple items inside of a tuple, you no longer need a trailingcomma

pop_tup = ('this','is','a','populated','tuple')
print(type(pop_tup))
print(pop_tup)

variety_tup = (4,'five',6.0,)
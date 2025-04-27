import random

print(random.random())   ## generates a random nmber between o.0 and 1.0

list1 = [1, 2, 3, 4, 5, 6]

print(random.choice(list1))   ## choose a random number from list1 ( work for list, tuple, sets )

print(random.sample(list1,3))   ## generates a list from list1 with 3 value

print(random.shuffle(list1))   ## it shuffle the list1

random.seed(5)
print(random.random())    ## generates a random number between 0.0 and 1.0

print(random.randint(2,30))    ## randint(start, end)

random.seed(5)   ## 
print(random.randint(2, 30))







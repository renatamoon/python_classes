# LENGH AND SUM WITH DICTIONARIES

grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total/length

print("THE AVERAGE IS: ", average) # THE AVERAGE IS:  86.25

print("=-"*20)

# ----- looking back to lists, dictionaries and sets which one of these are the best choice:

grades = [80, 75, 90, 100] # a list is the better choice
grades1 = (80, 75, 90, 100) # a tuple is not a good choice once you can't change it
grades2 = {80, 75, 90, 100} # a set is not a good choice once you can't input equal values
# ARGUMENT MUTABILITY IN PYTHON

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}


def see_friend(friends, name):
    print(id(friends))  # 140590572217472
    friends[name] = 0


print(id(friends_last_seen))  # 140590572217472
print(id(friends_last_seen['Rolf']))  # 9789920

see_friend(friends_last_seen, 'Rolf')

print(id(friends_last_seen['Rolf']))  # 9788928
print(id(friends_last_seen))  # 140590572217472

# ---- another example

age = 20


def increase_age(current_age):
    current_age = current_age + 1


print(id(age))  # 9789568
increase_age(age)
print(id(age))  # 9789568

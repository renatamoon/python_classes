# MAP FUNCTION

friends = ["Rolf", "Jose", "Randy", "Anna", "Mary"]

friends_lower = map(lambda x: x.lower(), friends)  # map function
friends_lower_1 = [friend.lower() for friend in friends]  # list comprehension
friends_lower_2 = (friend.lower() for friend in friends)  # list comprehension
print(next(friends_lower))


# when you can use map
class User:
    def __int__(self, username, password):
        self.username = username
        self.password = password


    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"])


user = [
    {"username": "rolf", "password": "123"},
    {"username": "tecladoisokay", "password": "youaretoo"}
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)

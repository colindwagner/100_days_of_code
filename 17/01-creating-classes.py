

class User:
    def __init__(self, username, id):
        ## initialize attributes
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        user.following += 1

user_1 =  User("Colin", 1)
user_2 =  User("CC", 2)

user_1.follow(user_2)


print(user_1.username)
print(user_1.followers)
print(user_2.followers)
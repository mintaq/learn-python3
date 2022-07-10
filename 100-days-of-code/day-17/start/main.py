class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def set_name(self, name):
        self.name = name

    def follow(self, user):
        """Increase followers of a user.

        Keyword arguments:
        name: User
        """
        user.followers += 1
        self.following += 1


user_1 = User("001", "Minh")
user_2 = User("002", "Thu")
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)

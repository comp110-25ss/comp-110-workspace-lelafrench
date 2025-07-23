"""Class writing practice."""


# define the class
class Profile:
    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create a Profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str):
        """Write a tweet and post if not private."""
        if self.private is False:
            print(msg)

    def __str__(self) -> str:
        """String represetnation of a Profile object."""
        if self.private:
            return f"{self.username}: Private"
        else:
            return f"{self.username}: Public"


# instantiate the class
user1: Profile = Profile("110_rulez")
user1.private = False
user1.tweet("OOP is cool!")
print(user1)

# https://randomuser.me/api/

import requests
from datetime import datetime
from time import sleep


class User:
    """A user class, used for program flow. Use with respect."""

    def __init__(
        self, first_name, last_name, email, username, password, registered_date
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.registered_date = registered_date

    def __str__(self):
        """Returns users name and email."""
        return f"{self.first_name} {self.last_name} <{self.email}>"

    def __int__(self):
        """Returns the number of days since the users registration.
        Date default format: 2007-07-09T05:51:59.390Z"""
        registered_date = datetime.strptime(
            self.registered_date, "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        today = datetime.now()
        return (today - registered_date).days

    def __repr__(self):
        """Returns users first and last name with their username."""
        return f"<{self.first_name} '{self.username}' {self.last_name}>"


class UserFactory:
    def __init__(self, max_users=10):
        self.max_users = max_users
        self.users_generated = 0
        self.users = []

    def create_new_user(self):
        """This function gets a random user from an API and returns an User object.
        Returns (bool, User or None) if bool is False, then None."""

        resp = requests.get("https://randomuser.me/api/")
        if not resp.ok:
            return False, None
        resp = resp.json()["results"][0]
        new_user = User(
            first_name=resp["name"]["first"],
            last_name=resp["name"]["last"],
            email=resp["email"],
            username=resp["login"]["username"],
            password=resp["login"]["password"],
            registered_date=resp["registered"]["date"],
        )
        return True, new_user

    def fill_users_list(self):
        """Fills the user list in the object with the number of users equal to the self.max_users
        if there are errors, the users list may be shorter."""
        for idx in range(self.max_users):
            success, user = self.create_new_user()
            if not success:
                continue
            self.users.append(user)

    def get_users(self):
        return self.users

    # def __iter__(self):
    #     """Function generating user every time it gets a response from the API.
    #     If you need to check new user less than every 500ms, use fill_users_list method
    #     and then iterat over a per-prepared list of users."""
    #     while True:
    #         success, user = self.create_new_user()
    #         if not success:
    #             continue
    #         yield user

    def __iter__(self):
        return self

    def __next__(self):
        self.users_generated += 1
        if self.users_generated > self.max_users:
            raise StopIteration
        success, new_user = self.create_new_user()
        self.users.append(new_user)
        return new_user


class UsersDatabase:
    def __init__(self):
        """self.users is like this:
        {"username": user_obj, ...}"""
        self.users = {}

    def __str__(self):
        str_tpl = "{:10.10s} | {:10.10s} | {:40.40s} | {:10.10s}\n"
        retval = "\n" + str_tpl.format("First Name", "Last Name", "E-Mail", "Username")
        retval += "-" * 79 + "\n"
        for user in self.users.values():
            retval += str_tpl.format(
                user.first_name, user.last_name, user.email, user.username
            )
        return retval

    def __setitem__(self, user_obj, user_obj_1):
        # obj[key] = val -> obj[user_obj] = user_obj_1
        if user_obj.username in self.users:
            print(f"Name {user_obj.username} is already taken, sorry!")
        else:
            self.users[user_obj.username] = user_obj_1

    def __getitem__(self, username):
        if username in self.users:
            return self.users[username]
        else:
            print("No such user in the database!")
            return


if __name__ == "__main__":
    users_database = UsersDatabase()

    user_factory = UserFactory(max_users=5)
    user_factory.fill_users_list()

    test_user_1 = User(
        first_name="Lukasz",
        last_name="Kozarski",
        email="lukasz@email.com",
        username="lukasz",
        password="asdafa",
        registered_date="",
    )
    users_database[test_user_1] = test_user_1

    print(users_database)

    test_user_2 = User(
        first_name="",
        last_name="",
        email="",
        username="lukasz",
        registered_date="",
        password="",
    )
    users_database[test_user_2] = test_user_2

    # for user in user_factory.get_users():
    #     # print(f"Assignin {user} to the users database.")
    #     users_database[user.username] = user

    for user in user_factory:
        # print(f"Assignin {user} to the users database.")
        users_database[user] = user

    print(users_database)

    print("\nGetting user from DB:")
    print("User:", users_database["anna"])

    # for user in user_factory:
    #     print(user)
    #     print(f"-- Registered for {int(user)} days.\n")
    #     sleep(0)

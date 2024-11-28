# ```python
class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'  # Уровень доступа для обычных сотрудников

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа для администраторов
        self._admin_level = admin_level  # Дополнительный уровень доступа для администраторов
        self._users = []  # Список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Only User or subclasses of User can be added.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def get_users(self):
        return self._users

    def __str__(self):
        return f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}, " \
               f"Admin Level: {self._admin_level})"


# Пример использования
if __name__ == "__main__":
    admin1 = Admin(user_id=1, name="Alice", admin_level="super")
    user1 = User(user_id=2, name="Bob")
    user2 = User(user_id=3, name="Charlie")
    user3 = User(user_id=4, name="Dav")

    admin1.add_user(user1)
    admin1.add_user(user2)
    admin1.add_user(user3)

    print("Current users:")
    for user in admin1.get_users():
        print(user)

    admin1.remove_user(2)

    print("Users after removal:")
    for user in admin1.get_users():
        print(user)

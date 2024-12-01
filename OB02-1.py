#Пример реализации системы управления учетными записями пользователей для небольшой компании на Python. В этом примере создаются классы `User` и `Admin`, где класс `Admin` наследуется от класса `User`. Также реализуются методы для добавления и удаления пользователей.

# ```python
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа для обычных сотрудников

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level})"
    def print_person(self):
        print(f"{self.__user_id} Имя: {self.__name}")

class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администраторов
        self.__admin_level = admin_level  # Дополнительный уровень доступа для администраторов
        self.__users = []  # Список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Only User or subclasses of User can be added.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def get_users(self):
        return self.__users

    def __str__(self):
        return f"Admin(ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level}, " \
               f"Admin Level: {self.__admin_level})"


# Пример использования
if __name__ == "__main__":
    admin1 = Admin(user_id = 1, name="Alice", admin_level = "super")
    user1 = User(user_id = 2, name="Bob")
    user2 = User(user_id = 3, name="Charlie")
    user3 = User(user_id = 4, name="Dav")

    admin1.add_user(user1)
    admin1.add_user(user2)
    admin1.add_user(user3)
    print("*************************************************")
#Проверка инкапсуляции:
    print(f"Пытаемся изменить id user1 с 2 на 5: ")
    user1.__user_id = 5
    print(f"user1_id: {user1.get_user_id()}— не получилось!")
    print(f"Пытаемся изменить name user1 с Bob на Boba: ")
    user1._User__name = "Boba"
    print(f"user1.name: {user1.get_name()} — получилось!")
    print("Current users:")
    print("*************************************************")

    for user in admin1.get_users():
        print(user)

    admin1.remove_user(2)

    print("Users after removal:")
    for user in admin1.get_users():
        print(user)

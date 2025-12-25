class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Приватный атрибут

    def check_password(self, password):
        return self.__password == password

    def set_password(self, current_password, new_password):
        if not self.check_password(current_password):
            print("Текущий пароль неправильный")
            return False
        if self.check_password(new_password):
            print("Пароль должен отличаться")
            return False
        self.__password = new_password
        print("все хорошо")
        return True



user = UserAccount("dima", "dima@example.com", "123")

user.set_password(input("new_password"),input("current_password"))


import datetime
import os


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        # cria o arquivo se não existir
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()
            return

        with open(self.filename, "r") as file:
            for line in file:
                data = line.strip().split(";")

                if len(data) != 4:
                    continue

                email, password, name, created = data
                self.users[email] = (password, name, created)

    def get_user(self, email):
        return self.users.get(email, -1)

    def add_user(self, email, password, name):
        email = email.strip()

        if email not in self.users:
            self.users[email] = (
                password.strip(),
                name.strip(),
                DataBase.get_date()
            )
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        user = self.get_user(email)
        if user != -1:
            return user[0] == password
        return False

    def save(self):
        with open(self.filename, "w") as file:
            for email, data in self.users.items():
                password, name, created = data
                file.write(f"{email};{password};{name};{created}\n")

    @staticmethod
    def get_date():
        return datetime.datetime.now().strftime("%Y-%m-%d")
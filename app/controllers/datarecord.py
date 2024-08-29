from app.models.user_account import UserAccount
import json
import uuid


class DataRecord():
    """Banco de dados JSON para o recurso Usuários"""

    def __init__(self):
        self.__user_accounts= []
        self.__authenticated_users = {}
        self.read()


    def read(self):
        try:
            with open("app/controllers/db/user_accounts.json", "r") as arquivo_json:
                user_data = json.load(arquivo_json)
                self.__user_accounts = [UserAccount(**data) for data in user_data]
        except FileNotFoundError:
            self.__user_accounts.append(UserAccount('Guest', '000000'))


    def book(self,username,password):
        new_user= UserAccount(username,password)
        self.__user_accounts.append(new_user)
        with open("app/controllers/db/user_accounts.json", "w") as arquivo_json:
            user_data = [vars(user_account) for user_account in \
            self.__user_accounts]
            json.dump(user_data, arquivo_json)


    def getCurrentUser(self,session_id):
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id]
        else:
            return None


    def checkUser(self, username, password):
        for user in self.__user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())  # Gera um ID de sessão único
                self.__authenticated_users[session_id] = user
                return session_id  # Retorna o ID de sessão para o usuário
        return None


    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id] # Remove o usuário logado

    def user_exists(self, username):
        """Verifica se um usuário já existe no banco de dados."""
        for user in self.__user_accounts:
            if user.username == username:
                return True
        return False

    def register_user(self, username, password):
        if self.user_exists(username):
            return False  # Indica que o usuário já existe
        new_user = UserAccount(username, password)
        self.__user_accounts.append(new_user)
        with open("app/controllers/db/user_accounts.json", "w") as arquivo_json:
            user_data = [vars(user_account) for user_account in self.__user_accounts]
            json.dump(user_data, arquivo_json)
        return True  # Indica que o registro foi bem-sucedido

    def update_user(self, username, new_username, new_password):
        for user in self.__user_accounts:
            if user.username == username:
                user.username = new_username
                user.password = new_password
                self.save()  # Salva as alterações no arquivo JSON
                return True
        return False

    def delete_user(self, username):
        self.__user_accounts = [user for user in self.__user_accounts if user.username != username]
        self.save()

    def save(self):
        with open("app/controllers/db/user_accounts.json", "w") as arquivo_json:
            user_data = [vars(user_account) for user_account in self.__user_accounts]
            json.dump(user_data, arquivo_json)
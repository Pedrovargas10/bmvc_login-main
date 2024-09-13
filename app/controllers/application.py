from app.controllers.datarecord import DataRecord
from bottle import template, redirect, request, response


class Application():

    def __init__(self):

        self.pages = {
            'pagina': self.pagina,
            'portal': self.portal,
            'registro': self.registro,
            'home': self.home
        }
        self.__model= DataRecord()


    def render(self, page, parameter=None):
        content = self.pages.get(page)
        if content is None:
            raise ValueError("Página não encontrada")
        if not parameter:
            return content()
        else:
            return content(parameter)
    
    def home(self):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)  # Assume que você tenha esse método no controller
        return template('app/views/html/home', username=current_user.username if current_user else None)


    def portal(self):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)
        return template('app/views/html/portal', username=current_user.username if current_user else None)


    def pagina(self, username, error_message=None):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)

        if current_user and current_user.username == username:
            return template('app/views/html/pagina', username=current_user.username, error_message=error_message)
        else:
            return redirect('/portal')

    def is_authenticated(self, username):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)
        return current_user and username == current_user.username


    def authenticate_user(self, username, password):
        session_id = self.__model.checkUser(username, password)
        if session_id:
            response.set_cookie('session_id', session_id, httponly=True, \
            secure=True, max_age=3600)
            redirect('/')
        redirect('/portal')


    def logout_user(self):
        session_id = request.get_cookie('session_id')
        self.__model.logout(session_id)
        response.delete_cookie('session_id')
        redirect('/')

    def registro(self):
        return template('app/views/html/registro')
    
    def register_user(self, username, password):
        return self.__model.register_user(username, password)

    def update_user(self, username, new_username, new_password):
        # Verifica se o novo nome de usuário já existe no sistema
        if new_username != username and self.__model.checkUserExists(new_username):
            return "Este nome de usuário já existe"
    
        # Verifica se o nome de usuário é o mesmo
        if username == new_username:
            return "O nome de usuário não pode ser igual ao anterior"
    
        # Tenta atualizar o usuário
        if self.__model.update_user(username, new_username, new_password):
            # Atualiza a sessão para refletir o novo nome de usuário
            session_id = self.__model.checkUser(new_username, new_password if new_password else self.__model.get_password(username))
            response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
            return True
    
        return "Falha ao atualizar o usuário"
    
    def delete_user(self, username, password):
        session_id = request.get_cookie('session_id')
        user = self.__model.getCurrentUser(session_id)
    
        if user and user.username == username and user.password == password:
            self.__model.delete_user(username)
            self.__model.logout(session_id)
            response.delete_cookie('session_id')
            return {'redirect': '/'}
    
        # Se a senha estiver incorreta, retorna uma mensagem de erro
        return {'error_message': "Senha incorreta. Por favor, tente novamente."}



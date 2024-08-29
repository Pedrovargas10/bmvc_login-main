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


    def render(self,page,parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)


    def helper(self):
        return template('app/views/html/helper')
    
    def home(self):
        return template('app/views/html/index')


    def portal(self):
        session_id= request.get_cookie('session_id')
        current_user= self.__model.getCurrentUser(session_id)
        if current_user:
            return template('app/views/html/portal', \
            username= current_user.username)
        return template('app/views/html/portal', \
        username= None)


    def pagina(self,username):
        if self.is_authenticated(username):
            session_id= request.get_cookie('session_id')
            user = self.__model.getCurrentUser(session_id)
            return template('app/views/html/pagina', \
            transfered=True, current_user=user)
        return template('app/views/html/pagina', \
        transfered=False)


    def is_authenticated(self, username):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)
        return username == current_user.username


    def authenticate_user(self, username, password):
        session_id = self.__model.checkUser(username, password)
        if session_id:
            response.set_cookie('session_id', session_id, httponly=True, \
            secure=True, max_age=3600)
            redirect(f'/pagina/{username}')
        redirect('/portal')


    def logout_user(self):
        session_id = request.get_cookie('session_id')
        self.__model.logout(session_id)
        response.delete_cookie('session_id')
        redirect('/portal')

    def registro(self):
        return template('app/views/html/registro')
    
    def register_user(self, username, password):
        return self.__model.register_user(username, password)

    def perfil(self, username):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)
        if current_user and current_user.username == username:
            return template('app/views/html/perfil', user=current_user)
        redirect('/portal')

    def update_user(self, username, new_username, new_password):
        if self.__model.update_user(username, new_username, new_password):
            response.set_cookie('session_id', self.__model.checkUser(new_username, new_password), httponly=True, secure=True, max_age=3600)
            return True
        return False

    def delete_user(self, username):
        self.__model.delete_user(username)
        response.delete_cookie('session_id')
        redirect('/portal')
from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/')
def home():
    return ctl.render('home')

@app.route('/pagina/<username>', methods=['GET'])
def action_pagina(username=None):
    return ctl.render('pagina',username)


@app.route('/portal', method='GET')
def login():
    return ctl.render('portal')


@app.route('/portal', method='POST')
def action_portal():
    username = request.forms.get('username')
    password = request.forms.get('password')
    ctl.authenticate_user(username, password)


@app.route('/logout', method='POST')
def logout():
    ctl.logout_user()

# Rota para a página de cadastro (GET)
@app.route('/registro', method='GET')
def register():
    return ctl.render('registro')

# Rota para processar o formulário de cadastro (POST)
@app.route('/registro', method='POST')
def action_register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if ctl.register_user(username, password):
        return redirect('/portal')  # Redireciona para a página de login após o cadastro
    else:
        return "Este usuário já existe"
    
@app.route('/pagina/<username>/update-username', method='GET')
def update_username_page(username):
    return template('app/views/html/update-username', username=username, error_message="")


@app.route('/pagina/<username>/update-username', method='POST')
def update_username(username):
    new_username = request.forms.get('new_username')
    current_password = request.forms.get('current_password')
    
    # Chame o controlador para atualizar o nome de usuário
    result = ctl.update_username(username, new_username, current_password)
    
    if 'redirect' in result:
        return redirect(result['redirect'])
    if 'error_message' in result:
        return template('app/views/html/update-username', username=username, error_message=result['error_message'])

@app.route('/pagina/<username>/update-password', method='GET')
def update_password_page(username):
    return template('app/views/html/update-password', username=username, error_message="")

@app.route('/pagina/<username>/update-password', method='POST')
def update_password(username):
    current_password = request.forms.get('current_password')
    new_password = request.forms.get('new_password')
    confirm_password = request.forms.get('confirm_password')

    # Verifica se a nova senha e a confirmação são iguais
    if new_password != confirm_password:
        return template('app/views/html/update-password', username=username, error_message="As senhas não conferem.")

    # Chame o controlador para atualizar a senha do usuário
    result = ctl.update_password(username, current_password, new_password)

    if 'redirect' in result:
        return redirect(result['redirect'])
    if 'error_message' in result:
        return template('app/views/html/update-password', username=username, error_message=result['error_message'])

@app.route('/pagina/<username>/delete', method='POST')
def delete_profile(username):
    password = request.forms.get('password')  # Obtém a senha do formulário

    # Chama o método no controller para excluir a conta
    result = ctl.delete_user(username, password)
    
    if 'redirect' in result:
        return redirect(result['redirect'])
    
    if 'error_message' in result:
        return template('app/views/html/pagina', username=username, error_message=result['error_message'])


#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='localhost', port=8080, debug=True)

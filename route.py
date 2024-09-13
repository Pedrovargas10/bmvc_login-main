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

@app.route('/pagina/<username>/update', method='POST')
def update_profile(username):
    new_username = request.forms.get('new_username')
    new_password = request.forms.get('new_password')
    
    # Chama a função de atualização e armazena o resultado
    result = ctl.update_user(username, new_username, new_password)
    
    # Verifica se o resultado é uma mensagem de erro
    if isinstance(result, str):
        # Passa a mensagem de erro para o template
        return template('app/views/html/pagina', username=username, error_message=result)
    else:
        # Atualiza o nome de usuário com sucesso e redireciona
        return redirect(f'/pagina/{new_username}')
    
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

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

@app.route('/helper')
def helper():
    return ctl.render('helper')

#-----------------------------------------------------------------------------
# Suas rotas aqui:

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
        return "Usuário já existe. Por favor, escolha outro nome de usuário."



#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='localhost', port=8080, debug=True)

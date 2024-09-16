<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel de Administração</title>
    <link rel="stylesheet" href="/static/css/superuser.css">
</head>
<body>
    <div class="container">
        <h2>Painel de Administração</h2>

        <!-- Lista de usuários -->
        <table>
            <thead>
                <tr>
                    <th>Nome de Usuário</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                % for user in users:
                <tr>
                    <td>{{ user.username }}</td>
                    <td>
                        <form action="/admin/delete/{{ user.username }}" method="POST">
                            <button type="submit" class="btn-action">Excluir</button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>

        <!-- Formulário para criar novo usuário -->
        <h3>Criar Novo Usuário</h3>
        <form action="/admin/create" method="POST">
            <input type="text" name="username" placeholder="Nome de Usuário" required>
            <input type="password" name="password" placeholder="Senha" required>
            <button type="submit" class="btn-action">Criar Usuário</button>
        </form>

        <!-- Formulário para atualizar nome de usuário -->
        <h3>Atualizar Nome de Usuário</h3>
        <form action="/admin/update-username" method="POST">
            <input type="text" name="current_username" placeholder="Nome de Usuário Atual" required>
            <input type="text" name="new_username" placeholder="Novo Nome de Usuário" required>
            <button type="submit" class="btn-action">Atualizar Nome</button>
        </form>

        <!-- Formulário para atualizar senha -->
        <h3>Atualizar Senha</h3>
        <form action="/admin/update-password" method="POST">
            <input type="text" name="username" placeholder="Nome de Usuário" required>
            <input type="password" name="new_password" placeholder="Nova Senha" required>
            <button type="submit" class="btn-action">Atualizar Senha</button>
        </form>

        <!-- Botão de Logout -->
        <h3>Logout</h3>
        <form action="/logout" method="POST">
            <button type="submit" class="btn-action">Sair</button>
        </form>

        <!-- Botão para Voltar à Página Inicial -->
        <h3>Voltar à Página Inicial</h3>
        <form action="/" method="GET">
            <button type="submit" class="btn-action">Voltar</button>
        </form>
    </div>
</body>
</html>

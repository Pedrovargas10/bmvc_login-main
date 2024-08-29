<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perfil do Usuário</title>
</head>
<body>
    <h1>Perfil de {{user.username}}</h1>
    <form action="/perfil/{{user.username}}" method="POST">
        <label for="new_username">Novo Nome de Usuário:</label>
        <input type="text" name="new_username" value="{{user.username}}" required><br>

        <label for="new_password">Nova Senha:</label>
        <input type="password" name="new_password" value="{{user.password}}" required><br>

        <button type="submit">Atualizar</button>
    </form>

    <form action="/perfil/{{user.username}}/delete" method="POST">
        <button type="submit" style="color:red;">Excluir Conta</button>s
    </form>
</body>
</html>

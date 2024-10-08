<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    % if username:
        <h4>Usuário logado: {{ username }} </h4>
    % end
    <form action="/portal" method="post">
        <label for="username">Nome:</label>
        <input id="username" name="username" type="text" required /><br>

        <label for="password">Senha:</label>
        <input id="password" name="password" type="password" required /><br>

        <input value="Login" type="submit" />
    </form>
    <form action="/logout" method="post">
        <button type="submit">Logout</button>
    </form>
    <a href="/registro">
        <button type="button">Cadastre-se</button>
    </a>
</body>
</html>

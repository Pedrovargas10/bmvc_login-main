<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alterar Nome de Usuário</title>
    <link rel="stylesheet" href="/static/css/update-username.css"> <!-- Link para o arquivo de estilo externo -->
</head>
<body>
    <div class="container">
        <h2>Alterar Nome de Usuário para {{ username }}</h2>
        <form action="/pagina/{{ username }}/update-username" method="POST">
            <div class="form-group">
                <label for="new_username">Novo Nome de Usuário:</label>
                <input type="text" id="new_username" name="new_username" required placeholder="Digite o novo nome de usuário">
            </div>
            <div class="form-group">
                <label for="current_password">Senha Atual:</label>
                <input type="password" id="current_password" name="current_password" required placeholder="Digite sua senha atual">
            </div>
            <button type="submit" class="btn-save">Salvar Alterações</button>
            % if error_message:
            <div class="error-message" id="error-message-container">
                    <p>{{ error_message }}</p>
            </div>
            % end
        </form>

        <!-- Link para voltar à página do perfil -->
        <a href="/pagina/{{ username }}" class="btn-back">Voltar ao Perfil</a>
    </div>

    <script src="/static/js/error-handler.js"></script> <!-- Validação de erro -->
</body>
</html>
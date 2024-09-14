<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Perfil</title>
    <link rel="stylesheet" href="/static/css/pagina.css"> <!-- Link para o arquivo de estilo -->
</head>
<body>
    <div class="container">
        <h2>Bem-vindo, {{ username }}</h2>
        
        <!-- Seção de opções para o usuário -->
        <div class="user-options">
            <!-- Botão para alterar nome de usuário -->
            <form action="/pagina/{{ username }}/update-username" method="GET">
                <button type="submit" class="btn-option">Alterar Nome de Usuário</button>
            </form>

            <!-- Botão para alterar senha -->
            <form action="/pagina/{{ username }}/update-password" method="GET">
                <button type="submit" class="btn-option">Alterar Senha</button>
            </form>

            <!-- Botão para excluir conta -->
            <form action="/pagina/{{ username }}/delete" method="POST" onsubmit="return confirm('Tem certeza que deseja excluir sua conta? Esta ação não pode ser desfeita.')">
                <button type="submit" class="btn-delete">Excluir Conta</button>
            </form>

            <!-- Botão para logout -->
            <form action="/logout" method="POST">
                <button type="submit" class="btn-logout">Logout</button>
            </form>
        </div>

        <!-- Mensagem de erro (se houver) -->
        % if error_message:
        <div class="error-message" id="error-message-container">
            <p>{{ error_message }}</p>
        </div>
        % end

        <!-- Link para voltar à página inicial -->
        <a href="/" class="btn-back">Voltar à Página Inicial</a>
    </div>

    <script src="/static/js/error-handler.js"></script> <!-- Validação de erro -->
</body>
</html>

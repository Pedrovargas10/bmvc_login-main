<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alterar Senha</title>
    <link rel="stylesheet" href="/static/css/update-password.css">
</head>
<body>
    <div class="container">
        <h2>Alterar Senha</h2>
        <form action="/pagina/{{ username }}/update-password" method="POST" class="form-update">
            
            <!-- Campo para senha atual -->
            <div class="form-group">
                <label for="current_password">Senha Atual:</label>
                <input type="password" id="current_password" name="current_password" required placeholder="Digite sua senha atual">
            </div>

            <!-- Campo para nova senha -->
            <div class="form-group">
                <label for="new_password">Nova Senha:</label>
                <input type="password" id="new_password" name="new_password" required placeholder="Digite a nova senha">
            </div>

            <!-- Campo para confirmação da nova senha -->
            <div class="form-group">
                <label for="confirm_password">Confirme a Nova Senha:</label>
                <input type="password" id="confirm_password" name="confirm_password" required placeholder="Confirme a nova senha">
            </div>

            <!-- Botão para salvar as alterações -->
            <button type="submit" class="btn-save">Salvar Alterações</button>

            <!-- Mensagem de erro (se houver) -->
            % if error_message:
            <div class="error-message" id="error-message-container">
                <p>{{ error_message }}</p>
            </div>
            % end
        </form>

        <!-- Link para voltar à página inicial -->
        <a href="/pagina/{{ username }}" class="btn-back">Voltar à Página Inicial</a>
    </div>

    <script src="/static/js/error-handler.js"></script> <!-- Validação de erro -->
</body>
</html>

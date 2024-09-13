<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Página do Usuário</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      padding: 20px;
      text-align: center;
    }

    .container {
      max-width: 600px;
      margin: 0 auto;
      background-color: white;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    h2 {
      text-align: center;
    }

    form {
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
      text-align: center;
      align-items: center;
    }

    label {
      margin-bottom: 5px;
    }

    input {
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
      width: 100%;
      max-width: 400px;
      box-sizing: border-box;
    }

    button {
      padding: 10px;
      background-color: #28a745;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      width: 200px;
      margin: 10px 0;
    }

    button.delete {
      background-color: #dc3545;
    }

    button:hover {
      opacity: 0.9;
    }

    .form-group {
      margin-top: 20px;
    }

    .form-group label,
    .form-group input {
      width: 100%;
      text-align: center;
    }

    /* Adicione estilos para a mensagem de erro */
    .error-message {
      color: red;
      margin: 10px 0;
    }
  </style>
</head>
<body>

<div class="container">
  <h2>Bem-vindo, {{ username }}</h2>

  <!-- Contêiner da mensagem de erro -->
  % if error_message:
    <div class="error-message">
      {{ error_message }}
    </div>
  % end

  <!-- Contêiner dos botões -->
  <div class="button-container">
    <!-- Botão para alterar informações -->
    <button id="alterar-info-btn" class="btn">Alterar Informações</button>

    <!-- Botão para excluir conta -->
    <button id="excluir-conta-btn" class="btn delete">Excluir Conta</button>
  </div>

  <!-- Formulário de alteração (inicialmente oculto) -->
  <div id="form-alterar-info" style="display: none; margin-top: 10px;">
    <form action="/pagina/{{ username }}/update" method="POST">
      <label for="new_username">Novo nome de usuário:</label>
      <input type="text" id="new_username" name="new_username" placeholder="Novo nome de usuário">
      
      <label for="new_password">Nova senha:</label>
      <input type="password" id="new_password" name="new_password" placeholder="Nova senha">
      
      <button type="submit" class="btn">Salvar Alterações</button>
    </form>
  </div>

  <!-- Formulário de confirmação de exclusão de conta (inicialmente oculto) -->
  <div id="form-excluir-conta" style="display: none; margin-top: 10px;">
    <form id="delete-form" action="/pagina/{{ username }}/delete" method="POST">
      <input type="password" id="password" name="password" placeholder="Digite sua senha para confirmar">
      <button type="submit" class="btn delete">Confirmar Exclusão</button>
    </form>
  </div>

  <!-- Scripts -->
  <script src="/static/js/error-handler.js"></script>
  <script src="/static/js/alterar_info.js"></script>
  <script src="/static/js/account-actions.js"></script>
</div>

</body>
</html>

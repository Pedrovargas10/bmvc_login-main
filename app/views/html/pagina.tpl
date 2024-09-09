<!DOCTYPE html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>pagina de Usuário</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      padding: 20px;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      background-color: white;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h2 {
      text-align: center;
    }
    form {
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
    }
    label {
      margin-bottom: 5px;
    }
    input {
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      padding: 10px;
      background-color: #28a745;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button.delete {
      background-color: #dc3545;
    }
    button:hover {
      opacity: 0.9;
    }
  </style>
</head>
<body>

<div class="container">
  <h2>Bem-vindo, {{ username }}</h2>

    % if error_message:
      <p style="color: red;">{{ error_message }}</p>
    % end

  <!-- Formulário para atualizar informações -->
  <form action="/pagina/{{username}}/update" method="POST">
    <label for="new_username">Novo nome de usuário:</label>
    <input type="text" id="new_username" name="new_username" value="{{username}}" required>

    <label for="new_password">Nova senha:</label>
    <input type="password" id="new_password" name="new_password" placeholder="Digite sua nova senha" required>

    <button type="submit">Atualizar Informações</button>
  </form>

  <!-- Formulário para excluir conta -->
  <form action="/pagina/{{username}}/delete" method="POST">
    <button type="submit" class="delete" onclick="return confirm('Tem certeza que deseja excluir sua conta?')">Excluir Conta</button>
  </form>
</div>

</body>
</html>
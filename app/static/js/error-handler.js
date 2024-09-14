document.getElementById('delete-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Evita o envio automático do formulário

  const password = document.getElementById('password').value;
  const username = '{{ username }}';

  fetch(`/pagina/${username}/delete`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `password=${encodeURIComponent(password)}`
  })
  .then(response => response.json())
  .then(data => {
      if (data.error_message) {
          // Exibe a mensagem de erro na página sem redirecionar
          document.getElementById('error-message-container').textContent = data.error_message;
          document.getElementById('error-message-container').style.display = 'block';
      } else if (data.redirect) {
          // Redireciona se a conta for excluída
          window.location.href = data.redirect;
      }
  })
  .catch(error => {
      console.error('Erro ao excluir conta:', error);
  });
});
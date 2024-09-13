document.addEventListener('DOMContentLoaded', () => {
    const errorMessageContainer = document.getElementById('error-message-container');
    const errorMessage = errorMessageContainer ? errorMessageContainer.textContent.trim() : '';
  
    if (errorMessage) {
      // Exibe a mensagem de erro
      errorMessageContainer.style.display = 'block'; // Garante que a mensagem de erro seja exibida
      // Pode-se usar um alert ou outra forma de notificação, se desejado
    }
  });
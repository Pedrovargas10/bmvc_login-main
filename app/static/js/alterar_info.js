// alterar_info.js

document.addEventListener('DOMContentLoaded', function () {
    // Seleciona o botão e o formulário de alteração
    const alterarInfoBtn = document.getElementById('alterar-info-btn');
    const formAlterarInfo = document.getElementById('form-alterar-info');
  
    // Adiciona um evento de clique ao botão
    alterarInfoBtn.addEventListener('click', function () {
      // Alterna a exibição do formulário
      if (formAlterarInfo.style.display === 'none' || formAlterarInfo.style.display === '') {
        formAlterarInfo.style.display = 'block';
        alterarInfoBtn.textContent = 'Ocultar Alterações'; // Muda o texto do botão para "Ocultar Alterações"
      } else {
        formAlterarInfo.style.display = 'none';
        alterarInfoBtn.textContent = 'Alterar Informações'; // Muda o texto do botão para "Alterar Informações"
      }
    });
  });
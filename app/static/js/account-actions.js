document.addEventListener("DOMContentLoaded", function() {
    // Seleciona os botões e formulários
    var alterarInfoBtn = document.getElementById('alterar-info-btn');
    var formSelecao = document.getElementById('form-selecao');

    var alterarUsernameBtn = document.getElementById('alterar-username-btn');
    var formAlterarUsername = document.getElementById('form-alterar-username');

    var alterarSenhaBtn = document.getElementById('alterar-senha-btn');
    var formAlterarSenha = document.getElementById('form-alterar-senha');

    // Função para exibir/ocultar o formulário de seleção
    if (alterarInfoBtn && formSelecao) {
        alterarInfoBtn.addEventListener('click', function() {
            formSelecao.style.display = (formSelecao.style.display === "none") ? "block" : "none";
        });
    }

    // Função para exibir/ocultar o formulário de alterar nome de usuário
    if (alterarUsernameBtn && formAlterarUsername) {
        alterarUsernameBtn.addEventListener('click', function() {
            formAlterarUsername.style.display = (formAlterarUsername.style.display === "none") ? "block" : "none";
        });
    }

    // Função para exibir/ocultar o formulário de alterar senha
    if (alterarSenhaBtn && formAlterarSenha) {
        alterarSenhaBtn.addEventListener('click', function() {
            formAlterarSenha.style.display = (formAlterarSenha.style.display === "none") ? "block" : "none";
        });
    }
});

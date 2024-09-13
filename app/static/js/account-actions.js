// Função para exibir ou ocultar o formulário de alteração de informações
document.addEventListener("DOMContentLoaded", function() {
    var alterarInfoBtn = document.getElementById('alterar-info-btn');
    var formAlterarInfo = document.getElementById('form-alterar-info');

    if (alterarInfoBtn && formAlterarInfo) {
        alterarInfoBtn.addEventListener('click', function() {
            if (formAlterarInfo.style.display === "none") {
                formAlterarInfo.style.display = "block";
            } else {
                formAlterarInfo.style.display = "none";
            }
        });
    }

    // Função para exibir/ocultar o campo de confirmação de senha
    var excluirContaBtn = document.getElementById('excluir-conta-btn');
    var formExcluirConta = document.getElementById('form-excluir-conta');

    if (excluirContaBtn && formExcluirConta) {
        excluirContaBtn.addEventListener('click', function() {
            if (formExcluirConta.style.display === "none") {
                formExcluirConta.style.display = "block";
            } else {
                formExcluirConta.style.display = "none";
            }
        });
    }
});

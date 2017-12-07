$(document).ready(function() {
    $("#buscar").click(function(event) {

        var inputUser = document.getElementById("user");
        var inputId_perm = document.getElementById("id_perm");
        var divListaErros = document.getElementById("lista-erros");

        //limpa elemento
        divListaErros.innerHTML = " ";

        var listaDeErros = retornaListaDeErros(inputUser,inputId_perm);

        if (montaListaDeErrosNaInterface(listaDeErros)){
            //se montar a lista intenrrompe a execução!
            return;
        };

        var loading =
            '<h4>Pesquisa em andamento, por favor aguarde ...</h4><div class="progress"><div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div></div>'

        document.getElementById("resposta").classList.add('conteudo-pdm');

        $('#resposta').html(loading);

        $.ajax({
            type: "POST",
            url: "resultado/",
            data: {
                'user': $('#user').val().trim(),
                'id_perm': $('#id_perm').val().trim()
            },
            success: function(result) {
                $('#resposta').html(result)
            },
            error: function(xhr) {
                $('#resposta').html(xhr);
                alert("Ocorreu um erro!\nContate o Suporte " + " " + xhr.statusText);

            }
        });
        return false;
    });
});

//internal function

function retornaListaDeErros(user, idperm) {
    var errorMessages = [];

    if (user.value == ' ' || user.value == '') {
        errorMessages.push(" O campo user não pode ser vazio.");
    }

    idPermPatter = /\d+#perm\!.*\S/ ;
    if (!idPermPatter.test(idperm.value)) {
        errorMessages.push(" Informe um id_perm válido!");
    }

    notUserPattern = /^.*?@.*?\./ ;
    if (notUserPattern.test(user.value)) {
        errorMessages.push(": Não é necessario @dominio!");
    }

    return errorMessages;
}

function montaListaDeErrosNaInterface(listaDeErros) {

    var divListaErros = document.getElementById("lista-erros");
    //limpa elemento
    divListaErros.innerHTML = " ";

    if (listaDeErros.length > 0) {

        //adiciona classes bootstrap para o elemento
        divListaErros.classList.add("alert");
        divListaErros.classList.add("alert-danger");
        divListaErros.setAttribute("role","alert");

        //inicia a lista
        var ul = document.createElement("ul");
        divListaErros.appendChild(ul);

        listaDeErros.forEach(function (erro) {

            var li = document.createElement("li");
            li.textContent = erro;
            ul.appendChild(li);
        });
        return true;
    }

    var divListaErros = document.getElementById("lista-erros");
    //limpa elemento
    divListaErros.innerHTML = " ";
    divListaErros.classList.remove("alert");
    divListaErros.classList.remove("alert-danger");
    divListaErros.setAttribute("role","");

    return false;

}

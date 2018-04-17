$(document).ready(function() {
    //Aqui só guardei os eventos principais
    $("#btn-add").click(function(event) {

        var inputFile = document.querySelector("#input-new-file");
        var listaDeArquivos = document.querySelector("#lista-de-arquivos");

        //Aqui usamos a validação no lugar do false fixado!
        if (!validaCampoArquivo(inputFile)) {
            // return nothing to abort...
            return ;
        }

        // funcao que insere arquivo na lista
        insereArquivoNaLista(inputFile, listaDeArquivos);

        // Adiciona o evento de remover linhas quando o arquivo for para lista
        adicionaEventoRemovePorItem();

        //limpa o campo depois de inserir
        limpaCampoDoArquivo(inputFile);

    });

    $("#btn-limpa-lista").click(function(event) {
        event.preventDefault();
        if (window.confirm("Deseja limpar a lista de arquivos?")){
            $(".arquivo-na-lista").remove();
        }
    });

});



// Subtasks
function insereArquivoNaLista(arquivo, lista) {

    var file = arquivo.value.trim();
    var status = "Pronto para atualizar";
    var action = "Remover";

    var listaTds = [];
    listaTds.push(file);
    listaTds.push(status);
    listaTds.push(action);

    var tr = document.createElement('tr');
    tr.classList.add('arquivo-na-lista');

    listaTds.forEach(function(valor) {
        var td = document.createElement('td');
        td.textContent = valor;
        if (valor == "Remover") {
            td.classList.add("remover-item");
        }
        tr.appendChild(td);
    });
    lista.querySelector("tbody").appendChild(tr);
}

function limpaCampoDoArquivo(campoASerLimpado) {
    campoASerLimpado.value = "";
}

function adicionaEventoRemovePorItem() {
    $(".remover-item").on('click', function(event){
        var linha = this.parentNode;
        console.log(linha);
        linha.classList.add("invisivel");
        setTimeout(function() {
            linha.remove();
        }, 1000);
    });
}

function validaCampoArquivo(campoASerValidado){
    //****implementar****
    //Deve retornar true se estiver validado ou
    //false se não estiver.
    return true;
}

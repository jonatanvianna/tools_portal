//MOdal que exibe detalhes da diretiva que foi clicada
jQuery("tr#id_diretiva").click(function() {
   var d = jQuery(this);
   var diretiva = d[0].dataset;
   var date_closed = ""
   var btn_delete_diretiva = "";
   var btn_close_diretiva = "";
   var btn_edit_diretiva = "";

   if (diretiva.status === "Fechada"){
      date_closed = '<strong>Fechada em: </strong>'+ diretiva.date_closed + '<br/>';
   }

   status = '<h4> Status: <strong>'+ diretiva.status + '</strong></h4>';
   date_entry = '<strong>Data de Abertura: </strong>' + diretiva.date_entry +  '<br/>';
   main_ticket = '<strong>Ticket principal: </strong>' + diretiva.main_ticket + '<br/>';
   product = '<strong>Produto: </strong>[' + diretiva.product.toUpperCase() + '] <br/>';
   description = '<strong>Descrição: </strong>'+ diretiva.description + '<br/>';
   date_update = '<strong>Última atualização em: </strong>'+ diretiva.date_update + '<br/>';
   id = '<input type="hidden" id="id" name="id" value="' + diretiva.id + '">';

   jQuery(".modal-body").html(
      id +
      status +
      date_entry +
      main_ticket +
      product +
      description +
      date_update +
      date_closed
   );


   if ( diretiva.status === 'Aberta' ){
      btn_close_diretiva = '<a href="/diretivas/close/?id='+diretiva.id+'"><button type="submit " id="btn-fechar" class="btn btn-success">Encerrar esta Diretiva</button></a>';
      btn_edit_diretiva = '<a href="/diretivas/update/?id='+diretiva.id+'"><button type="button" id="btn-editar" class="btn btn-warning">Editar</button></a>';
      btn_delete_diretiva = '<a href="/diretivas/delete/?id='+diretiva.id+'"><button type="submit" id="btn-deletar" class="btn btn-danger">Deletar</button></a>';
   }

   jQuery(".modal-footer").html(
      btn_close_diretiva +
      btn_edit_diretiva +
      btn_delete_diretiva
   );
});
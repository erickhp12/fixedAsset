function deleteMain() {
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteMain/" + item + "/",
        success: function (data) {
            $('#modal-borrar').modal('hide');
            location.reload();
            for (i = 0; i < data.length; i++) {
                $('ul').append('<li>' + data[i] + '</li>');
            }
        }
    });
}

function deleteMarca() {
    item = document.getElementById('idBorrar').innerHTML;
    $.ajax({
        type: "GET",
        url: "/deleteMarca/" + item + "/",
        success: function (data) {
            $('#modal-borrar').modal('hide');
            location.reload();
            for (i = 0; i < data.length; i++) {
                $('ul').append('<li>' + data[i] + '</li>');
            }
        }
    });
}
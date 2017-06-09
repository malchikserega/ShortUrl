/**
 * Created by Sergey on 08.06.17.
 */
$(function () {
    $('#shurl').click(function () {
        var url = $('#url').val();
        $.ajax({
            type: 'POST',
            url: '/shturl',
            data: {'url': url},
            success: function (response) {
                $('#shorturl').removeAttr('hidden')
                $('#readyurl').attr("href", response);
                $('#readyurl').text('http://127.0.0.1:5000/' + response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
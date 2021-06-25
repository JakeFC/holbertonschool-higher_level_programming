$(document).ready(function () {
  const code = $('#language_code');
  code.keypress(function (e) {
    if (e.which === 13) {
      $.ajax({
        type: 'GET',
        url: ('https://fourtonfish.com/hellosalut/?lang=' + code.val()),
        success: function (data) {
          $('#hello').html(data.hello);
        }
      });
    }
  });
  $('#btn_translate').click(function () {
    $.ajax({
      type: 'GET',
      url: ('https://fourtonfish.com/hellosalut/?lang=' + code.val()),
      success: function (data) {
        $('#hello').html(data.hello);
      }
    });
  });
});

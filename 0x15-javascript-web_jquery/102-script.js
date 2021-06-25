// fetches and prints how to say “Hello” depending on the language, using this
// API service: https://www.fourtonfish.com/hellosalut/hello/ whenever the user
// clicks #btn_translate
$(document).ready(function () {
  const code = $('#language_code');
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

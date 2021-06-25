// fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays
// the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=en',
    success: function (data) {
      $('#hello').html(data.hello);
    }
  });
});

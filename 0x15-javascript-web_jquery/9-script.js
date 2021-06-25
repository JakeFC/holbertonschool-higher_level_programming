$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=en',
    success: function (data) {
      $('#hello').html(data.hello);
    }
  });
});

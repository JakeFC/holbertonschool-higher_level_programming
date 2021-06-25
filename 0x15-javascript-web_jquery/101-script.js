$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
$(document).ready(function () {
  $('#remove_item').click(function () {
    $('ul.my_list li').last().remove();
  });
});
$(document).ready(function () {
  $('#clear_list').click(function () {
    $('ul.my_list li').remove();
  });
});

// fetches and lists the title for all movies by using
// this URL: https://swapi-api.hbtn.io/api/films/?format=json
$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});

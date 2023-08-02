const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(url, function (data, status) {

  function getFilmAndAppend (filmUrl) {
    $.get(filmUrl, function (film) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  }

  $.each(data.films, function (index, filmUrl) {
    getFilmAndAppend(filmUrl);
  });
});

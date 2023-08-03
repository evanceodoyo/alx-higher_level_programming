$(document).ready(function () {
  function fetchTranslation () {
    let url = 'https://www.fourtonfish.com/hellosalut/hello/';
    url = url + '?lang=' + $('INPUT#language_code').val();

    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').on('click', function () {
    fetchTranslation();
  });

  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});

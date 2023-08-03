$(document).ready(function () {
  let url = 'https://www.fourtonfish.com/hellosalut/hello/';
  url = url + '?lang=' + $('INPUT#language_code').val();

  $('INPUT#btn_translate').on('click', function () {
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});

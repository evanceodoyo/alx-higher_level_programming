const url = ' https://fourtonfish.com/hellosalut/?lang=fr'; /* No longer accessible, blocks Cross-Origin Request */

$.get(url, function (data, status) {
  $('DIV#hello').text(data.hello);
});

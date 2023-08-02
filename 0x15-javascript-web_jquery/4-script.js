$('DIV#toggle_header').on('click', function () {
  if ($(this).hasClass('red')) {
    $(this).removeClass('red');
    $(this).addClass('green');
  } else if ($(this).hasClass('green')) {
    $(this).removeClass('green');
    $(this).addClass('red');
  } else {
    $(this).addClass('green');
  }
});

$(document).ready(function () {
/* Add item to the list. */
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  /* Remove item from the list. */
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last').remove();
  });

  /* Removes all list elements. */
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});

$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
    $.ajax({
      url,
      headers: {
        'Access-Control-Allow-Origin': '*'
      },
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});

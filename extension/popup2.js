$(document).ready(function() {
  $('#CanLII').click(function() {
    let case = $('#caseid').val();
    $('#caseid').val("");
    $.ajax({
      url: `https://www.canlii.org/en/ca/scc/doc/2001/2001scc2/2001scc2.html&appid=[2001scc2]`,
      type: 'GET',
      data: {
        format: 'json'
      },
      success: function(response) {
        $ //CHRIS'S CODE//
      },
      error: function() {
        $('#errors').text("There was an error processing your request. Please try again.")
      }
    });
  });
});
$(function() {
  var showSuggestion = function() {
    var title = $('#suggestion-title');
    var body = $('#suggestion-body');
    switch ($(this).data("symbol")) {
      case "AR":
        title.html("Incorrect article usage");
        body.html("We use <em>a</em> or <em>an</em> when a noun is new or unknown. We use <em>a</em>" +
          "before words that begin with a consonant sound (a carrot) and <em>an</em>" +
          "before words that begin with a vowel sound (an orange, an hour).");
        break;
      case "SP":
        title.html("Incorrect spelling");
        var word = $(this).data("selection");
        body.html("We could not find the word <em>" + word + "</em> in our dictionary.");
        break;
      case "C":
        title.html("Incorrect capitalization");
        var text = "A capitalized word is one beginning with an upper case letter. We capitalize words in the following situations:";
        text += "<ul>";
        text += "<li>Beginning of a sentence</li>";
        text += "<li>Proper nouns</li>";
        text += "<li>The pronoun <em>I</em></li>";
        text += "<li>Names of months and days of the week</li>";
        text += "<li>Name of countries and languages</li>";
        body.html(text);
        break;
      default:
        // Do not show explanation box
        return;
    }
    $("#user-view .suggestion").show();
  };

  var hideSuggestion = function() {
    $("#user-view .suggestion").hide();
  };

  var displayCorrections = function(text, response) {
    $('#user-entry').hide();
    $('#user-view').show();

    var changes = response.changes;
    var analysis = response.analysis;

    if (analysis) {
        $(".precision").html(analysis.precision);
        $(".recall").html(analysis.recall);
    } else {
        $(".precision").html("");
        $(".recall").html("");
    }

    // sort in descending order, so added <span>s don't mess up the offset.
    changes.sort(function(a, b) {
      return b.start - a.start;
    });
    for (var i = 0; i < changes.length; i++) {
      var start = changes[i].start;
      var end = start + changes[i].selection.length;

      var prev = text.slice(0, start);
      var after = text.slice(end, text.length);

      var span = '<mark data-symbol="' + changes[i].symbol + '" ';
      span += '         data-selection="' + changes[i].selection + '">';
      text = prev + span + changes[i].selection + "</mark>" + after;
    }

    $("#user-view .text").html(text);

    $('#user-view mark').hover(showSuggestion, hideSuggestion);
  };

  $('#user-view .btn').on('click', function() {
    $('#user-entry button').prop('disabled', false);
    $('#user-view').hide();
    $('#user-entry').show();
  });

  $('#user-entry .btn-primary').on('click', function() {
    var text = $('#user-entry textarea').val();
    var id = $('#id').val();
    var algo = $("#algorithm option:selected").val();

    // disable button before sending
    $('#user-entry button').prop('disabled', true);
    // send text to API
    $.ajax({
        url: "/predict",
        method: "POST",
        data: JSON.stringify({text: text, id: id, algorithm: algo}),
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    }).done(function(response) {
        displayCorrections(text, response);
    });
  });

  $('#example').on('click', function() {
    $.ajax({
        url: "/essays?random=1",
        dataType: "json"
    }).done(function(json) {
        $('#id').val(json.id);
        $('#text-entry').html(json.text);
    });
  });
});

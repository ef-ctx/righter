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
    }
    $("#user-view .suggestion").show();
  };

  var hideSuggestion = function() {
    $("#user-view .suggestion").hide();
  };

  var displayCorrections = function(resp) {
    $('#user-entry').hide();
    $('#user-view').show();

    var item = resp.item;
    var analysis = resp.analysis;

    if (analysis) {
        $(".precision").html(analysis.precision);
        $(".recall").html(analysis.recall);
    } else {
        $(".precision").html("");
        $(".recall").html("");
    }

    // sort in descending order, so added <span>s don't mess up the offset.
    item.changes.sort(function(a, b) {
      return b.start - a.start;
    });
    var text = item.text;
    for (var i = 0; i < item.changes.length; i++) {
      var start = item.changes[i].start;
      var end = start + item.changes[i].selection.length;

      var prev = text.slice(0, start);
      var after = text.slice(end, text.length);

      var span = '<mark data-symbol="' + item.changes[i].symbol + '" ';
      span += '         data-selection="' + item.changes[i].selection + '">';
      text = prev + span + item.changes[i].selection + "</mark>" + after;
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
        url: "http://localhost:8000/corr",
        data: {text: text, id: id, algorithm: algo},
        dataType: "json"
    }).done(displayCorrections);
  });

  $('#example').on('click', function() {
    $.ajax({
        url: "http://localhost:8000/example",
        dataType: "json"
    }).done(function(json) {
        $('#id').val(json.id);
        $('#text-entry').html(json.text);
    });
  });
});

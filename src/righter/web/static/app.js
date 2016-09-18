$(function() {
  var showSuggestion = function() {
    var title = $('#suggestion-title');
    var body = $('#suggestion-body');
    var selection = decodeURIComponent($(this).data("selection"));
    var algo = $(this).data("algo");
    var explanation = decodeURIComponent($(this).data("explanation"));
    var suggestions = decodeURIComponent($(this).data("suggestions")).split("///").filter(function(e) {return e != ""});
    var righterText;
    switch (decodeURIComponent($(this).data("symbol"))) {
      case "AR":
        title.html("Incorrect article usage");
        righterText = "We use <em>a</em> or <em>an</em> when a noun is new or unknown. We use <em>a</em>";
        righterText += "before words that begin with a consonant sound (a carrot) and <em>an</em>";
        righterText += "before words that begin with a vowel sound (an orange, an hour).";
        break;
      case "SP":
        title.html("Incorrect spelling");
        righterText = "We could not find the word <em>" + selection + "</em> in our dictionary.";
        break;
      case "C":
        title.html("Incorrect capitalization");
        righterText = "A capitalized word is one beginning with an upper case letter. We capitalize words in the following situations:";
        righterText += "<ul>";
        righterText += "<li>Beginning of a sentence</li>";
        righterText += "<li>Proper nouns</li>";
        righterText += "<li>The pronoun <em>I</em></li>";
        righterText += "<li>Names of months and days of the week</li>";
        righterText += "<li>Name of countries and languages</li>";
        break;
      default:
        title.html("Incorrect");
        break;
    }
    var text = "";
    if (explanation) {
      text += "<p>" + explanation + "</p>";
    }
    if (suggestions.length > 0) {
      text += "<p>Suggestions:</p>";
      text += "<ul>";
      for (var i = 0; i < suggestions.length; i++) {
        text += "<li>" + suggestions[i] + "</li>";
      }
      text += "</ul>";
    }

    if (algo == 'righter') {
      body.html(righterText);
    } else {
      body.html(text);
    }
    $("#user-view .suggestion").show();
  };

  var hideSuggestion = function() {
    $("#user-view .suggestion").hide();
  };

  var displayCorrections = function(algo, text, response) {
    $('#user-entry').hide();
    $('#user-view').show();

    var analysis = response.analysis;

    if (analysis) {
        $(".precision").html(analysis.precision);
        $(".recall").html(analysis.recall);
    } else {
        $(".precision").html("");
        $(".recall").html("");
    }

    // sort in descending order, so added <span>s don't mess up the offset.
    var changes = []
    response.changes.sort(function(a, b) {
      return b.start - a.start;
    });
    if (response.changes.length > 1) {
      for (var i = 0; i < response.changes.length-1; i++) {
        var end = response.changes[i+1].start + response.changes[i+1].selection.length;
        if (response.changes[i].start > end) {
          changes.push(response.changes[i]);
        }
      }
      changes.push(response.changes[response.changes.length-1]);
    } else {
      changes = response.changes;
    }

    for (var i = 0; i < changes.length; i++) {
      var start = changes[i].start;
      var end = start + changes[i].selection.length;

      var prev = text.slice(0, start);
      var after = text.slice(end, text.length);

      var symbol = changes[i].symbol || "";
      var selection = changes[i].selection || "";
      var explanation = changes[i].explanation || "";
      var suggestions = changes[i].suggestions || [];
      suggestions = suggestions.join("///");
      var span = '<mark data-symbol="' + encodeURIComponent(symbol) + '" ';
      span += '         data-selection="' + encodeURIComponent(selection) + '" ';
      span += '         data-explanation="' + encodeURIComponent(explanation) + '" ';
      span += '         data-suggestions="' + encodeURIComponent(suggestions) + '" ';
      span += '         data-algo="' + algo + '">';
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
    var corrections = $('#corrections option:selected').val();
    var algo = $("#algorithm option:selected").val();

    var ignoreType = false;

    if (corrections == "any") {
      ignoreType = true;
    }

    // disable button before sending
    $('#user-entry button').prop('disabled', true);
    // send text to API
    $.ajax({
        url: "/predict",
        method: "POST",
        data: JSON.stringify({text: text, id: id, algorithm: algo, ignoreType: ignoreType}),
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    }).done(function(response) {
        displayCorrections(algo, text, response);
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

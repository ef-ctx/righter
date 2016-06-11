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

  var displayCorrections = function(item) {
    $('#user-entry').hide();
    $('#user-view').show();

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

      var span = '<div data-symbol="' + item.changes[i].symbol + '" ';
      span += '        data-selection="' + item.changes[i].selection + '" ';
      span += '        class="highlight">';
      text = prev + span + item.changes[i].selection + "</div>" + after;
    }

    $("#user-view .text").html(text);

    $('#user-view .highlight').hover(showSuggestion, hideSuggestion);
  };

  $('#user-view .btn').on('click', function() {
    $('#user-entry button').prop('disabled', false);
    $('#user-view').hide();
    $('#user-entry').show();
  });

  $('#user-entry button').on('click', function() {
    var text = $('#user-entry textarea').val();

    // disable button before sending
    $('#user-entry button').prop('disabled', true);
    // send text to API

    // this will be called from an ajax callback, probably
    displayCorrections({"nationality": "cn", "text": "\n            Dear Julia, I'm very angry because I did most of the chores this week.  I did the ironing and washed dishes on Monday. I washed the dishes and made the beds on Tuseday. I washed the dishes on Wednesday and Friday too. I made dinner, washed the dishes, make the beds and paied the bills on Thursday. I swept the floor, mopped the floor and do the shopping on Saturday. I did the laundry and Vacuumed on Sunday.\n            ", "changes": [{"selection": "Vacuumed", "start": 403, "symbol": "C"}, {"selection": "Tuseday", "start": 173, "symbol": "SP"}, {"selection": "paied", "start": 283, "symbol": "SP"}], "id": "C221982", "level": "4"});
  });
});

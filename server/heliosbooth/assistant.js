window.onload = () => console.log('done');

ASSISTANT = {}

ASSISTANT.random = function (length) {
  return btoa(sjcl.random.randomWords(length)).slice(0, length);
}

ASSISTANT.generateSessionData = function (sessionTitle) {
  localStorage['sessionTitle'] = sessionTitle;
  localStorage['sessionId'] = sessionTitle + ASSISTANT.random(16);
  localStorage['keyRandom'] = ASSISTANT.random(32);
}

ASSISTANT.handleStart = function () {
  const sessionTitle = document.querySelector('input[name="session_title"]').value

  if (sessionTitle == '') {
    alert("Session title cannot be empty");
    return;
  }

  if (sessionTitle.length > 50) {
    alert("Session title cannot be greater than 50");
    return;
  }

  ASSISTANT.generateSessionData(sessionTitle);
  BOOTH.start_election();
}

ASSISTANT.renderQrCode = function () {

  const qrCodeData = JSON.stringify({
    'sessionId': localStorage['sessionId'],
    'sessionTitle': localStorage['sessionTitle'],
  });

  $('#qrcode').qrcode({ width: 256, height: 256, text: qrCodeData });
  $('#session-title').text('sessionTitle: ' + localStorage['sessionTitle']);
  $('#session-id').text('sessionId: ' + localStorage['sessionId']);
}

ASSISTANT.audit_ballot = function () {
  const encryptedRandomness = localStorage["encryptedRandomness"];
  const body = {
    "body": encryptedRandomness
  };
  ASSISTANT.postOnBB(body);
  BOOTH.audit_ballot();
};

ASSISTANT.postOnBB = function (data) {
  const sessionId = localStorage["sessionId"];
  const url = `/helios/fake-booth/${sessionId}/`;
  $.ajax({
    url: url,
    type: 'PUT',
    data: data,
    success: function (response) {
      console.log('SUCCESSFULLY POSTED ON BB');
    }
  });
};

ASSISTANT.cast_ballot = function () {
  const castCode = $('#cast_code').val()

  if (!castCode || castCode.length === 0) {
    alert("Please provide cast code");
    return;
  }

  $('#hidden_cast_code').val(castCode);

  BOOTH.cast_ballot();
}
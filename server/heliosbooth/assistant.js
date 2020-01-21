window.onload = () => console.log('done');

ASSISTANT = {}

ASSISTANT.random = function (length) {
  return btoa(sjcl.random.randomWords(length));
}

ASSISTANT.generateSessionData = function (sessionTitle) {
  localStorage['sessionTitle'] = sessionTitle;
  localStorage['sessionId'] = sessionTitle + ASSISTANT.random(16);
  localStorage['keyRandom'] = ASSISTANT.random(128);
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
}

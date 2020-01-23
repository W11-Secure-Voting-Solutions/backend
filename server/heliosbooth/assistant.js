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

  if (sessionTitle.length === 0) {
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
    'kRand': localStorage['keyRandom'],
  });

  $('#qrcode').qrcode({ width: 256, height: 256, text: qrCodeData });
  $('#session-title').text('sessionTitle: ' + localStorage['sessionTitle']);
  $('#session-id').text('sessionId: ' + localStorage['sessionId']);
}

ASSISTANT.sendPublicKey = function(publicKey) {
  const electionObject = JSON.parse(publicKey);
  const publicKeyString = JSON.stringify(electionObject.public_key);
  const data = {
    'publicKey': publicKeyString
  }
  ASSISTANT.postOnBB(data);
}

ASSISTANT.audit_ballot = function () {
  BOOTH.audit_trail = BOOTH.encrypted_ballot_with_plaintexts_serialized || $.toJSON(BOOTH.encrypted_ballot.get_audit_trail());
  const auditTrailObject = JSON.parse(BOOTH.audit_trail);
  const randomnesses = auditTrailObject.answers[0].randomness;

  const kRand = localStorage['keyRandom'];
  var encryptedRandomnesses = ASSISTANT.encrypt(randomnesses.toString(), kRand);
  const body = {
    "randomness": encryptedRandomnesses
  };
  ASSISTANT.postOnBB(body);
  BOOTH.show($('#audit_div')).processTemplate({ 'audit_trail': BOOTH.audit_trail, 'election_url': BOOTH.election_url });
};

ASSISTANT.encrypt = function(message, key) {
  var message = CryptoJS.AES.encrypt(message, key).toString();
  return message.toString();

}

ASSISTANT.sendEncryptedChoices = function(encryptedBallot) {
  const encryptedChoicesObject = JSON.parse(encryptedBallot);
  const choices = JSON.stringify(encryptedChoicesObject.answers[0].choices);
  const data = {
    choices
  }
  ASSISTANT.postOnBB(data);
}

ASSISTANT.postOnBB = function(data) {
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
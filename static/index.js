

        function DisableNextButton(disableButton) {
          document.getElementById(disableButton).disabled = 'true';
        };

        function EnableNextButton(enableButton) {
          document.getElementById(enableButton).removeAttribute('disabled');
        };

function UpdateAttendees() {
    const url = '/counter?event_key=' + eventKey;
    const options = {
          method: 'POST',
          credentials: 'same-origin',
        }
    const request = new Request(url, options);
          fetch(request);
        }

const signUpButtons = document.querySelectorAll('.addcount');
const dropOutButtons = document.querySelectorAll('.removecount')
var clicks = 0

signUpButtons.forEach(function(elem)) {
  elem.addEventListener('click', (e)=>
  clicks += number;
  signUpButtons.innerHTML = clicks;
  DisableNextButton(disableButton);
  EnableNextButton(enableButton);
  UpdateAttendees();
)}



dropOutButtons.forEach(function(elem)) {
  elem.addEventListener('click', (e)=>
  clicks -= number;
  dropOutButtons.innerHTML = clicks;
  DisableNextButton(disableButton);
  EnableNextButton(enableButton);
  UpdateAttendees();
)}

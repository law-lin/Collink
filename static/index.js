        signU = document.querySelectorAll('.signUpButton')
        dropU = document.querySelectorAll('.removeButton')



        signU.forEach((signUpButton) => {
          var clicks = 0;
          signUpButton.addEventListener('click', (event) => {

          disableButton = event.target
          parent = disableButton.parentElement
          enableButton = parent.children[2]
          clickElement = parent.children[1].children[0]
          eventKeyElement = parent.children[3]
          onClick(disableButton, enableButton, clicks, clickElement)
          UpdateAttendees(eventKeyElement.value)





  });
});


        dropU.forEach((removeButton) => {

          var clicks = 1;
          removeButton.addEventListener('click', (event) => {

          disableButton = event.target
          parent = enableButton.parentElement
          enableButton = parent.children[0]
          clickElement = parent.children[1].children[0]
          eventKeyElement = parent.children[3]
          onClick2(disableButton, enableButton, clicks, clickElement)
          SubtractAttendees(eventKeyElement.value)



  });
});

        function DisableNextButton(disableButton) {

          disableButton.disabled = 'true';
        };

        function EnableNextButton(enableButton) {
          enableButton.removeAttribute('disabled');
        };

        function UpdateAttendees(eventKey) {
          const url = '/counter?' + 'event_key=' + eventKey
          const options = {
            method:'post',
            credentials:'same-origin',
          }
          const request = new Request(url, options);
          fetch(request);

        }

        function SubtractAttendees(eventKey) {
          const url = '/subtract?' + 'event_key=' + eventKey
          const options =
          {
            method:'post',
            credentials:'same-origin',
          }
          const request = new Request(url, options);
          fetch(request)
        }

        function onClick(disableButton, enableButton, clicks, clickElement) {
            clicks += 1;
            // clickElement.innerHTML = clicks;
            DisableNextButton(disableButton);
            EnableNextButton(enableButton);


        };


        function onClick2(disableButton, enableButton, clicks, clickElement) {
            clicks -= 1;
            // clickElement.innerHTML = clicks;
            DisableNextButton(disableButton);
            EnableNextButton(enableButton);

        };

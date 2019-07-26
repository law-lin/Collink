        signU = document.querySelectorAll('.signUpButton')
        dropU = document.querySelectorAll('.removeButton')


        signU.forEach((signUpButton) => {
          var clicks = 0;
          signUpButton.addEventListener('click', (event) => {

          disableButton = event.target
          parent = disableButton.parentElement
          enableButton = parent.children[2]
          clickElement = parent.children[1].children[0]
          onClick(disableButton, enableButton, clicks, clickElement)



  });
});


signU.forEach((removeButton) => {
  var clicks = 0;
  removeButton.addEventListener('click', (event) => {

  disableButton = event.target
  parent = enableButton.parentElement
  enableButton = parent.children[2]
  clickElement = parent.children[1].children[0]
  onClick2(enableButton, disableButton, clicks, clickElement)



});
});

        function DisableNextButton(disableButton) {

          disableButton.disabled = 'true';
        };

        function EnableNextButton(enableButton) {
          enableButton.removeAttribute('disabled');
        };




        function onClick(disableButton, enableButton, clicks, clickElement) {
            clicks += 1;
            clickElement.innerHTML = clicks;
            DisableNextButton(disableButton);
            EnableNextButton(enableButton);


        };


        function onClick2(disableButton, enableButton, clicks, clickElement) {
            clicks += 1;
            clickElement.innerHTML = clicks;
            DisableNextButton(disableButton);
            EnableNextButton(enableButton);

        };

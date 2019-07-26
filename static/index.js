        signU = document.querySelectorAll('.signUpButton')

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

        function DisableNextButton(disableButton) {

          disableButton.disabled = 'true';
        };

        function EnableNextButton(enableButton) {
          enableButton.removeAttribute('disabled');
        };




        function onClick(disableButton, enableButton, clicks, clickElement) {
            clicks += 1;
            clickElement.innerHTML = clicks;
            DisableNextButton(disableButton)
            EnableNextButton(enableButton)


        };


        function onClick2(numBer, disableButton, enableButton) {
            clicks += numBer;
            document.getElementById("clicks").innerHTML = clicks;
            DisableNextButton(disableButton)
            EnableNextButton(enableButton)

        };

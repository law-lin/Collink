

        function DisableNextButton(disableButton) {
    document.getElementById(disableButton).disabled = 'true';
        };

        function EnableNextButton(enableButton) {
    document.getElementById(enableButton).removeAttribute('disabled');
        };



        var clicks = 0;
        function onClick(numBer, disableButton, enableButton) {
            clicks += numBer;
            document.getElementById("clicks").innerHTML = clicks;
            DisableNextButton(disableButton)
            EnableNextButton(enableButton)

        };


        function onClick2(numBer, disableButton, enableButton) {
            clicks += numBer;
            document.getElementById("clicks").innerHTML = clicks;
            DisableNextButton(disableButton)
            EnableNextButton(enableButton)

        };

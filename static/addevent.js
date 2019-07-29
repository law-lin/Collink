checkbox = document.getElementById('checkbox')


checkbox.addEventListener('change', (event) => {
  if (event.target.checked) {
    document.getElementById('imageinput').disabled = false;
  } else {
    document.getElementById('imageinput').disabled = true;
  }
});


//Max image size function
var uploadFile = document.getElementById("imageinput");

uploadFile.onchange = function() {
    if(this.files[0].size >= 1048576){
       alert("Image size is too big! Please use an image that is 1 MB or less.");
       this.value = "";
    };
};

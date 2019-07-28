checkbox = document.getElementById('checkbox')


checkbox.addEventListener('change', (event) => {
  if (event.target.checked) {
    document.getElementById('imageinput').disabled = false;
  } else {
    document.getElementById('imageinput').disabled = true;
  }
});

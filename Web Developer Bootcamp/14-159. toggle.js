console.log("Script Connected");
var btn = document.querySelector('button')
btn.addEventListener('click', function () {
    document.body.classList.toggle('clicked');
});
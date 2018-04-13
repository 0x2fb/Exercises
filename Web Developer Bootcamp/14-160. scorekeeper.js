console.log("Script Connected");
var btnp1 = document.getElementById('btnp1');
var btnp2 = document.getElementById('btnp2');
var scorep1 = document.getElementById('scorep1');
var scorep2 = document.getElementById('scorep2');
var matches = document.getElementById('matches');
var matval = document.getElementById('number');
var scovalp1 = 0;
var scovalp2 = 0;


btnp1.addEventListener('click', function () {
    if (scovalp1 < matval & scovalp2 < matval) {
        scovalp1 += 1;
        scorep1.textContent = scovalp1;
    }
});
btnp2.addEventListener('click', function () {
    if (scovalp1 < matval & scovalp2 < matval) {
        scovalp2 += 1;
        scorep2.textContent = scovalp2;
    }
});
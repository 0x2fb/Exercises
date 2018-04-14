console.log("Script Connected");
var p1Button = document.getElementById('p1button');
var p2Button = document.getElementById('p2button');
var p1Display = document.getElementById('p1display');
var p2Display = document.getElementById('p2display');
var p1Score = 0;
var p2Score = 0;
var gameOver = false;
var winningScore = 0;
var numInput = document.getElementById('winningscore');
var matchDisplay = document.getElementById('matchdisplay');
var resetButton = document.getElementById('reset');

function resetGame() {
    p1Score = 0;
    p2Score = 0;
    p1Display.textContent = p1Score;
    p2Display.textContent = p2Score;
    gameOver = false;
    p1Display.classList.remove('winner');
    p2Display.classList.remove('winner');
};

p1Button.addEventListener('click', function () {
    if (!gameOver) {
        p1Score++;
        p1Display.textContent = p1Score;
        if (p1Score === winningScore) {
            console.log("GAME OVER");
            gameOver = true;
            p1Display.classList.toggle('winner');
        }
    }
});
p2Button.addEventListener('click', function () {
    if (!gameOver) {
        p2Score++;
        p2Display.textContent = p2Score;
        if (p2Score === winningScore) {
            console.log("GAME OVER");
            gameOver = true;
            p2Display.classList.toggle('winner');
        }
    }
});
resetButton.addEventListener('click', resetGame);
numInput.addEventListener('change', function () {
    matchDisplay.textContent = numInput.value;
    winningScore = Number(numInput.value);
    resetGame();
});
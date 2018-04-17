var colors = [];
var pickedColor;
var numberOfSquares = 6;
var squares = document.querySelectorAll('.square');
var colorDisplay = document.querySelector('#colorDisplay');
var messageDisplay = document.querySelector('#message');
var h1 = document.querySelector('h1');
var resetButton = document.getElementById('reset');
var modeButtons = document.querySelectorAll('.mode');

function init() {
    resetButton.addEventListener('click', function () {
        reset();
    });
    modeButtonListeners();
    squareListeners();
    reset();
};

function modeButtonListeners() {
    for (var i = 0; i < modeButtons.length; i++) {
        modeButtons[i].addEventListener('click', function () {
            modeButtons[0].classList.remove("selected");
            modeButtons[1].classList.remove("selected");
            modeButtons[2].classList.remove("selected");
            this.classList.add('selected');
            if (this.textContent === "Easy") {
                numberOfSquares = 3;
            } else if (this.textContent === "Normal") {
                numberOfSquares = 6;
            } else {
                numberOfSquares = 9;
            }
            reset();
        })
    };
};

function squareListeners() {
    for (var i = 0; i < squares.length; i++) {
        squares[i].addEventListener('click', function () {
            var clickedColor = this.style.backgroundColor;
            if (clickedColor === pickedColor) {
                messageDisplay.textContent = "Correct";
                changeColors(clickedColor);
                resetButton.textContent = "Play again?";
            } else {
                this.style.backgroundColor = '#232323';
                messageDisplay.textContent = "Try again";
            }
        })
    };
};

function reset() {
    colors = generateRandomColors(numberOfSquares);
    pickedColor = pickColor();
    colorDisplay.textContent = pickedColor;
    messageDisplay.textContent = "";
    h1.style.backgroundColor = 'steelblue';
    resetButton.textContent = "New Colors";
    for (var i = 0; i < squares.length; i++) {
        if (colors[i]) {
            squares[i].style.display = 'block';
            squares[i].style.backgroundColor = colors[i];
        } else {
            squares[i].style.display = 'none';
        }
    }
};

function changeColors(color) {
    for (var i = 0; i < squares.length; i++) {
        squares[i].style.backgroundColor = color;
    };
    h1.style.backgroundColor = color;
};

function pickColor() {
    var random = Math.floor(Math.random() * colors.length);
    return colors[random];
};

function generateRandomColors(num) {
    var col_array = []
    for (var i = 0; i < num; i++) {
        col_array.push(randomColor());
    }
    return col_array;
};

function randomColor() {
    var red = Math.floor(Math.random() * 256);
    var green = Math.floor(Math.random() * 256);
    var blue = Math.floor(Math.random() * 256);
    return 'rgb(' + red + ', ' + green + ', ' + blue + ')';
};

init();
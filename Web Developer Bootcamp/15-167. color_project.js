var numberOfSquares = 6;
var colors = generateRandomColors(numberOfSquares);
var squares = document.querySelectorAll('.square');
var pickedColor = pickColor();
var colorDisplay = document.querySelector('#colorDisplay');
var messageDisplay = document.querySelector('#message');
var h1 = document.querySelector('h1');
var resetButton = document.getElementById('reset');
var easyButton = document.getElementById('easyBtn');
var hardButton = document.getElementById('hardBtn');
colorDisplay.textContent = pickedColor;

easyButton.addEventListener('click', function () {
    easyButton.classList.add('selected');
    hardButton.classList.remove('selected');
    numberOfSquares = 3;
    colors = generateRandomColors(numberOfSquares);
    pickedColor = pickColor();
    colorDisplay.textContent = pickedColor;
    for (var i = 0; i < squares.length; i++) {
        if (colors[i]) {
            squares[i].style.backgroundColor = colors[i];
        } else {
            squares[i].style.display = 'none';
        }
    }
});

hardButton.addEventListener('click', function () {
    hardButton.classList.add('selected');
    easyButton.classList.remove('selected');
    numberOfSquares = 6;
    colors = generateRandomColors(numberOfSquares);
    pickedColor = pickColor();
    colorDisplay.textContent = pickedColor;
    for (var i = 0; i < squares.length; i++) {
        if (squares[i].style.display === 'none') {
            squares[i].style.display = 'block';
        }
        squares[i].style.backgroundColor = colors[i];
    }
});

resetButton.addEventListener('click', function () {
    // generate new colors
    colors = generateRandomColors(numberOfSquares);
    // pick a new random color from the array
    pickedColor = pickColor();
    //change colorDisplay to match picked color
    colorDisplay.textContent = pickedColor;
    //change colors of squares
    for (var i = 0; i < squares.length; i++) {
        squares[i].style.backgroundColor = colors[i];
    }
    h1.style.backgroundColor = 'steelblue';
    resetButton.textContent = "New Colors";
    messageDisplay.textContent = "";
});

for (var i = 0; i < squares.length; i++) {
    // add initial colors to squares
    squares[i].style.backgroundColor = colors[i];
    //add click listeners to squares
    squares[i].addEventListener('click', function () {
        // grab color of clicked square
        var clickedColor = this.style.backgroundColor;
        //compare color to pickedColor 
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

function changeColors(color) {
    //loop through all squares
    for (var i = 0; i < squares.length; i++) {
        //change each color to match given color
        squares[i].style.backgroundColor = color;
    };
    h1.style.backgroundColor = color;
};

function pickColor() {
    var random = Math.floor(Math.random() * colors.length);
    return colors[random];
};

function generateRandomColors(num) {
    // make an array
    var col_array = []
    // add num random colors to the array
    for (var i = 0; i < num; i++) {
        // get random color and push into array
        col_array.push(randomColor());
    } // return the array
    return col_array;
};

function randomColor() {
    // pick a 'red' from 0 to 255
    var red = Math.floor(Math.random() * 256);
    // pick a 'green' from 0 to 255
    var green = Math.floor(Math.random() * 256);
    // pick a 'blue' from 0 to 255
    var blue = Math.floor(Math.random() * 256);
    // return the color as a string
    return 'rgb(' + red + ', ' + green + ', ' + blue + ')';
};
console.log(colors);
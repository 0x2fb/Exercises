function isEven(num) {
  if (num % 2 === 0) {
    return true;
  } else {
    return false;
  }
}
console.log(isEven(4));
console.log(isEven(21));
console.log(isEven(68));
console.log(isEven(333));

function factorial(num) {
  if (num === 0) { return 1; }
  else { num *= factorial(num - 1); }
  return num;
}
console.log(factorial(5));
console.log(factorial(2));
console.log(factorial(10));
console.log(factorial(0));

function kebabToSnake(str) {
  var newString = ''
  for (var i = 0; i < str.length; i++) {
    if (str[i] === '-') { newString += '_'; }
    else { newString += str[i]; }
  } return newString;
}

console.log(kebabToSnake('hello-world'));
console.log(kebabToSnake('dogs-are-awesome'));
console.log(kebabToSnake('blah'));
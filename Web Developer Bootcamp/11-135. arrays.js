function printReverse(ls) {
    for (var i = 0; i < ls.length; i++) {
        console.log(ls[ls.length - i - 1]);
    }
}
printReverse([1, 2, 3, 4]);
printReverse(["a", "b", "c"]);

function isUniform(ls) {
    for (var i = 1; i < ls.length; i++) {
        if (ls[0] !== ls[i]) {
            return false;
        }
    } return true;
}

console.log(isUniform([1, 1, 1, 1]));
console.log(isUniform([2, 1, 1, 1]));
console.log(isUniform(["a", "b", "p"]));
console.log(isUniform(["b", "b", "b"]));

function sumArray(ls) {
    var sum = 0;
    for (var i = 0; i < ls.length; i++) {
        sum += ls[i];
    } return sum;
}

console.log(sumArray([1, 2, 3]));
console.log(sumArray([10, 3, 10, 4]));
console.log(sumArray([-5, 100]));

function max(ls) {
    var max_num = ls[0];
    for (var i = 1; i < ls.length; i++) {
        if (max_num < ls[i]) {
            max_num = ls[i];
        }
    } return max_num;
}

console.log(max([1, 2, 3]));
console.log(max([10, 3, 10, 4]));
console.log(max([-5, 100]));
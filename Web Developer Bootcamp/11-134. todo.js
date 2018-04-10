var todos = ["Buy Milk"];

var input = prompt("What would you like to do?");

while (input !== "quit") {
    if (input === "new") {
        var new_task = prompt("Please enter the task.");
        todos.push(new_task);
    } else if (input === "list") {
        console.log("****************");
        todos.forEach(function (el, i) {
            console.log(i + ": " + el);
        });
        console.log("****************");
    } else if (input === "delete") {
        var trash = prompt("Which index do you want to delete?");
        todos.splice(trash, 1);
    }
    input = prompt("What would you like to do?");
}
console.log("Thanks for using the app.")

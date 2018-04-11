var movies = [
    {
        title: "Arrival",
        rating: 10,
        hasWatched: true
    },
    {
        title: "Departed",
        rating: 10,
        hasWatched: true
    },
    {
        title: "Inception",
        rating: 10,
        hasWatched: true
    },
    {
        title: "The Godfather",
        rating: 8,
        hasWatched: false
    }
];

movies.forEach(function (mov) {
    if (mov.hasWatched) {
        var watched = "You have watched '";
    }
    else {
        var watched = "You have not seen '";
    }
    console.log(watched + mov.title + "' - " + mov.rating + " stars");
}
);
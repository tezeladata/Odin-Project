const myLibrary = [];

function Book(name, author, genre, year) {
    this.name = name,
    this.author = author,
    this.genre = genre,
    this.year = year
}

function addBookToLibrary(form) {
    myLibrary.push(new Book(form.name.value, form.author.value, form.genre.value, form.year.value))
    console.log(myLibrary)
}

const gridContainer = document.getElementById("grid-container")
function displayBook(form) {
    const bookObj = new Book(form.name.value, form.author.value, form.genre.value, form.year.value);

    const html = `<div>
        <h2>${bookObj.name}</h2>
        <h3>${bookObj.author}</h3>
        <em>${bookObj.genre}</em> <br>
        <strong>${bookObj.year}</strong>
      </div>`

    gridContainer.insertAdjacentHTML("beforeend", html)
}

const form = document.getElementById("form1");
form.addEventListener("submit", e => {
    e.preventDefault();

    addBookToLibrary(form)
    displayBook(form)
})
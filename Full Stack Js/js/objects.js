// There are multiple ways to define objects but in most cases, it is best to use the object literal syntax as follows:
const obj1 = {
    name: "David",
    surname: "Tezelashvili",
    age: 16,
    ageInTenYears: function(){
        return this.age + 10
    }
}

console.log(obj1.ageInTenYears())
console.log(obj1["name"])


// One of the simplest ways you can begin to organize your code is by grouping things into objects.
const playerOne = {
  name: "tim",
  marker: "X"
};

const playerTwo = {
  name: "jenn",
  marker: "O"
};

// Now we can use function for easy demonstration:
const display = (player => console.log(player.name))
display(playerOne)



// When you have a specific type of object that you need to duplicate like our player or inventory items, a better way to create them is using an object constructor, which is a function that looks like this:
function Player(name, score){
    this.name = name;
    this.score = score;
}

// Now we can use "new" keyword to create object
const playerThree = new Player("David", 10);
console.log(typeof playerThree)
console.log(playerThree)


// We can also include functions in constructors:
function Student(name, surname, qualification, country){
    this.name = name;
    this.surname = surname;
    this.qualification = qualification;
    this.country = country;
    this.displayAll = (() => console.log(`Hello, this is ${this.name} ${this.surname}. Your degree is: ${this.qualification} and you live in ${this.country}`))
}
const student1 = new Student("David", "Tezelashvili", "Programming", "Georgia");
student1.displayAll()



// Before we go much further, there’s something important you need to understand about JavaScript objects. All objects in JavaScript have a prototype. The prototype is another object that the original object inherits from, which is to say, the original object has access to all of its prototype’s methods and properties.
// The prototype object can have properties and functions, just as these Player objects have properties like .name, .marker, and functions like .sayName() attached to them.
// Here, the “original object” refers to an object like player1 or player2. These objects are said to “inherit”, or in other words, these objects have access to the prototype’s properties or functions, if they have been defined. For example, if there was a .sayHello() function defined on the prototype, player1 can access the function just as if it was its own function - player1.sayHello(). But it’s not just player1 who can call the .sayHello() function, even player2 can call it, since it’s defined on the prototype!


// Prototype check:
console.log(Object.getPrototypeOf(student1) === Student.prototype)

// As said in the earlier point, every Player object has a value which refers to Player.prototype. So: Object.getPrototypeOf(player1) === Object.getPrototypeOf(player2) (returns true).
// So, any properties or methods defined on Player.prototype will be available to the created Player objects!

// Function called "greet" becomes available to all objects created with Student constructor
Student.prototype.greet = (() => console.log("Hello"));
student1.greet()


// Unlike what we have done so far using Object.getPrototypeOf() to access an object’s prototype, the same thing can also be done using the .__proto__ property of the object. However, this is a non-standard way of doing so, and deprecated. Hence, it is not recommended to access an object’s prototype by using this property.
console.log(student1.__proto__ === Player.prototype)


// We can define properties and functions common among all objects on the prototype to save memory. Defining every property and function takes up a lot of memory, especially if you have a lot of common properties and functions, and a lot of created objects! Defining them on a centralized, shared object which the objects have access to, thus saves memory.

// Example of inheritance
console.log(student1.hasOwnProperty("greet"))
console.log(Student.prototype.hasOwnProperty("greet"))

console.log(Object.prototype)

// Every prototype object inherits from Object.prototype by default.
// An object’s Object.getPrototypeOf() value can only be one unique prototype object.



function Person(name) {
  this.name = name;
}

Person.prototype.sayName = function() {
  console.log(`Hello, I'm ${this.name}!`);
};

function Player(name, marker) {
  this.name = name;
  this.marker = marker;
}

Player.prototype.getMarker = function() {
  console.log(`My marker is '${this.marker}'`);
};

Object.getPrototypeOf(Player.prototype); // returns Object.prototype

// Now make `Player` objects inherit from `Person`
Object.setPrototypeOf(Player.prototype, Person.prototype);
Object.getPrototypeOf(Player.prototype); // returns Person.prototype

const player1 = new Player('steve', 'X');
const player2 = new Player('also steve', 'O');

player1.sayName(); // Hello, I'm steve!
player2.sayName(); // Hello, I'm also steve!

player1.getMarker(); // My marker is 'X'
player2.getMarker(); // My marker is 'O'
// The word “scoping” essentially asks, “Where is a certain variable available to me?” - it indicates the current context of a variable. 

// Global scope:
let x = 10
console.log(x)

// Local scope:
{
    let y = 20
}
// console.log(y) ReferenceError: y is not defined


// Before ECMAScript 6, JavaScript had a single keyword to declare a variable, var. These variables can be redefined and updated, and are said to be defined within the function scope, meaning, they are only available within the function they are declared in.
() => {
    // Function scope, var keyword
    var name = "David";
}
// console.log(name) because of function scope, name variable is unavaliable to us


let globalAge = 23; // This is a global variable

// This is a function - and hey, a curly brace indicating a block
function printAge (age) {
  var varAge = 34; // This is a function scoped variable

  // This is yet another curly brace, and thus a block
  if (age > 0) {
    // This is a block-scoped variable that exists
    // within its nearest enclosing block, the if's block
    const constAge = age * 2;
    console.log(constAge);
  }

  // ERROR! We tried to access a block scoped variable
  // not within its scope
//   console.log(constAge); 
}

printAge(globalAge);

// ERROR! We tried to access a function scoped variable
// outside the function it's defined in
// console.log(varAge);



// Closures
function makeAdding(firstNumber){
    const first = firstNumber;

    return function resulting(secondNumber){
        const second = secondNumber;
        return first + second
    }
}

const add5 = makeAdding(5);
console.log(add5(2))
// Same as:
console.log(makeAdding(5)(2))
// The makeAdding function takes an argument, firstNumber, declares a constant first with the value of firstNumber, and returns another function.
// When an argument is passed to the returned function, which we have assigned to add5, it returns the result of adding up the number passed earlier to the number passed now (first to second).


function func1(numberOne){
    const first = numberOne;

    return function func2(numberTwo){
        const second = numberTwo;

        return function func3(numberThree){
            const third = numberThree;

            return first * second * third;
        }
    }
}
console.log(func1(20)(5)(10))


// Why constructors are bad:
// If you try to use a constructor function without the new keyword, not only does your program fail to work, but it also produces error messages that are hard to track down and understand.
// Yet another issue stems from the way the instanceof works. It checks the presence of a constructor’s prototype in an object’s entire prototype chain - which does nothing to confirm if an object was made with that constructor since the constructor’s prototype can even be reassigned after the creation of an object.



// Factory functions:
// Factory functions work very similar to how constructors did, but with one key difference - they levy the power of closures. Instead of using the new keyword to create an object, factory functions set up and return the new object when you call the function.

// we can Create factory function using following:
function createUser (name){
    const discordName = "@" + name;
    return {name, discordName}
}
console.log(createUser("David")) // factory functions should return object. main upside is that new keyword was not used
// Similar task, but using constructor function:
const createUser2 = function(name){
    this.name = name;
    this.discordName = "@" + name;
}
console.log(new createUser2("David"))


function createShape(type, ...dimensions){
    switch(type){
        case "Circle": 
            return {
                type: "Circle",
                radius: dimensions[0],
                getArea () {
                    return Math.PI * this.radius**2
                },
                getPerimeter () {
                    return 2 * Math.PI * this.radius
                }
            }
        case "Square":
            return {
                type: "Square",
                sideLength: dimensions[0],
                getArea() {
                    return this.sideLength**2
                },
                getPerimeter() {
                    return this.sideLength*4
                }
            }
        case "Rectangle":
            return {
                type: "Rectangle",
                width: dimensions[0],
                height: dimensions[1],
                getArea(){
                    return this.width * this.height
                },
                getPerimeter(){
                    return (this.width + this.height) * 2
                }
            }
    }
}
const circ1 = createShape("Circle", 3)
console.log(circ1.getArea(), circ1.getPerimeter())
const rect1 = createShape("Rectangle", 3, 4)
console.log(rect1)



// Destucting
const {a, b} = {a: 1, b: 2}
console.log(b);
console.log(a)

const [c, ...d] = [1, 2, 3, 4, 5];
console.log(c);
console.log(d)



// Private variables:
function createUser (name) {
  const discordName = "@" + name;

  let reputation = 0;
  const getReputation = () => reputation;
  const giveReputation = () => reputation++;

  return { name, discordName, getReputation, giveReputation };
}

const josh = createUser("josh");
josh.giveReputation();
josh.giveReputation();

console.log({
  discordName: josh.discordName,
  reputation: josh.getReputation()
});

josh.giveReputation();
josh.giveReputation();
// We have increased variable reputation's value by two, and in console reputation will have value set to four
console.log({
  discordName: josh.discordName,
  reputation: josh.getReputation()
});


// Concerning factory functions, a private variable or function uses closures to create smaller, dedicated variables and functions within a factory function itself - things that we do not need to return in the object itself. This way we can create neater code, without polluting the returned object with unnecessary variables that we create while creating the object itself. Often, you do not need every single function within a factory to be returned with the object, or expose an internal variable. You can use them privately since the property of closures allows you to do so.
// In this case we used reputation as private variable



// Prototypal inheritance with factories
// function createPlayer (name, level) {
//   const { getReputation, giveReputation } = createUser(name);

//   const increaseLevel = () => level++;
//   return { name, getReputation, giveReputation, increaseLevel };
// }

// We just used createUser to create one object in createPlayer function.
// level is argument passed directly to createPlayer
// increase level is just function which increments level variable
// At last, we return name (createPlayer), getReputation (createUser), giveReputation (createUser) and increaseLevel (createPlayer)
// getReputation are giveReputation inherited from createUser

// We can simplify it even more, use object.assign:
function createPlayer (name, level) {
  const user = createUser(name);

  const increaseLevel = () => level++;
  return Object.assign({}, user, { increaseLevel });
}
const user1 = createPlayer("Hello", 0);
user1.increaseLevel()
console.log(user1.increaseLevel())

// giveReputation and getReputation is accesible because they are created in createUser function
user1.giveReputation();
console.log(user1.getReputation())




// iife
const calculator = (function () {
  const add = (a, b) => a + b;
  const sub = (a, b) => a - b;
  const mul = (a, b) => a * b;
  const div = (a, b) => a / b;
  return { add, sub, mul, div };
})(); // Immediately invoked

console.log(calculator.add(3,5))
console.log(calculator.sub(6,2))
console.log(calculator.mul(14,5534))

// This is where we encounter the word encapsulation - bundling data, code, or something into a single unit, with selective access to the things inside that unit itself. While it sounds general, this is what happens when we wrap, or encapsulate our code into modules - we don’t expose everything to the body of our program itself. This encapsulation leads to an effect called namespacing. Namespacing is a technique that is used to avoid naming collisions in our programs.
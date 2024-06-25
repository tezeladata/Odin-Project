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
// აქიდან ვაგრძელებ შემდეგზე
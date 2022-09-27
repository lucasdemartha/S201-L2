class Animal {
    constructor(name, age, species) {
        this.name = name;
        this.age = age;
        this.species = species;
    }
    printInfo() {
        console.log(`${this.name} is ${this.age} years old and is a ${this.species}`);
    }
}

class Dog extends Animal {
    constructor(name, age, species, breed) {
        super(name, age, species);
        this.breed = breed;
    }
   
    printInfo() {
        console.log(`${this.name} is ${this.age} years old and is a ${this.species} and is of the ${this.breed} breed`);
    }

}

class Cat extends Animal {
    constructor(name, age, species, furColor) {
        super(name, age, species);
        this.furColor = furColor;
    }

    printInfo() {
        console.log(`${this.name} is ${this.age} years old and is a ${this.species} and has ${this.furColor} fur`);
    }
}

let dog = new Dog('Bob', 2, 'dog', 'Labrador');
dog.printInfo();

let furColor = ['black', 'brown', 'white'];
let cat = new Cat('John', 6, 'cat', furColor);
cat.printInfo();
let animal = new Animal('Reptil', 7, 'Lagarto');
animal.printInfo()
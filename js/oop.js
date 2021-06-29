// наследование
// let admin = {
//     rules: 777,
//     isAdmin(){
//         console.log("Админ: " + this.name + ", права - " + this.rules)
//     },
// }
// let user = {
//     name: "Ivan",
//     age: 20,
//     __proto__: admin
// }

function User(name, age) {
    this.name = name;
    this.age = age;
    this.myInfo = function () {
        console.log("Меня зовут " + this.name + ", мне " + this.age + " лет")
    }
}

let u1 = new User("Ivan", 27)
let u2 = new User("Petr", 21)
let u3 = new User("Masha", 24)

// 16:00

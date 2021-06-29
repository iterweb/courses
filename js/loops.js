// **цикл while

// let counter = 0;
// while (counter < 10){
//     console.log(counter);
//     counter ++;
// }


// преждевременное завершение цикла while

// let counter = 0;
// while (counter < 10){
//     console.log(counter);
//     if (counter == 4){
//         break;
//     }
//     counter ++;
// }


// **цикл do while (выполняется как миниму один раз)

// let count = 10;
// do{
//     console.log(count)
//     count --;
// }
// while (count > 7)


// **цикл for

// for(let i=0; i<10; i+=2){
//     console.log(i)
// }

// let arr = [2, 4, 1, 5, 0, 7]
// for (let i=0; i<arr.length; i++){
//     console.log(arr[i]*2)
// }


// **цикл for of (работа с массивами)

// let arr = [2, 4, 1, 5, 0, 7]
// for(let item of arr){
//     console.log(item*2)
// }


// **цикл for in (работа с обьектами(словарями))

// let obj = {'name': 'Ivan', 'age': 20, 'number': 231242124}
// for(let key in obj){
//     console.log(`Ключ - ${key} , Значение - ${obj[key]}`)
// }


// let arr = [2, 4, 1, 5, 0, 7]
// arr.forEach(function (item, index, array){
//     console.log(`Элемент: ${item}\nИндекс: ${index}\nУмноженный элемент: ${item*2}\nМассив: ${array}`)
// })

/*
let people = [
    {'id': 1, 'name': 'Ivan'},
    {'id': 2, 'name': 'Collin'},
    {'id': 3, 'name': 'Nick'},
    {'id': 4, 'name': 'Peter'},
]
let a = people.find(function (item) {
    if(item.id == 3) return item
})
console.log(`Вывод обьекта, где ключ(id) равен 3, это ${a}`)
console.log(a)

let b = people.findIndex(function (item) {
    if(item.id == 2) return item
})
console.log(`Вывод индекса обьекта, где ключ(id) равен 2, индекс равен ${b}`)

let c = people.filter(function (item) {
    if(item.id < 3) return item
})
console.log('Вывод массива обьектов, которые подходят под условие')
console.log(c)
 */

// let arr = [2, 4, 1, 5, 0, 7]
// let new_arr = arr.map(function (item) {
//     return item*3
// })
// console.log(new_arr)
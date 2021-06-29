// create an array from 0 to 20 with pair values
let arr_1 = []
for(let i=0; i<21; i+=2){
    arr_1.push(i)
}
console.log(arr_1)

// create an array of 30 divisible by 3 without remainder
let arr_2 = []
for(let i=30; i>0; i-=3){
    arr_2.push(i)
}
console.log(arr_2)

let arr_3 = []
for(let i=30; i>0; i--){
    if(i%3 == 0){
        arr_3.push(i)
    }
}
console.log(arr_3)

// find all even numbers of an array
let random_arr = [2, 12, 5, 17, 0, 33, 10, 6, 13, 20, 44, 15]
let even_arr = []
let count = 0;

for(let item of random_arr){
    if(item%2 == 0){
        even_arr.push(item)
        count ++;
    }
}
console.log(even_arr, count)
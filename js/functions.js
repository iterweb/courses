// сортировка списка
/*
//первый способ
let arr = [1, 43, 5, 23, 7, 12, 8, 13, 44, 89, 12, 4, 0]
arr.sort((a, b) => a - b)
console.log(arr)

// второй способ
arr.sort(function (a, b) {
    return a - b
})
console.log(arr)

// третий способ
arr.sort(function (a, b) {
    if(a == b) return 0
    if(a > b) return 1
    if (a < b) return -1
})
console.log(arr)
 */

// число фибоначи
/*
function fibonachi (count) {
    let fib = []
    for (let i=0; i<count; i++) {
        if (i == 0) fib[i] = 0;
        else if (i == 1) fib[i] = 1;
        else fib[i] = fib[i-2] + fib[i-1];
    }
    return fib;
}
let f = fibonachi(10);
console.log(f)
 */

// вычисление факториала числа
/*
function factorial(n) {
    let fact = 1;
    if (n == 0) return fact;
    for (let i=1; i<=n; i++) {
        fact *= i;
    }
    return fact;
}
let f = factorial(3);
console.log(f)
 */

/*
let addAndMul = function (num) {
    num += "";
    let add = 0, mul = 1;
    for (let i=0; i<num.length; i++) {
        add += +num[i];
        mul *= num[i];
    }
    return {
        'Сумма': add,
        'Произведение': mul
    }
}
console.log(addAndMul(795))
 */


// реверс числа
/*
function reverse(number) {
    number += "";
    let reverse_number = "";
    for(let i=number.length - 1; i>=0; i--){
        reverse_number += number[i]
    }
    return +reverse_number
}
let n = reverse(3849);
console.log(n)
 */


// подсчитать кол. чётных и не чётных цифр в числе
/*
function number(num) {
    num += "";
   let chet = 0, nechet = 0;
   for(let i=0; i<num.length; i++){
       if(num[i] % 2 == 0) chet++;
       else nechet++;
   }
   return {
       'Четные цифры': chet,
       'Нечетные цифры': nechet
   }
}
let n = number(3849);
console.log(n)
 */


// угадать число от 0 до 100, за 10 попыток
function random_number() {
    let number = Math.floor(Math.random()*100)
    for(let i=1; i<=10; i++) {
        let result = prompt(`Попытка №${i}, введите число:`)
        if(+result == number) {
            return alert(`Победа!!!\nПопытка: №${i}\nЧисло: ${number}`)
        }
        else if(+result < number) {
            alert(`Ваше число ${result}, меньше загаданного`)
        }
        else if(+result > number) {
            alert(`Ваше число ${result}, больше загаданного`)
        }
    }
    return alert(`Вы не угадали число ${number}`)
}
random_number()
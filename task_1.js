/* Задача 1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки. */

"use strict";

const arr = [2, 5, 6, 10, 1, 3];

const res = sort_list_imperative(arr);
console.log(res);

function sort_list_imperative(numbers) {
    
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (numbers[j] < numbers[j + 1]) {
       const temp =  numbers[j];
       numbers[j] = numbers[j + 1];
       numbers[j + 1] = temp;
      }
    }
  }
  return numbers;
}

/* Задача №2
Написать точно такую же процедуру, но в декларативном стиле */

const res2 = arr.sort((a, b) => b - a);
console.log(res2);

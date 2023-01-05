import { readFileSync } from 'fs';

let stacks: Array<string> = readFileSync('dane.txt', 'utf-8').split('\n');
let procedures: Array<string> = readFileSync('dane2.txt', 'utf-8').split('\n');

const create_stacks = (
  content: Array<string>,
  numbersOfStacks: number
): Array<Array<string>> => {
  let charsInRow = content[0].toString().length;
  let stacks = new Array(numbersOfStacks);

  for (let i = 0; i < numbersOfStacks; i++) {
    stacks[i] = new Array();
  }

  for (let i = 0; i < content.length - 1; i++) {
    let arr = content[i].toString();

    for (let j = 0; j < charsInRow; j += 4) {
      let a = arr.slice(j, j + 3);
      if (a.trim() === '') {
        continue;
      }
      stacks[j / 4].push(a);
    }
  }
  return stacks;
};

const move_from_stack = (
  stacks: Array<Array<string>>,
  indexStack: number,
  amount: number,
  destination: number
): void => {
  for (let i = 0; i < amount; i++) {
    let crate = stacks[indexStack][0];
    stacks[indexStack].shift();
    stacks[destination].unshift(crate);
  }
};

const move_from_stack_v2 = (
  stacks: Array<Array<string>>,
  indexStack: number,
  amount: number,
  destination: number
): void => {
  let crates = stacks[indexStack].slice(0, amount);
  stacks[indexStack].splice(0, amount);
  for (let i = crates.length - 1; i > -1; i--) {
    stacks[destination].unshift(crates[i]);
  }
};

const crateMover = (
  procedures: Array<string>,
  stacks: Array<Array<string>>,
  moverType: number
) => {
  for (let i = 0; i < procedures.length - 1; i++) {
    let arr = procedures[i].split(' ');
    let amount = parseInt(arr[1]);
    let indexStack = parseInt(arr[3]) - 1;
    let destination = parseInt(arr[5]) - 1;

    if (moverType === 9000) {
      move_from_stack(stacks, indexStack, amount, destination);
    }
    if (moverType === 9001) {
      move_from_stack_v2(stacks, indexStack, amount, destination);
    }
  }
};

let stacksArray1 = create_stacks(stacks, 9);
crateMover(procedures, stacksArray1, 9000);

let answer1 = '';
stacksArray1.forEach((element) => {
  answer1 += element[0].charAt(1);
});

let stacksArray2 = create_stacks(stacks, 9);
crateMover(procedures, stacksArray2, 9001);
let answer2 = '';
stacksArray2.forEach((element) => {
  answer2 += element[0].charAt(1);
});

console.log(`Part one: ${answer1}`);
console.log(`Part two: ${answer2}`);

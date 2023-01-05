import { readFileSync } from 'fs';

let signal: Array<string> = readFileSync('dane.txt', 'utf-8').split('\n');

const check_unique = (signal_array: Array<string>, amount: number): boolean => {
  if (new Set(signal_array).size == amount) return true;
  return false;
};

const part_one = (signal: string): number => {
  let signal_array = new Array();
  for (let i = 0; i < signal.length; i++) {
    signal_array[i] = signal.charAt(i);
  }

  for (let i = 0; i < signal_array.length; i++) {
    if (check_unique(signal_array.slice(i, i + 4), 4)) {
      return i + 4;
    }
  }
  return -1;
};

const part_two = (signal: string): number => {
  let signal_array = new Array();
  for (let i = 0; i < signal.length; i++) {
    signal_array[i] = signal.charAt(i);
  }

  for (let i = 0; i < signal_array.length; i++) {
    if (check_unique(signal_array.slice(i, i + 14), 14)) {
      return i + 14;
    }
  }
  return -1;
};

console.log(`Part one: ${part_one(signal[0])}`);
console.log(`Part two: ${part_two(signal[0])}`);
